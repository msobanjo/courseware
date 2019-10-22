# Introduction

### Overview

Terraform allows you to control your infrastructure on the cloud service provider the big providers like: AWS, GCP, Azure are supported. 
Your infrastructure can be described as code, allowing you to have a blueprint of your datacenter that can be versioned like any other piece of code.

### Infrastructure as Code

Infrastructure as code means that we can use a high level or descriptive programming language to describe and manage infrastructure. 
There is a known issues with pipelines and that is environment drift, which means over time, an environment can end up in unique configuration that cannot be automatically recreated. 
When environments become inconsistent, deployments can be affected and testing can be made invalid. 
With infrastructure as code, the infrastructure configurations can be versioned and maintained, so if another environment needs to be created, you can be sure that you are using up to date configurations.

### Common use cases