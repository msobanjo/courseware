# ELastic Beanstalk Introducion
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [CLI Commands](#cli-commands)
- [Applications](#applications)
	- [Creating Applications](#creating-applications)

<!--TOC_END-->
## Overview
Elastic Beanstalk (EB) on AWS is Platform as a Service (PaaS) solution for deploying web applications and workloads.
EB can be used with little knowledge of infrastructure, allowing you to focus more on development.

EB has the potential to be used as a quick way to provision a test environment or be used for production solutions with the ability to create different versions to deploy and roll back versions of deployments.

Applications developed with any of the following are supported:
- Java
- .NET
- Nodejs
- Python
- PHP
- Ruby
- Go
- Docker
Common web servers can be also configure in EB:
- Apache
- Nginx
- Passenger
- IIS

## CLI Commands
EB can be easily used through the AWS console; a guided setup is provided.
Using the CLI will allow you gain a better understanding of how the different EB components work and the necessary configurations that you need to make.

## Applications
An application is the highest level of configurtation for EB.
You may have more than one application in EB if you would like to.
### Creating Applications
You will need to have a name for your application that isn't the same as any another applications in your EB, you may also provide a description for you application.

```bash
# aws elasticbeanstalk create-application --application-name [APPLICATION_NAME] --description [DESCRIPTION]
aws elasticbeanstalk create-application --application-name my-first-application --description "My first EB Application"
```

More options for the `create-application` command can be found [here](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/create-application.html)
