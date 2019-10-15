# Introduction
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Use Case](#use-case)
- [Available Tools](#available-tools)

<!--TOC_END-->
## Overview
Configuration management is a systems engineering process for establishing and maintaining consistency of a product's performance, functional, and physical attributes with its requirements, design, and operational information throughout its life.

What this this basically means is to configure something, like an application server or multiple servers, maintain that desired configuration and be able to consistenly and reliably update or change that configuration.

Configuration management becomes expecially important on environments/application servers that cannot be deleted.
This is because the servers will be running for months, maybe even years - over this time the disired configuration of theses machines can deviate dramatically, causing unforseen errors when deploying new versions of the applications.

## Use Case
Lets say there is the following application stack:
- 3 Front end web servers
- 2 Backend API servers
- 1 Database Server

When we start to consider the tasks shown below, its easy to see why we would benefit from tools that can automate the configuration of servers:
- Creating and configuring a new environment for the application
    - To manually configure multiple servers consistently would be very hard and error prone
- Deploying a new version of the application
    - Reliably changing configurations and reinstalling applications will cause extra time needed to make deployments and downtime

## Available Tools
So we find ourselves needing a way of managing configurations for multiple hosts and environments, fortunately there are several tools that are very compentent at this:
- Ansible
- Puppet
- Chef
