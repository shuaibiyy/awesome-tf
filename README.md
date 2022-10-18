# Awesome Terraform [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) <!-- omit in toc -->

> A curated list of resources on [HashiCorp's Terraform](https://www.terraform.io/).
> [<img src="https://rawgit.com/shuaibiyy/awesome-terraform/master/terraform.svg" align="right" width="100">](https://terraform.io)
> Your [contributions](https://github.com/shuaibiyy/awesome-terraform/blob/master/contributing.md) are welcome!

Terraform enables you to safely and predictably create, change, and improve production infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

Sponsored by [Scalr - Terraform Automation & Collaboration Software](https://scalr.com/?utm_source=awesome-terraform)

<a href="https://www.scalr.com/?utm_source=awesome-terraform" target="_blank"><img src="https://bit.ly/2VPBJDv" alt="Scalr - Terraform Automation & Collaboration Software" width="175" height="40" /></a>

## Contents <!-- omit in toc -->

- [Legend](#legend)
- [Official Resources](#official-resources)
- [Community](#community)
- [Books](#books)
- [Tutorials and Blog Posts](#tutorials-and-blog-posts)
  - [Beginner Guides](#beginner-guides)
  - [Writing Custom Providers](#writing-custom-providers)
  - [How-To](#how-to)
  - [Multi-Environment Configuration](#multi-environment-configuration)
  - [Azure](#azure)
  - [AWS](#aws)
  - [Google Cloud](#google-cloud)
  - [Miscellaneous](#miscellaneous)
- [Community Modules](#community-modules)
- [Private Module Registries](#private-module-registries)
- [Private Provider Registries](#private-provider-registries)
- [Providers](#providers)
  - [Hashicorp supported providers](#hashicorp-supported-providers)
  - [Vendor supported providers](#vendor-supported-providers)
- [Testing](#testing)
- [Tools](#tools)
- [Libraries](#libraries)
- [Boilerplates](#boilerplates)
- [Terraform Enterprise](#terraform-enterprise)
- [Videos](#videos)
- [Editor Plugins](#editor-plugins)
- [License](#license)

## Legend

- Not compatible with _terraform >= 0.12_ :ghost:
- Abandoned :skull:
- Monetized :heavy_dollar_sign:

## Official Resources

- [Hashicorp Terraform Blog](https://www.hashicorp.com/blog/products/terraform)
- [Introduction to Terraform](https://www.terraform.io/intro/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Terraform GitHub Actions](https://github.com/hashicorp/setup-terraform)
- [Terraform learn](https://learn.hashicorp.com/terraform/)

## Community

- [weekly.tf - Terraform Weekly Newsletter](https://weekly.tf) - Various news in the Terraform world (projects, announcements, discussions).
- [Complete Terraform documentation as PDF files (Updated nightly)](https://github.com/antonbabenko/terraform-docs-as-pdf)
- [Terraform AWS Modules](https://github.com/terraform-aws-modules) + [meta-configurations repository](https://github.com/terraform-aws-modules/meta)
- [Terraform Bug Tracker](https://github.com/hashicorp/terraform/issues)
- [Terraform Community Modules](https://github.com/terraform-community-modules)
- [Terraform Twitter Community](https://twitter.com/i/communities/1501688565884928007)
- [Terraform Gitter](https://gitter.im/hashicorp-terraform)
- [Terraform Discuss](https://discuss.hashicorp.com/c/terraform-core/27)
- [Terraform Provider/Module Registry](https://registry.terraform.io/)
- [Terraform PDF Doc](https://github.com/dohsimpson/terraform-doc-pdf) :skull:
- [Terragrunt Reference Architecture](https://github.com/antonbabenko/terragrunt-reference-architecture)
- Language-specific communities:
  - [Telegram (Ukrainian speak community)](https://t.me/terraform_ukraine)

## Books

- [Big Little Book On Terraform](https://www.amazon.com/Big-Little-Book-Terraform-Omos-ebook/dp/B07PWYPNX8/)
- [Bootstrapping Microservices with Docker, Kubernetes, and Terraform, Second Editon](https://www.manning.com/books/bootstrapping-microservices-with-docker-kubernetes-and-terraform-second-edition)
- [Deep-Dive Terraform on Azure](https://link.springer.com/book/10.1007/978-1-4842-7328-9)
- [Getting Started with Terraform, 2nd ed.](https://www.amazon.com/Getting-Started-Terraform-production-infrastructure/dp/1788623533/)
- [HashiCorp Infrastructure Automation Certification Guide](https://www.amazon.com/HashiCorp-Infrastructure-Automation-Certification-Guide-ebook/dp/B092KM7LXC/)
- [Infrastructure as Code](http://shop.oreilly.com/product/0636920039297.do)
- [Patterns and Practices for Infrastructure as Code: With examples in Python and Terraform](https://www.manning.com/books/patterns-and-practices-for-infrastructure-as-code)
- [Terraform Best Practices](https://www.terraform-best-practices.com/) - [open-source ebook](https://github.com/antonbabenko/terraform-best-practices)
- [Terraform Cookbook](https://www.amazon.com/Terraform-Cookbook-Efficiently-Infrastructure-platforms/dp/1800207557)
- [Terraform in Action](https://www.manning.com/books/terraform-in-action)
- [Terraform: Up & Running, 3rd ed.](https://www.terraformupandrunning.com/)
- [The Terraform Book](https://terraformbook.com/)

## Tutorials and Blog Posts

### Beginner Guides

- [A Comprehensive Guide to Terraform](https://blog.gruntwork.io/a-comprehensive-guide-to-terraform-b3d32832baca#.w9x897ywp) - Series of blog posts from the author of "Terraform: Up & Running" that guide the reader from beginning with Terraform to using it in the real world.
- [Using Terraform for Cloud Deployments - Part 1](https://dev.to/koenighotze/using-terraform-for-cloud-deployments---part-1) - Provisioning an EC2 instance.
- [Hello, world: The Fargate/Terraform tutorial I wish I had](https://section411.com/2019/07/hello-world/) - Blog post describing setting up an ECS Fargate cluster from scratch

### Writing Custom Providers

- [Creating custom terraform providers](https://medium.com/@jozmo/creating-custom-terraform-providers-341311823fa2) - Guide for creating custom providers.
- [Writing a Terraform provider](https://web.archive.org/web/20220516140659/http://blog.jfabre.net/2017/01/22/writing-terraform-provider/) - Guide for creating custom providers.
- [Writing Custom Providers](https://www.terraform.io/docs/extend/writing-custom-providers.html) - Official documentation for creating custom providers.

### How-To

- [How To Write OPA for Terraform](https://www.scalr.com/blog/opa-series-part-1-open-policy-agent-and-terraform/) - How to use Open Policy Agent to evaluate and enforce policy on your Terraform plans
- [Deploying Discourse with Terraform](https://web.archive.org/web/20181001135342/http://www.hashicorp.com/blog/deploying-discourse-with-terraform) - Shows how Terraform can create a running instance of Discourse on DigitalOcean in one command.
- [Deploying Django to AWS ECS with Terraform](https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/) - Looks at how to use Terraform to spin up the required AWS infrastructure for running a Django app on ECS.
- [Easily Deploy A Seneca Microservice to ECS with Wercker and Terraform: Part I](http://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-i/), [II](http://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-ii/) & [III](http://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-i/) - Illustrates how Terraform can be incorporated into a microservice deployment pipeline.
- [Terraform for a Highly Available VPN between AWS and Azure](https://web.archive.org/web/20210616132857/https://deployeveryday.com/2020/04/13/vpn-aws-azure-terraform.html) - Terraform code to deploy a highly available VPN between AWS and Azure.
- [Terraforming 1Password](https://blog.agilebits.com/2018/01/25/terraforming-1password/) - How 1Password migrated from CloudFormation to Terraform.
- [Tutorial: How to Use Terraform to Deploy OpenStack Workloads](https://web.archive.org/web/20170611135511/http://www.stratoscale.com/blog/openstack/tutorial-how-to-use-terraform-to-deploy-openstack-workloads/) - Illustrates how easy it is to use the OpenStack Terraform provider to deploy a web server.
- [Zero Downtime Updates with HashiCorp Terraform](https://www.hashicorp.com/blog/zero-downtime-updates-with-terraform) - Ensuring zero downtime of your infrastructure.
- [Google Cloud Platform for 10$ a month using terraform](https://github.com/nufailtd/terraform-budget-gcp) - Shows how to use terraform to create a secure Google Kubernetes Cluster, Google Cloud Run Services and other infrastructure elements for less than [10$](https://nufailtd.github.io/budget-gcp/) a month.

### Multi-Environment Configuration

- [Terraform Design Patterns: the Terrafile](http://bensnape.com/2016/01/14/terraform-design-patterns-the-terrafile/) - Managing Terraform modules and their versions within Terraform projects with Terrafile.
- [Terraform, VPC, and why you want a tfstate file per env](https://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/) - Some gotchas surrounding using Terraform in large projects with multiple environments and how to avoid them.
- [Using Pipelines to Manage Environments with Infrastructure as Code](https://medium.com/@kief/https-medium-com-kief-using-pipelines-to-manage-environments-with-infrastructure-as-code-b37285a1cbf5) - Explains different approaches for building a pipeline to handle infrastructure changes moving from one environment to the next.

### Azure

- [Learning HashiCorp Terraform](https://web.archive.org/web/20201108000713/https://www.g10s.io/hashicorp-terraform/) - Guide for Azure.
- [New Terraform Azure Automation Resources](https://bgelens.nl/terraform-automation-resources/) - Azure Automation.
- [Terraforming Azure PaaS](https://devkimchi.com/2019/01/21/terraforming-azure-paas/) - Deploy PaaS Resources on Azure.

### AWS

- [AWS Lambda the Terraform Way](https://github.com/nsriram/lambda-the-terraform-way) - Understand AWS Lambda in-depth, beyond executing functions, using Terraform. Also includes guides for integration with S3, API Gateway, DynamoDB, Kinesis, SQS.
- [Managing AWS Lambda Functions with Terraform](https://spacelift.io/blog/terraform-aws-lambda) - What is AWS Lambda used for and how to use Terraform to manage AWS Lambda functions?

### Google Cloud
- [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://cloud.google.com/architecture/managing-infrastructure-as-code) - Setup and manage infrastructure as code with Terraform, Cloud Build, and GitOps.
- [Getting started with Terraform on Google Cloud](https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform) - Using Terraform to create a VM in Google Cloud and Starting a basic Python Flask server.
- [Managing Cloud Infrastructure with Terraform](https://www.cloudskillsboost.google/quests/44) - Deploy Kubernetes Load Balancer Service with Terraform,HTTPS Content-Based Load Balancer with Terraform,Modular Load Balancing with Terraform - Regional Load Balancer, Custom Providers with Terraform, Cloud SQL with Terraform,Building a VPN Between Google Cloud and AWS with Terraform.
- [Hashicorp Terraform Tutorials for Google Cloud](https://learn.hashicorp.com/collections/terraform/gcp-get-started) - Get started with Terraform on Google Cloud.

### Miscellaneous

- [Sharing data between Terraform configurations](https://jamesmckay.net/2016/09/sharing-data-between-terraform-configurations/) - Illustrates how to use remote state to share data between Terraform configurations.
- [The Segment AWS Stack](https://segment.com/blog/the-segment-aws-stack/) - Shows the behind the scenes of the infrastructure powered by Terraform that solved [The Million Dollar Engineering Problem](https://segment.com/blog/the-million-dollar-eng-problem/) at [Segment](https://segment.com/).
- [Top 3 Terraform Testing Strategies for Ultra-Reliable Infrastructure-as-Code](https://www.contino.io/insights/top-3-terraform-testing-strategies-for-ultra-reliable-infrastructure-as-code)
- [Two Weeks with Terraform](https://charity.wtf/2016/02/23/two-weeks-with-terraform/) - Some hard-earned experience from using Terraform in the wild, and some operational wisdom.
- [Terraform: Beyond the Basics with AWS](https://aws.amazon.com/blogs/apn/terraform-beyond-the-basics-with-aws/) - Explanation of a demo using Terraform to provision a sample AWS architecture.
- [Terraform cost estimation](https://github.com/antonbabenko/terraform-cost-estimation) - Anonymized, secure, and free Terraform cost estimation based on Terraform plan (0.12+) or Terraform state (any version).
- [How to Debug Terraform Projects: Tutorial](https://spacelift.io/blog/terraform-debug)

## Community Modules

For more Community Modules not listed here please see the [Terraform Module Registry](https://registry.terraform.io/).

- [rancher-terraform-digitalocean](https://github.com/lunagt/rancher-terraform-digitalocean) - Rancher server on digitalocean.
- [segmentio/stack](https://github.com/segmentio/stack) - Configures production infrastructure with AWS, Docker, and ECS.
- [terraform-aws-alb](https://github.com/terraform-aws-modules/terraform-aws-alb) - Creates Application load-balancer on AWS (verified module).
- [terraform-aws-appconfig](https://github.com/clowdhaus/terraform-aws-appconfig) - Creates AWS AppConfig resources on AWS.
- [terraform-aws-atlantis](https://github.com/terraform-aws-modules/terraform-aws-atlantis) - Creates Terraform configurations for running [Atlantis](https://runatlantis.io) on AWS Fargate. Github, Gitlab and BitBucket are supported.
- [terraform-aws-autoscaling](https://github.com/terraform-aws-modules/terraform-aws-autoscaling) - Creates Auto-Scaling Groups and Launch Configurations (verified module).
- [terraform-aws-customer-gateway](https://github.com/terraform-aws-modules/terraform-aws-customer-gateway) - Creates Customer Gateway on AWS.
- [terraform-aws-datadog-forwarders](https://github.com/clowdhaus/terraform-aws-datadog-forwarders) - Creates resources on AWS to forward logs/metrics to Datadog.
- [terraform-aws-dms](https://github.com/clowdhaus/terraform-aws-dms) - Creates AWS DMS (Database Migration Service) resources on AWS.
- [terraform-aws-dynamodb-table](https://github.com/terraform-aws-modules/terraform-aws-dynamodb-table) - Creates DynamoDB table on AWS.
- [terraform-aws-ec2-instance](https://github.com/terraform-aws-modules/terraform-aws-ec2-instance) - Creates EC2 instances on AWS.
- [terraform-aws-ecr](https://github.com/cloudposse/terraform-aws-ecr) - Manages Docker container registries on AWS ECR.
- [terraform-aws-ecs](https://github.com/terraform-aws-modules/terraform-aws-ecs) - Creates AWS ECS resources on AWS.
- [terraform-aws-efs](https://github.com/cloudposse/terraform-aws-efs) - Defines an EFS Filesystem.
- [terraform-aws-eks](https://github.com/terraform-aws-modules/terraform-aws-eks) - Creates Elastic Kubernetes Service on AWS (very popular module).
- [terraform-aws-elb](https://github.com/terraform-aws-modules/terraform-aws-elb) - Creates Elastic load-balancer on AWS (verified module).
- [terraform-aws-eventbridge](https://github.com/terraform-aws-modules/terraform-aws-eventbridge) - Creates EventBridge resources on AWS.
- [terraform-aws-jenkins-ha-agents](https://github.com/neiman-marcus/terraform-aws-jenkins-ha-agents) - EC2 Based Jenkins deployment with HA (spot) agents. Runs on EFS for immutability. Fully customizeable, with sensible defaults.
- [terraform-aws-jenkins](https://github.com/cloudposse/terraform-aws-jenkins) - Build a Docker image with Jenkins, saves it to an ECR repo, and deploys it to Elastic Beanstalk running a Docker stack.
- [terraform-aws-key-pair](https://github.com/cloudposse/terraform-aws-key-pair) - Automatically Generate SSH Key Pairs (Public/Private Keys).
- [terraform-aws-lambda](https://github.com/terraform-aws-modules/terraform-aws-lambda) - Terraform module, which builds dependencies and packages, and also creates AWS Lambda resources in countless combinations.
- [terraform-aws-lambda-auto-package](https://github.com/nozaq/terraform-aws-lambda-auto-package) - A terraform module to define a lambda function which source files are automatically built and packaged for lambda deployment.
- [terraform-aws-managed-service-prometheus](https://github.com/clowdhaus/terraform-aws-managed-service-prometheus) - Creates AWS Managed Service for Prometheus (AMP) resources on AWS.
- [terraform-aws-modules](https://github.com/terraform-aws-modules) - Collection of Terraform AWS modules supported by the community (includes official AWS modules).
- [terraform-aws-msk-kafka-cluster](https://github.com/clowdhaus/terraform-aws-msk-kafka-cluster) - Creates AWS MSK (Managed Streaming for Kafka) resources on AWS.
- [terraform-aws-notify-slack](https://github.com/terraform-aws-modules/terraform-aws-notify-slack) - Creates SNS topic and Lambda function which sends notifications to Slack.
- [terraform-aws-postgresql-rds](https://github.com/azavea/terraform-aws-postgresql-rds) - Creates PostgreSQL on RDS.
- [terraform-aws-rds](https://github.com/terraform-aws-modules/terraform-aws-rds) - Creates RDS resources on AWS (verified module).
- [terraform-aws-rds-aurora](https://github.com/terraform-aws-modules/terraform-aws-rds-aurora) - Creates RDS Aurora cluster resources on AWS (verified module).
- [terraform-aws-rds-proxy](https://github.com/clowdhaus/terraform-aws-rds-proxy) - Creates AWS RDS Proxy resources on AWS.
- [terraform-aws-redshift](https://github.com/terraform-aws-modules/terraform-aws-redshift) - Creates Redshift resources on AWS.
- [terraform-aws-route53](https://github.com/terraform-aws-modules/terraform-aws-route53) - Creates Route53 resources on AWS.
- [terraform-aws-secure-baseline](https://github.com/nozaq/terraform-aws-secure-baseline) - Set up your AWS account with the secure baseline configuration based on CIS Amazon Web Services Foundations.
- [terraform-aws-security-group](https://github.com/terraform-aws-modules/terraform-aws-security-group) - Creates EC2-VPC security groups on AWS (verified module).
- [terraform-aws-ssh-bastion-service](https://github.com/joshuamkite/terraform-aws-ssh-bastion-service) - Terraform plan to deploy ssh bastion as a stateless service on AWS.
- [terraform-aws-s3-bucket](https://github.com/terraform-aws-modules/terraform-aws-s3-bucket) - Creates S3 bucket resources on AWS.
- [terraform-aws-transit-gateway](https://github.com/terraform-aws-modules/terraform-aws-transit-gateway) - Creates Transit Gateway resources on AWS.
- [terraform-aws-vpc](https://github.com/terraform-aws-modules/terraform-aws-vpc) - Creates VPC resources on AWS (verified and very popular module).
- [terraform-aws-vpn-gateway](https://github.com/terraform-aws-modules/terraform-aws-vpn-gateway) - Creates VPN gateway resources on AWS.
- [terraform-azurerm-aks](https://github.com/kjanshair/terraform-azurerm-aks) - Create AKS resources on Azure.
- [terraform-azurerm-iis](https://github.com/ghostinthewires/terraform-azurerm-iis-install) - Install IIS Server on Azure VM instance.
- [terraform-azurerm-mysql](https://github.com/foreverXZC/terraform-azurerm-mysql) - Create MySql Database on Azure.
- [terraform-azurerm-redis](https://github.com/rahulkhengare/terraform-azurerm-redis) - Create Redis on Azure.
- [terraform-azurerm-sqlserver](https://github.com/metadevpro/terraform-azurerm-sqlserver-seed) - Create SQl Server Database on Azure.
- [terraform-cloudflare-maintenance](https://github.com/adinhodovic/terraform-cloudflare-maintenance) - Module to create a Maintenance Page using Cloudflare Workers.
- [terraform-digitalocean-droplet](https://registry.terraform.io/modules/terraform-digitalocean-modules/droplet/digitalocean) - Terraform module for managing DigitalOcean Droplets and related resources.
- [terraform-ecs-jenkins](https://github.com/shuaibiyy/terraform-ecs-jenkins) - Provisions Jenkins on AWS ECS using Terraform.
- [terraform-google-project-factory](https://github.com/terraform-google-modules/terraform-google-project-factory) - Opinionated Google Cloud Platform project creation and configuration with Shared VPC, IAM, APIs, etc.
- [terraform-linode-k8s](https://registry.terraform.io/modules/linode/k8s/linode/) - Installs Kubernetes on Linode Instances.
- [terraform-static-website-s3-cloudfront](https://github.com/sjevs/terraform-static-website-s3-cloudfront) - Creates static websites on AWS S3 & Cloudfront based on variables.
- [tf_aws_bastion_s3_keys](https://github.com/terraform-community-modules/tf_aws_bastion_s3_keys) - Creates bastion hosts on AWS EC2.

## Private Module Registries

- [anthology](https://github.com/erikvanbrakel/anthology) - Private Terraform registry implementation as an alternative to the official registry.
- [citizen](https://github.com/outsideris/citizen) - Private Terraform Module Registry
- [modulehub](https://www.modulehub.io) - Private Terraform Module Registry and State backend.
- [terraform-simple-registry](https://github.com/apparentlymart/terraform-simple-registry) - Simple implementation of the Terraform registry protocols.
- [terraform-registry](https://github.com/philips-labs/terraform-registry) - Serve terraform provider registry backed by GitHub releases.
- [terrareg](https://github.com/matthewjohn/terrareg) - Private Terraform module registry with UI and git-backed indexing/import

## Private Provider Registries

- [terustry](https://github.com/veepee-oss/terustry) - Open Source terraform provider registry acting as a proxy for gitlab or github releases.

## Providers

### Hashicorp supported providers

- [terraform-provider-aws](https://github.com/hashicorp/terraform-provider-aws) - Provider for Amazon Web Services.
- [terraform-provider-azurerm](https://github.com/hashicorp/terraform-provider-azurerm) - Provider for Azure.
- [terraform-provider-docker](https://github.com/hashicorp/terraform-provider-docker) - Provider for Docker.
- [terraform-provider-google](https://github.com/hashicorp/terraform-provider-google) - Provider for Google Cloud Platform.
- [terraform-provider-helm](https://github.com/hashicorp/terraform-provider-helm) - Provider for Helm.
- [terraform-provider-kubernetes](https://github.com/hashicorp/terraform-provider-kubernetes) - Provider for Kubernetes.
- [terraform-provider-vsphere](https://github.com/hashicorp/terraform-provider-vsphere) - Provider for VMware vSphere.

### Vendor supported providers

- [terraform-provider-alicloud](https://github.com/aliyun/terraform-provider-alicloud) - Provider for Alibaba Cloud.
- [terraform-provider-atlas](https://github.com/ariga/terraform-provider-atlas) - Provider for [Atlas](https://atlasgo.io/).
- [terraform-provider-azuredevops](https://github.com/mikaelkrief/terraform-provider-azuredevops) - Provider for Azure DevOps (VSTS).
- [terraform-provider-buildkite](https://github.com/buildkite/terraform-provider-buildkite) - Provider for Buildkite.
- [terraform-provider-checkly](https://github.com/checkly/terraform-provider-checkly) - Manage [Checkly](https://www.checklyhq.com) resources for API & E2E monitoring.
- [terraform-provider-confluent](https://github.com/confluentinc/terraform-provider-confluent) - Provider for Confluent.
- [terraform-provider-datadog](https://github.com/DataDog/terraform-provider-datadog) - Provider for Datadog.
- [terraform-provider-digitalocean](https://github.com/digitalocean/terraform-provider-digitalocean) - Provider for DigitalOcean.
- [terraform-provider-dominos](https://github.com/ndmckinley/terraform-provider-dominos) - Provider for Dominos Pizza.
- [terraform-provider-env0](https://github.com/env0/terraform-provider-env0) - Provider for [env0](https://www.env0.com/)
- [terraform-provider-github](https://github.com/integrations/terraform-provider-github) - Provider for GitHub.
- [terraform-provider-gitlab](https://github.com/gitlabhq/terraform-provider-gitlab) - Provider for GitLab.
- [terraform-provider-graphql](https://github.com/sullivtr/terraform-provider-graphql) - Provider for GraphQL queries and mutations.
- [terraform-provider-hcloud](https://github.com/hetznercloud/terraform-provider-hcloud) - Provider for Hetzner Cloud.
- [terraform-provider-healthchecksio](https://github.com/kristofferahl/terraform-provider-healthchecksio) - Provider to manage healthchecks.io resources.
- [terraform-provider-heroku](https://github.com/heroku/terraform-provider-heroku) - Provider for Heroku.
- [terraform-provider-ibm](https://github.com/IBM-Cloud/terraform-provider-ibm) - Provider for IBM Cloud.
- [terraform-provider-k8s](https://github.com/banzaicloud/terraform-provider-k8s) - Simple Kubernetes Provider, works with any manifest.
- [terraform-provider-keycloak](https://github.com/mrparkers/terraform-provider-keycloak) - Provider to manage the settings of your [Keycloak](https://www.keycloak.org/) identity provider server.
- [terraform-provider-linode](https://github.com/btobolaski/terraform-provider-linode) - Provider for Linode.
- [terraform-provider-openstack](https://github.com/terraform-provider-openstack/terraform-provider-openstack) - Plugin for OpenStack.
- [terraform-provider-panos](https://github.com/PaloAltoNetworks/terraform-provider-panos) - Provider for [Palo Alto Networks next-generation firewalls](https://www.paloaltonetworks.com/network-security).
- [terraform-provider-pingdom](https://github.com/russellcardullo/terraform-provider-pingdom) - Provider to manage Pingdom resources.
- [terraform-provider-rancher2](https://github.com/rancher/terraform-provider-rancher2) - Provider for Rancher v2.
- [terraform-provider-scalr](https://github.com/Scalr/terraform-provider-scalr) - Provider for [Scalr](https://scalr.com)
- [terraform-provider-secrethub](https://github.com/secrethub/terraform-provider-secrethub) - Provider for SecretHub.
- [terraform-provider-sigsci](https://github.com/signalsciences/terraform-provider-sigsci) - Provider for Signal Sciences.
- [terraform-provider-snowflake](https://github.com/chanzuckerberg/terraform-provider-snowflake) - Provider for Snowflake data warehouse.
- [terraform-provider-spinnaker](https://github.com/armory-io/terraform-provider-spinnaker) - Provider for [Spinnaker](https://www.spinnaker.io/).
- [terraform-provider-spotinst](https://github.com/spotinst/terraform-provider-spotinst) - Provider for spotinst.
- [terraform-provider-stripe](https://github.com/franckverrot/terraform-provider-stripe) - Provider for Stripe.
- [terraform-provider-ucloud](https://github.com/ucloud/terraform-provider-ucloud) - Provider to manage UCloud resources.
- [terraform-provider-uptimerobot](https://github.com/louy/terraform-provider-uptimerobot) - Provider to manage uptimerobot resources.
- [terraform-provider-vaulted](https://github.com/sumup-oss/terraform-provider-vaulted) - Encrypted HashiCorp Vault secrets via Terraform that can be stored in SCM such as Git.
- [terraform-provider-iterative](https://github.com/iterative/terraform-provider-iterative) - Terraform plugin built with machine learning in mind.

## Testing

- [kitchen-terraform](https://github.com/newcontext-oss/kitchen-terraform) - Provides a set of Test Kitchen plugins which enable a system to use Test Kitchen to converge a Terraform configuration and verify the resulting Terraform state with InSpec controls.
- [rspec-terraform](https://github.com/bsnape/rspec-terraform) - RSpec tests for your Terraform modules.
- [terraform-compliance](https://github.com/terraform-compliance/cli) - BDD Testing for Terraform Files.
- [terraform_validate](https://github.com/elmundio87/terraform_validate) - Assists in the enforcement of user-defined standards in Terraform.
- [terratest](https://github.com/gruntwork-io/terratest) - Terratest is a Go library that makes it easier to write automated tests for your infrastructure code.
- [clarity](https://github.com/xchapter7x/clarity) - A declarative test framework for Terraform for unit testing.

## Tools

- [AirIAM](https://github.com/bridgecrewio/AirIAM) - AirIAM is a tool for AWS IAM to least privilege Terraform execution framework.
- [Argonaut](https://argonaut.dev/) - Deploy apps and infrastructure on your cloud in minutes. Autogenerate Terraform modules, customize configurations through PRs. Support for app deployments on Kubernetes and Lambda environments.
- [astro](https://github.com/uber/astro/) - Astro is a tool for managing multiple Terraform executions as a single command. :ghost:
- [atmos](https://github.com/cloudposse/atmos) - A universal tool that converts deep merged YAML to module inputs. :alien:
- [atlantis](https://github.com/runatlantis/atlantis) - Unified workflow for collaborating on Terraform through GitHub.
- [aws2tf](https://github.com/aws-samples/aws2tf) - automates the importing of existing AWS resources into Terraform and outputs the Terraform HCL code.
- [aztfy](https://github.com/Azure/aztfy) - A tool to bring existing Azure resources under Terraform's management.
- [blast radius](https://github.com/28mm/blast-radius) - Interactive visualizations of Terraform dependency graphs. :skull:
- [Checkov](https://github.com/bridgecrewio/checkov/) - Terraform static analysis tool for terraform>=0.12
- [Cloudrail](https://github.com/indeni/cloudrail-demo) - Terraform and Live Cloud context-based analysis tool for terraform>=0.12 :heavy_dollar_sign:
- [Coder](https://coder.com/) - Coder provisions software development environments on your infrastructure via Terraform.
- [driftctl](https://github.com/snyk/driftctl) - Detect, track and alert on infrastructure drift
- [flora](https://github.com/ketchoop/flora) - Terraform version manager.
- [fogg](https://github.com/chanzuckerberg/fogg) - A tool for eliminating toil in managing terraform repositories.
- [former2](https://github.com/iann0036/former2) - Generate terraform configuration from your existing resources within your AWS account.
- [gaia](https://github.com/gaia-app/gaia) - A web application to import and run your Terraform modules.
- [hcldump](https://github.com/magodo/hcldump) - Dump the HCL (v2) abstract syntax tree.
- [hcledit](https://github.com/minamijoyo/hcledit) - A command line editor for HCL.
- [hclgrep](https://github.com/magodo/hclgrep) - Syntax based grep for HCL(v2).
- [iam-policy-json-to-terraform](https://github.com/flosell/iam-policy-json-to-terraform) - Small tool to convert an IAM Policy in JSON format into a Terraform aws_iam_policy_document
- [k2tf](https://github.com/sl1pm4t/k2tf) - Kubernetes YAML to Terraform HCL converter.
- [KICS](https://github.com/Checkmarx/kics) - Scans IaC projects for security vulnerabilities, compliance issues, and infrastructure misconfiguration. Currently working with Terraform projects, Kubernetes manifests, Dockerfiles, AWS CloudFormation Templates, and Ansible playbooks.
- [Infracost](https://github.com/infracost/infracost) - Cloud cost estimates for Terraform in your CLI and pull requests.
- [inframap](https://github.com/cycloidio/inframap) - Read your tfstate or HCL to generate a graph specific for each provider, showing only the resources that are most important/relevant.
- [json2hcl](https://github.com/kvz/json2hcl) - Convert JSON to HCL and vice versa. :ghost:
- [modules.tf-lambda](https://github.com/antonbabenko/modules.tf-lambda) - Infrastructure as code generator from visual diagrams created with [Cloudcraft.co](https://cloudcraft.co/app) to Terraform.
- [para](https://github.com/paraterraform/para) - The missing 3rd-party plugin manager and a "swiss army knife" for Terraform/Terragrunt - just 1 tool to facilitate all workflows. :skull:
- [pluralith](https://www.pluralith.com/) - Terraform state visualization and automated generation of infrastructure documentation. :heavy_dollar_sign:
- [pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) - pre-commit git hooks to take care of Terraform configurations (auto-format, validate, update docs).
- [pike](https://github.com/jamesWoolfenden/pike) - Pike calculates the permissions or IAM policy required to build your Terraform.
- [pretf](https://github.com/raymondbutcher/pretf) - drop-in Terraform wrapper that generates Terraform configuration with Python. See [pretf documentation](https://pretf.readthedocs.io/en/latest/)
- [python-terrafile](https://github.com/claranet/python-terrafile) - Systematically manage external modules from Github for use in Terraform.
- [prettyplan](https://github.com/chrislewisdev/prettyplan) - Prettyplan ([available online here](https://chrislewisdev.github.io/prettyplan/)) is a small tool to help you view large Terraform plans with ease. :ghost:
- [regula](https://github.com/fugue/regula) - Evaluates Terraform infrastructure-as-code for potential AWS, Azure, and Google Cloud security misconfigurations and compliance violations prior to deployment.
- [rover](https://github.com/im2nguyen/rover) - Interactive Terraform state and configuration explorer.
- [ruby-terraform](https://github.com/infrablocks/ruby_terraform) - Simple Ruby wrapper for invoking terraform commands.
- [scenery](https://github.com/dmlittle/scenery) - Another Terraform plan output prettifier. :ghost:
- [scratchrelaxtv](https://github.com/YakDriver/scratchrelaxtv) - Simple Python tool to help with module development - extract vars from `main.tf` to generate `variables.tf` and make module usage stub from `variables.tf`.
- [serverless.tf - Doing serverless with Terraform](https://serverless.tf/) - serverless.tf is an opinionated open-source framework for developing, building, deploying, and securing serverless applications and infrastructures on AWS using Terraform. [Read more](https://github.com/antonbabenko/serverless.tf).
- [Shisho](https://github.com/flatt-security/shisho) - Lightweight static analyzer for Terraform.
- [Styra Declarative Authorization Service (DAS)](https://www.styra.com/terraform-cloud-config-management-with-styra-das-and-open-policy-agent) - Provides a managed [Open Policy Agent (OPA)](https://www.openpolicyagent.org) platform for Application and Infrastructure use cases, including Terraform, Terraform Cloud, and Kubernetes. Enforce policy guardrails during development, in CI/CD pipelines, and at deploy time. Styra DAS Free provides multiple systems and users, policy impact analysis, decision logging and replay, and access to Styra's Terraform policy library.
- [tads-boilerplate](https://github.com/Thomvaill/tads-boilerplate) - The power of Ansible and Terraform + the simplicity of Docker Swarm = Infrastructure as Code and DevOps best practices.
- [tau](https://github.com/avinor/tau) - Tau is a thin wrapper on top of terraform to manage multiple deployments, dependencies and secrets.
- [terraboard](https://github.com/camptocamp/terraboard) - Web dashboard to inspect Terraform States.
- [terraboot](https://github.com/MastodonC/terraboot) - DSL to generate a terraform configuration and run it.
- [terracognita](https://github.com/cycloidio/terracognita) - Reads from existing Cloud Providers (reverse Terraform) and generates your infrastructure as code on Terraform configuration.
- [terracost](https://github.com/cycloidio/terracost) - Cloud cost estimation for Terraform in your CLI.
- [TerraDepot](https://github.com/derBroBro/TerraDepot) Terraform state repository, based on the default http remote backend. Allows the central administration of tfstates on AWS S3.
- [terradozer](https://github.com/jckuester/terradozer) - Terraform destroy without configuration files.
- [terrafile](https://github.com/coretech/terrafile) - Systematically manage external modules from Github for use in Terraform (written in Go).
- [terrafile](https://github.com/dxw/terrafile) - Systematically manage external modules from Github for use in Terraform (written in Ruby).
- [terraform-bundle](https://github.com/hashicorp/terraform/tree/master/tools/terraform-bundle) - Easily builds bundles containing a Terraform binary as well as provider binaries. Useful for CI and air-gapped Terraform Enterprise.
- [terraform-cdk](https://github.com/hashicorp/terraform-cdk) - CDK (Cloud Development Kit) for Terraform allows developers to use familiar programming languages to define cloud infrastructure and provision it through HashiCorp Terraform.
- [terraform-credentials-vault](https://github.com/oulman/terraform-credentials-vault) - A Terraform "credentials helper" plugin that allows providing credentials for Terraform-native services (private module registries, Terraform Cloud, etc) via environment variables.
- [terraform-docs](https://github.com/terraform-docs/terraform-docs) - Quick utility to generate docs from terraform modules.
- [terraform-graph-beautifier](https://github.com/pcasteran/terraform-graph-beautifier) - Command line tool allowing to convert the barely usable output of the terraform graph command to something more meaningful and explanatory.
- [terraform-landscape](https://github.com/coinbase/terraform-landscape) - *(only 0.11 and earlier)* Improve Terraform's plan output to be easier to read and understand.
- [terraform-operator](https://github.com/isaaguilar/terraform-operator.git) - A Kubernetes CRD to handle Terraform operations.
- [terraform-plan-parser](https://github.com/lifeomic/terraform-plan-parser) - Command line utility and JavaScript API for parsing stdout from `terraform plan` and converting it to JSON. :ghost:
- [terraform-provisioner](https://github.com/shuaibiyy/terraform-provisioner) - Tool for managing multiple provisions of the same Terraform scripts.
- [terraform-rake-tasks](https://github.com/gina-alaska/terraform-rake-tasks) - Shared Rake tasks for managing terraform plans.

- [terraform.py](https://github.com/ciscocloud/terraform.py) - Ansible dynamic inventory script for parsing Terraform state files.
- [terraformer](https://github.com/GoogleCloudPlatform/terraformer) - CLI tool to generate terraform files from existing infrastructure. Infrastructure to Code. Supported many providers.
- [terraforming](https://github.com/dtan4/terraforming) - Export existing AWS resources to Terraform style (tf, tfstate). Similar to `terraformer`.
- [terraformize](https://github.com/naorlivne/terraformize) - Apply\Destroy Terraform modules via a simple REST API endpoint.
- [Terraform-Visual](https://github.com/hieven/terraform-visual) A simple but powerful tool to visualize Terraform plan.
- [terragrunt](https://github.com/gruntwork-io/terragrunt) - Terragrunt is a thin wrapper for Terraform that provides extra tools for keeping your Terraform configurations DRY, working with multiple Terraform modules, and managing remote state.
- [terrahelp](https://github.com/opencredo/terrahelp) - Command line utility aimed at providing supplementary functionality which can sometimes prove useful when working with Terraform.
- [terrahub](https://github.com/TerraHubCorp/terrahub) - TerraHub is terraform automation and orchestration tool. Seamlessly integrated into console.terrahub.io, enterprise friendly GUI to show realtime terraform executions, as well as auditing and reporting capabilities for historical terraform runs. :heavy_dollar_sign:
- [terramate](https://github.com/mineiros-io/terramate) - Tool for managing multiple Terraform stacks that comes with support for change detection and code generation
- [terrascan](https://github.com/accurics/terrascan) - Collection of security and best practice test for static code analysis of terraform templates
- [terraspace](https://terraspace.cloud) - The Terraform Framework
- [terrastate](https://github.com/rohinivsenthil/terrastate) - Visual Studio Code extension to monitor/deploy/destroy Terraform resources in your workspace
- [terratag](https://github.com/env0/terratag) - Terratag is a CLI tool that enables users of Terraform to automatically create and maintain tags across their entire set of AWS, Azure, and GCP resources.
- [tf-init-booster](https://github.com/hayorov/terraform-init-booster) - A Pre-terraform routine that speedups terraform modules download for bulky blueprints.
- [tf-summarize](https://github.com/dineshba/tf-summarize) - A command-line utility to print the summary of the terraform plan
- [tfaction](https://github.com/suzuki-shunsuke/tfaction) - GitHub Actions collection for Opinionated Terraform Workflow
- [tfcmt](https://github.com/suzuki-shunsuke/tfcmt) - CLI to notify the result of plan and apply as Pull Request comment.
- [tfedit](https://github.com/minamijoyo/tfedit) - A refactoring tool for Terraform.
- [tfsec](https://github.com/aquasecurity/tfsec) - Terraform static analysis tool that supports terraform <0.12 & >=0.12 & directly integrates with HCL parser for better results.
- [tfenv](https://github.com/tfutils/tfenv) - Terraform version manager inspired by rbenv.
- [tfjson](https://github.com/palantir/tfjson) - Utility to read in a Terraform plan file and dump it out in JSON. :skull:
- [tflint](https://github.com/terraform-linters/tflint) - Terraform linter for detecting errors that can not be detected by `terraform plan`
- [tfmask](https://github.com/cloudposse/tfmask) - Terraform utility to mask select output from `terraform plan` and `terraform apply`
- [tfmigrate](https://github.com/minamijoyo/tfmigrate) - A Terraform state migration tool for GitOps.
- [tfmigrator](https://github.com/tfmigrator/cli) - Go library and CLI to migrate Terraform Configuration and State
- [tfscaffold](https://github.com/tfutils/tfscaffold) - Framework for controlling multi-environment multi-component terraform-managed AWS infrastructure.
- [tfschema](https://github.com/minamijoyo/tfschema) - Schema inspector for Terraform providers.
- [tfupdate](https://github.com/minamijoyo/tfupdate) - Update version constraints in your Terraform configurations.
- [tfvaultenv](https://github.com/oulman/tfvaultenv) - tfvaultenv reads secrets from HashiCorp Vault and outputs environment variables for various Terraform providers with those secrets.
- [tfwrapper](https://github.com/manheim/tfwrapper) - Rubygem providing rake tasks for running Hashicorp Terraform sanely.
- [tgf](https://github.com/coveo/tgf) - Terragrunt frontend for executing Terragrunt/Terraform through Docker.
- [validIaC](https://github.com/gofireflyio/validiac) - ValidIaC combines the best open-source tools to help ensure Terraform best practices, hygiene & security.
- [xterrafile](https://github.com/devopsmakers/xterrafile) Systematically manage external modules from the module registry, git or local directories for use in Terraform (written in Go).
- [yor](https://github.com/bridgecrewio/yor) - Automatically tag and trace infrastructure as code frameworks (Terraform, Cloudformation and Serverless) .

## Libraries

- [pyhcl](https://github.com/virtuald/pyhcl) - HCL parser in Python
- [python-hcl2](https://github.com/amplify-education/python-hcl2/) - HCL2 parser in Python
- [rhcl](https://github.com/winebarrel/rhcl) - Pure Ruby HCL parser

## Boilerplates

- [Terraform Generator](https://github.com/sudokar/generator-tf-module) - Scaffolding for a new terraform module or project with support of test frameworks (terratest and kitchen-terraform)
- [Terraform GitOps Framework](https://www.kubestack.com) - Everything you need to build reliable automation for AKS, EKS and GKE Kubernetes clusters in one free and open-source framework.

## Terraform Enterprise

- [terraform-enterprise-cli](https://github.com/skierkowski/terraform-enterprise-cli) - Terraform Enterprise Command Line Interface.
- [terraform-enterprise-client](https://github.com/skierkowski/terraform-enterprise-client) - Terraform Enterprise API Ruby Client and Command Line tool.
- [terraform-enterprise-migrator](https://github.com/silinternational/terraform-enterprise-migrator) - Script for migrating Terraform Enterprise environments from Legacy to new version of Terraform Enterprise.
- [tfe-state-explorer](https://github.com/segmentio/tfe-state-explorer) - Simple shell for exploring remote terraform enterprise state, with autocomplete. :skull:
- [Scalr](https://scalr.com) - Alternative to Terraform Enterprise with OPA integration, organizational structure, custom hooks, native integrations with other DevOps platforms, and centralized reporting.  :heavy_dollar_sign:
- [env0](https://env0.com) - Alternative to Terraform Cloud/Enterprise with OPA integration, custom flows and Terragrunt support :heavy_dollar_sign:
- [modulehub](https://www.modulehub.io) - Private Terraform Module Registry and State backend.
- [Brainboard](https://www.brainboard.co) - Visually Design, Deploy & Manage modern cloud infrastructures starting from any Cloud Provider - AWS, GCP, Azure :heavy_dollar_sign:
- [Terrakube](https://terrakube.org) - Open Source alternative to Terraform Enterprise with private registry, remote state, custom flows, scheduled workspaces and visual states.
- [Spacelift](https://spacelift.io/) - Alternative to Terraform Cloud/Enterprise. Collaborative Infrastructure Delivery Platform for Terraform :heavy_dollar_sign:

## Videos

- [Your Weekly Dose of Terraform](https://bit.ly/terraform-youtube) - YouTube channel with weekly live streams covering Terraform news, reviews, interviews, Q&A, live coding, and some hacking with Terraform.
- [Terraform explained in 15 mins](https://www.youtube.com/watch?v=l5k1ai_GBDE) - Terraform explained in 15 mins.
- [Terraform Course](https://www.youtube.com/watch?v=SLB_c_ayRMo) - Automate your AWS cloud infrastructure.
- [How to Build Reusable, Composable, Battle tested Terraform Modules](https://www.youtube.com/watch?v=LVgP63BkhKQ) - Yevgeniy Brikman talks about how to write Terraform code so that it is reusable, composable and testable. The presentation focuses on Terraform modules, but also provides a brief and clear explanation of what problem Terraform was created to solve and a short demo of Terraform basics (~39 min, October 2017).
- [Building Scalable, Repeatable Infrastructure in the Cloud with Terraform](https://www.youtube.com/watch?v=cG7pcksTAnY) - Demonstrates how Terraform enables the practice of Infrastructure as Code by deploying TeamCity in AWS using a hosted PostgreSQL.
- [Creating a Google Compute Instance with Terraform](https://www.youtube.com/watch?v=fo3VX33Zx0c) - Example of creating a Google Compute Instance with Terraform code.
- [Creating a Terraform Provider for Just About Anything](https://www.hashicorp.com/resources/creating-terraform-provider-for-anything) - Learn how to contribute to a Terraform provider or create your own from this walkthrough.
- [Evolving Your Infrastructure with Terraform](https://www.youtube.com/watch?v=wgzgVm7Sqlk) - CTO of OpenCredo provides an extensive look at using Terraform in the real-world with the help of some interesting use-cases.
- [Going Multi-Cloud with Terraform and Nomad](https://www.youtube.com/watch?v=e42A4aBZUkQ).
- [How to Extend the Terraform Provider List](https://www.youtube.com/watch?v=2BvpqmFpchI) - In this talk, Paul will walk through the creation of a terraform provider.
- [Orchestrating Containers with Terraform and Consul](https://www.infoq.com/presentations/terraform-consul) - Mitchell Hashimoto shows how Terraform can be used to deploy and scale containerized workloads.
- [Production ChaosMonkey with Terraform](https://www.youtube.com/watch?v=CPI6W3LK0-g) - How DigitalOcean uses Terraform to run production integration tests.
- [Running a Terraform Environment at Scale](https://www.youtube.com/watch?v=3JVGSq7QIS0) - Running Terraform at scale with hundreds of AWS accounts.
- [Setup Continuous Integration for a Terraform module](https://www.youtube.com/watch?v=vuJ6bjYKUcA) - Example of using CI with Kitchen-Terraform to test, tag and publish our Terraform module which creates a Google Compute Instance.
- [State of Terraform Providerland](https://www.youtube.com/watch?v=ar1PF5iDtbg) - How Terraform providers work and how to write one.
- [Terraform At Scale](https://www.youtube.com/watch?v=RldRDryLiXs) - How Segment uses Terraform.
- [Terraform w/ Lee Trout](https://www.youtube.com/watch?v=p2ESyuqPw1A) - Focuses on development patterns and how to effectively structure Terraform code.
- [Terraforming the Composable World](https://www.youtube.com/watch?v=cHrOXPatFeg) - Integrating Terraform with an on-premise bare metal provisioning.
- [Test and verify a Google Compute Instance with Kitchen-Terraform](https://www.youtube.com/watch?v=kiH3-LEveek) - Example of using Kitchen-Terraform to test our Terraform code that creates a Google Compute.
- [Untangling Terraform Through Refactoring](https://www.youtube.com/watch?v=OH6iDKaXpZs) - How to refactor your Terraform code in a careful way with minimum risk.
- [Complete Terraform Course - From BEGINNER to PRO! (Learn Infrastructure as Code)](https://www.youtube.com/watch?v=7xngnjfIlK4) - Complete course from beginner to pro, with no cloud provider focus, with a general approach

## Editor Plugins

- [Atom terraform-lookup](https://atom.io/packages/terraform-lookup)
- [Emacs terraform-mode](https://github.com/syohex/emacs-terraform-mode)
- [Intellij](https://plugins.jetbrains.com/plugin/7808-hashicorp-terraform--hcl-language-support)
- [Terraform-ls](https://github.com/hashicorp/terraform-ls) (Terraform Language Server)
- [Terraform-lsp](https://github.com/juliosueiras/terraform-lsp) (Language Server Protocol for Terraform)
- [Vim-Terraform](https://github.com/hashivim/vim-terraform)
- [Vim-Terraform-Completion](https://github.com/juliosueiras/vim-terraform-completion)
- [VS Code](https://marketplace.visualstudio.com/items?itemName=mauve.terraform)

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Shuaib Yunus has waived all copyright and related or neighboring rights to this work.
