#!/usr/bin/env python3
"""Check newly introduced README URLs with Lychee; leave quality decisions to review."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlsplit

# These responses require independent verification, not a conclusion of unavailability.
REVIEW_CODES = {202, 401, 403, 429}


def extract_urls(path, config):
    result = subprocess.run(
        ["lychee", "--config", str(config), "--dump", "--verbose", "--no-progress",
         "--include", "^https?://", str(path)],
        check=True, capture_output=True, text=True,
    )
    # Verbose dump also includes built-in exclusions (such as example domains).
    urls = (line.split()[0] for line in result.stdout.splitlines() if line.strip())
    return {url for url in urls if urlsplit(url).scheme in {"http", "https"}}


def classify(report, returncode, urls):
    """Reject hard failures and incomplete reports; distinguish unverified URLs."""
    if returncode not in {0, 2}:
        raise ValueError(f"Lychee failed to run (exit {returncode})")
    failures, review, seen = [], [], set()
    for key in ("success_map", "error_map", "timeout_map", "excluded_map"):
        for entries in report.get(key, {}).values():
            for entry in entries:
                url, status = entry["url"], entry["status"]
                seen.add(url)
                if key == "excluded_map" or status.get("code") in REVIEW_CODES:
                    review.append(url)
                elif key != "success_map":
                    failures.append(f"{url}: {status['text']}")
    if seen != set(urls) or report.get("unknown", 0) or report.get("unsupported", 0):
        raise ValueError("Lychee report is incomplete or contains unsupported results")
    return failures, sorted(set(review))


def check_urls(urls, config):
    with tempfile.TemporaryDirectory() as directory:
        temp = Path(directory)
        inputs = temp / "links.txt"
        inputs.write_text("\n".join(urls) + "\n")
        output = temp / "report.json"
        result = subprocess.run([
            "lychee", "--config", str(config), "--cache=false", "--no-progress", "--verbose",
            "--accept", "200,204,206", "--timeout", "20",
            "--format", "json", "--output", str(output), str(inputs),
        ], check=False)
        return classify(json.loads(output.read_text()), result.returncode, urls)


def announce(level, message):
    print(f"{level.upper()}: {message}")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        escaped = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::{level}::{escaped}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", help="PR base commit SHA")
    parser.add_argument("head", help="PR head commit SHA")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as directory:
        temp = Path(directory)
        # Read exact commits, never merge-base guesses or unrelated base changes.
        for ref, name in ((args.base, "base.md"), (args.head, "head.md")):
            content = subprocess.check_output(["git", "show", f"{ref}:README.md"])
            (temp / name).write_bytes(content)
        # Use established exclusions. Proposed policy changes need separate review.
        config = temp / "lychee.toml"
        config.write_bytes(subprocess.check_output(["git", "show", f"{args.base}:lychee.toml"]))
        empty_config = temp / "extract.toml"
        empty_config.write_text("")
        urls = sorted(extract_urls(temp / "head.md", empty_config)
                      - extract_urls(temp / "base.md", empty_config))
        if not urls:
            announce("notice", "No newly introduced README URLs. Human review still applies to new entries and changed descriptions.")
            return 0
        insecure = [url for url in urls if urlsplit(url).scheme != "https"]
        if insecure:
            announce("error", "New external URLs must use HTTPS: " + ", ".join(insecure))
            return 1
        failures, review = check_urls(urls, config)
        for url in review:
            announce("warning", f"Manual verification required (excluded or access/challenge response): {url}")
        for failure in failures:
            announce("error", failure)
        summary = (f"Checked {len(urls)} new URLs: {len(failures)} failures; "
                   f"{len(review)} require manual verification. Reachability does not establish quality.")
        announce("notice", summary)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as stream:
                stream.write(summary + "\n\n")
                # Plain code blocks avoid rendering submitted URLs as HTML in the summary.
                if review:
                    stream.write("Review access/challenge responses and exclusions in the warning annotations.\n")
        return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
