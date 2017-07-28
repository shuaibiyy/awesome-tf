# Awesome Terraform [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of resources on [HashiCorp's Terraform](https://www.terraform.io/).
[<img src="https://rawgit.com/shuaibiyy/awesome-terraform/master/terraform.svg" align="right" width="100">](https://terraform.io)
Your [contributions](https://github.com/shuaibiyy/awesome-terraform/blob/master/contributing.md) are welcome!

## Contents

- [Official Resources](#official-resources)
- [Books](#books)
- [Tutorials and Blog Posts](#tutorials-and-blog-posts)
- [Community Modules](#community-modules)
- [Tools](#tools)
- [Podcasts](#talks-and-podcasts)
- [Community](#community)

## Official Resources

* [Introduction to Terraform](https://www.terraform.io/intro/)
* [Terraform Documentation](https://www.terraform.io/docs/)

## Community

* [Terraform Google Group](https://groups.google.com/forum/#!forum/terraform-tool)
* [Terraform Gitter](https://gitter.im/hashicorp-terraform)
* [Terraform Bug Tracker](https://github.com/hashicorp/terraform/issues)
* [Terraform Community Modules](https://github.com/terraform-community-modules)

## Books

* [Terraform: Up & Running](http://www.terraformupandrunning.com/?ref=gruntwork-blog-comprehensive-terraform)
* [The Terraform Book](https://terraformbook.com/)
* [Getting Started with Terraform](https://www.amazon.com/Getting-Started-Terraform-Kirill-Shirinkin/dp/1786465108/)

## Tutorials and Blog Posts

* [A Comprehensive Guide to Terraform](https://blog.gruntwork.io/a-comprehensive-guide-to-terraform-b3d32832baca#.w9x897ywp)
* [Easily Deploy A Seneca Microservice to ECS with Wercker and Terraform: Part I-III](http://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-i/)
* [Tutorial: How to Use Terraform to Deploy OpenStack Workloads](http://www.stratoscale.com/blog/openstack/tutorial-how-to-use-terraform-to-deploy-openstack-workloads/)
* [Write your own Terraform provider: Part 1](http://container-solutions.com/write-terraform-provider-part-1/)
* [The Segment AWS Stack](https://segment.com/blog/the-segment-aws-stack/)
* [Terraform: Beyond the Basics with AWS](https://aws.amazon.com/blogs/apn/terraform-beyond-the-basics-with-aws/)
* [Deploying Discourse with Terraform](https://www.hashicorp.com/blog/terraform-discourse.html)
* [How we deploy from Slack using Jenkins, Terraform, Docker and Ansible](https://medium.com/@levinotik/how-we-deploy-from-slack-using-jenkins-terraform-docker-and-ansible-4196b6856cdf)
* [Bootstrapping Docker Infrastructure With Terraform](http://vilkeliskis.com/blog/2016/02/10/bootstrapping-docker-with-terraform.html)
* [Two Weeks with Terraform](https://charity.wtf/2016/02/23/two-weeks-with-terraform/)
* [Using modules in Terraform](http://www.avitzurel.com/blog/2016/01/05/using-modules-in-terraform/)
* [Terraform Modules for Fun and Profit](http://blog.lusis.org/blog/2015/10/12/terraform-modules-for-fun-and-profit/)
* [Using Terraform for Cloud Deployments - Part 1](https://dev.to/koenighotze/using-terraform-for-cloud-deployments---part-1)
* [Terraform, VPC, and why you want a tfstate file per env](https://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/)
* [Sharing data between Terraform configurations](https://jamesmckay.net/2016/09/sharing-data-between-terraform-configurations/)


## Community Modules

* [segmentio/stack](https://github.com/segmentio/stack) - A set of Terraform modules for configuring production infrastructure with AWS, Docker, and ECS.
* [terraform-ecs-jenkins](https://github.com/shuaibiyy/terraform-ecs-jenkins) - Provisions Jenkins on AWS ECS using Terraform.
* [tf_aws_bastion_s3_keys](https://github.com/terraform-community-modules/tf_aws_bastion_s3_keys) - A Terraform module for creating bastion host on AWS EC2.
* [terraform-static-website-s3-cloudfront](https://github.com/sjevs/terraform-static-website-s3-cloudfront) - Terraform template to create static website on AWS S3 & Cloudfront based on variables.
* [tf_aws_vpc_only](https://github.com/terraform-community-modules/tf_aws_vpc_only) - A Terraform module to provide only VPC (without subnets) in AWS.
* [tf_aws_asg_elb](https://github.com/terraform-community-modules/tf_aws_asg_elb) - A Terraform Module for creating an Auto-Scaling Group and Launch Configuration for use with an Elastic Load Balancer.
* [tf_aws_availability_zones_cfn](https://github.com/terraform-community-modules/tf_aws_availability_zones_cfn) - Get availability zones for your AWS region/account from Cloudformation.
* [tf_aws_ubuntu_ami](https://github.com/terraform-community-modules/tf_aws_ubuntu_ami) - Easy way to lookup Ubuntu AMIs with Terraform.
* [tf_aws_sg](https://github.com/terraform-community-modules/tf_aws_sg) - A Terraform module with a collection of common security group settings.
* [tf_aws_coreos_ami](https://github.com/terraform-community-modules/tf_aws_coreos_ami) - An easy way to lookup CoreOS AMIs with terraform.
* [tf_aws_private_subnet_nat_gateway](https://github.com/terraform-community-modules/tf_aws_private_subnet_nat_gateway) - A Terraform module to create private subnets with NAT Gateway in AWS.
* [tf_aws_rds](https://github.com/terraform-community-modules/tf_aws_rds) - A Terraform Template for RDS.
* [tf_aws_vpc](https://github.com/terraform-community-modules/tf_aws_vpc) - A terraform module to provide a VPC in AWS.
* [tf_aws_availability_zones](https://github.com/terraform-community-modules/tf_aws_availability_zones) - Lists of AZs your account has access to.
* [tf_aws_virttype](https://github.com/terraform-community-modules/tf_aws_virttype) - Lookup the virtualization types (hvm or pv) supported for AWS instance types.
* [tf_aws_nat](https://github.com/terraform-community-modules/tf_aws_nat) - NAT instances for AWS.
* [rancher-terraform-digitalocean](https://github.com/lunagt/rancher-terraform-digitalocean) - Terraform module for a rancher server on digitalocean.

## Tools

* [terraform-docs](https://github.com/segmentio/terraform-docs) - A quick utility to generate docs from terraform modules.
* [terraform.py](https://github.com/ciscocloud/terraform.py) - Ansible dynamic inventory script for parsing Terraform state files.
* [terraform-provisioner](https://github.com/shuaibiyy/terraform-provisioner) - A tool for managing multiple provisions of the same Terraform scripts.
* [terraboot](https://github.com/MastodonC/terraboot) - DSL to generate a terraform configuration and run it.
* [terraform-provider-pingdom](https://github.com/russellcardullo/terraform-provider-pingdom) - Terraform provider to manage pingdom resources.
* [terragrunt](https://github.com/gruntwork-io/terragrunt) - Terragrunt is a thin wrapper for Terraform that supports locking for Terraform state and enforces best practices.
* [terraform-import-as-hcl](https://gitlab.com/nowaker/terraform-import-as-hcl) - This script imports a Terraform resource into `.tfstate` AND creates an HCL resource definition in `.tf` file.

## Talks and Podcasts

* [Orchestrating Containers with Terraform and Consul](https://www.infoq.com/presentations/terraform-consul)
* [Automating Infrastructure at HashiCorp with Mitchell Hashimoto](http://softwareengineeringdaily.com/2016/04/05/automating-infrastructure-hashicorp/)
* [Building Scalable, Repeatable Infrastructure in the Cloud with Terraform](https://www.youtube.com/watch?v=cG7pcksTAnY)
* [Evolving Your Infrastructure with Terraform](https://www.youtube.com/watch?v=wgzgVm7Sqlk)
* [Going Multi-Cloud with Terraform and Nomad](https://www.youtube.com/watch?v=e42A4aBZUkQ)
* [Running a Terraform Environment at Scale](https://www.youtube.com/watch?v=3JVGSq7QIS0)
* [Terraforming the Composable World](https://www.youtube.com/watch?v=cHrOXPatFeg)
* [State of Terraform Providerland](https://www.youtube.com/watch?v=ar1PF5iDtbg)
* [Untangling Terraform Through Refactoring](https://www.youtube.com/watch?v=OH6iDKaXpZs)
* [Terraform Modules and Continuous Deployments](https://www.youtube.com/watch?v=tEvtgaoFAIs)
* [Terraform At Scale](https://www.youtube.com/watch?v=RldRDryLiXs)
* [Production ChaosMonkey with Terraform](https://www.youtube.com/watch?v=CPI6W3LK0-g)
* [Templating your Terraform](https://www.youtube.com/watch?v=83G_7y5RIts)
* [Terraform w/ Lee Trout](https://www.youtube.com/watch?v=p2ESyuqPw1A)
* [Using Terraform to Build a Hybrid Cloud](https://www.youtube.com/watch?v=adzqsywrJKk)

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Shuaib Yunus has waived all copyright and related or neighboring rights to this work.
