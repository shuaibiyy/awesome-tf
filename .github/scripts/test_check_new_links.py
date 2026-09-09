"""Regression tests for URL selection and the failure/manual-review boundary."""
import http.server
import threading
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

from check_new_links import check_urls, classify, extract_urls, main


class SelectionTests(unittest.TestCase):
    def test_markdown_forms_and_unchanged_broken_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / "empty.toml"
            config.write_text("")
            base, head = root / "base.md", root / "head.md"
            base.write_text("- [Old](https://old.invalid/dead) - Old description.\n")
            head.write_text('''- [Old](https://old.invalid/dead) - Edited description.
- [New][project]
[project]: https://new.invalid/tool
- [Inline](https://new.invalid/a_(b))
<a href="https://new.invalid/html">HTML</a>
''')
            old, new = extract_urls(base, config), extract_urls(head, config)
            self.assertEqual(len(new - old), 3)
            self.assertIn("https://new.invalid/tool", new - old)
            self.assertNotIn("https://old.invalid/dead", new - old)
            self.assertTrue(any("a_(b)" in url for url in new))
            head.write_text("- [Old](https://old.invalid/dead) - Edited description.\n")
            self.assertEqual(extract_urls(head, config) - old, set())
            head.write_text("- [New](http://new.invalid/tool)\n")
            self.assertEqual(extract_urls(head, config), {"http://new.invalid/tool"})


class EntrypointTests(unittest.TestCase):
    def run_main(self, head):
        def git_show(command):
            if command[-1].endswith(":lychee.toml"):
                return b""
            if command[-1].startswith("base:"):
                return b"- [Old](https://old.invalid/dead) - Old description.\n"
            return head.encode()
        with patch("sys.argv", ["check_new_links.py", "base", "head"]), patch(
            "check_new_links.subprocess.check_output", side_effect=git_show
        ), patch("check_new_links.announce"), patch("check_new_links.check_urls") as network:
            result = main()
            network.assert_not_called()
            return result

    def test_description_only_does_not_check_existing_broken_url(self):
        self.assertEqual(self.run_main("- [Old](https://old.invalid/dead) - New description.\n"), 0)

    def test_new_http_url_is_rejected(self):
        self.assertEqual(self.run_main("- [New](http://new.invalid/tool)\n"), 1)


class ReportTests(unittest.TestCase):
    def report(self, key, code=None, text="result"):
        status = {"text": text}
        if code is not None:
            status["code"] = code
        return {key: {"links.txt": [{"url": "https://tool.test/", "status": status}]}}

    def test_reachable_and_redirect_destination(self):
        report = self.report("success_map", 200)
        report["redirect_map"] = {"https://tool.test/": "https://tool.test/docs"}
        self.assertEqual(classify(report, 0, {"https://tool.test/"}), ([], []))

    def test_hard_network_failures(self):
        for key, reason in (("error_map", "DNS failure"), ("error_map", "TLS failure"),
                            ("error_map", "Connection refused"), ("timeout_map", "Timeout"),
                            ("error_map", "404 Not Found")):
            with self.subTest(reason=reason):
                failures, review = classify(self.report(key, text=reason), 2, {"https://tool.test/"})
                self.assertEqual(len(failures), 1)
                self.assertEqual(review, [])

    def test_bot_responses_and_exclusions_need_review(self):
        for code in (202, 401, 403, 429):
            with self.subTest(code=code):
                self.assertEqual(classify(self.report("error_map", code), 2, {"https://tool.test/"}),
                                 ([], ["https://tool.test/"]))
        self.assertEqual(classify(self.report("excluded_map"), 0, {"https://tool.test/"}),
                         ([], ["https://tool.test/"]))

    def test_incomplete_report_and_execution_failure(self):
        for report, code in (({}, 0), (self.report("success_map", 200), 1)):
            with self.assertRaises(ValueError):
                classify(report, code, {"https://tool.test/"})


class NetworkTests(unittest.TestCase):
    def test_real_requests_redirects_and_review_responses(self):
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                code = 302 if self.path == "/redirect" else int(self.path[1:])
                self.send_response(code)
                if code == 302:
                    self.send_header("Location", "/200")
                self.end_headers()
                self.wfile.write(b"Test resource")

            def log_message(self, *args):
                pass

        with http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            try:
                with tempfile.TemporaryDirectory() as directory:
                    config = Path(directory) / "lychee.toml"
                    config.write_text('max_retries = 0\ntimeout = 2\nexclude = ["/excluded$"]\n')
                    base = f"http://127.0.0.1:{server.server_port}"
                    urls = [base + path for path in ("/200", "/redirect", "/401", "/403", "/429", "/202", "/404", "/excluded")]
                    failures, review = check_urls(urls, config)
                    self.assertEqual(len(failures), 1)
                    self.assertIn("/404", failures[0])
                    self.assertEqual(set(review), {base + path for path in ("/401", "/403", "/429", "/202", "/excluded")})
            finally:
                server.shutdown()
                worker.join()


if __name__ == "__main__":
    unittest.main()
