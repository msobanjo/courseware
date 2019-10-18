<!--PROPS
{
    "prerequisites": [
        "aws/introduction"
    ]
}
-->
# Elastic Beanstalk Introducion
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [CLI Commands](#cli-commands)
- [Applications](#applications)
	- [Create](#create)
	- [Show Existing](#show-existing)
	- [Delete](#delete)
- [Versions](#versions)
	- [Create](#create-1)
		- [Sample Version](#sample-version)
		- [Version Using ZIP or WAR File](#version-using-zip-or-war-file)

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
Understanding the CLI commands will also allow you to script solutions for EB and any other resources in AWS for that matter.

## Applications
An application is the highest level of configurtation for EB.
You may have more than one application in EB if you would like to.
### Create
You will need to have a name for your application that isn't the same as any another applications in your EB, you may also provide a description for you application.

```bash
# aws elasticbeanstalk create-application --application-name [APPLICATION_NAME] --description "[DESCRIPTION]"
aws elasticbeanstalk create-application --application-name my-first-application --description "My first EB Application"
```

More options for the `create-application` command can be found [here](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/create-application.html)

### Show Existing
Existing applications and information about them can be shown by using the `describe-applications` command.
```bash
# aws elasticbeanstalk describe-applications
aws elasticbeanstalk describe-applications
```
If you have a lot of applications then specific applications can be described using the `--application-names` option:
```bash
# aws elasticbeanstalk describe-applications --application-names "[APPLICATION_NAME]" "[APPLICATION_NAME]"
aws elasticbeanstalk describe-applications --application-names "app-1" "app-2"
```

### Delete
The application can be deleted by providing the unique name of it to the `delete-application` command:
```bash
# aws elasticbeanstalk delete-application --application-name [APPLICATION_NAME]
aws elasticbeanstalk delete-application --application-name my-first-application
```

## Versions
The way that deployments can be managed in EB is through versions of your applications.
### Create
There are some required and preffered options to include when creating an application version:
- `--application-name` (required): the name of the application that you are creating a version for
- `--description` (optional): description for the version
- `--source-bundle` (optional): the code to deploy, if ommited, a sample application will be set by AWS. The source bundle can be either from an AWS CodeCommit Git repository or a ZIP or WAR file stored in S3. 
- `--auto-create-application` (optional): if you haven't created an application yet then one will be created if you use this option and the application doesn't exist
#### Sample Version
Here a sample version will be created because a source bundle has not been configured:
```bash
# aws elasticbeanstalk create-application-version --application-name [APPLICATION_NAME] --version-label [VERSION_LABEL]
aws elasticbeanstalk delete-application --application-name my-first-application --version-label v1
```
#### Version Using ZIP or WAR File
The AWS sample applications are good for seeing how EB work however we will of course need to be able to deploy our own code to EB, which can be done using the `--source-bundle` option.
Details on configuring these source bundles can be found in another module.

We will be looking at using a ZIP file for a source bundle in this case which can be retrieved from and S3 bucket.
Note that the S3 bucket that you are using must be in the same region as the EB application.
```bash
# aws elasticbeanstalk create-application-version --application-name [APPLICATION_NAME] --version-label [VERSION_LABEL] --source-bundle S3Bucket="[BUCKET_NAME]",S3Key="[S3_KEY]"
aws elasticbeanstalk delete-application --application-name my-first-application --version-label v1 --source-bundle S3Bucket="my-bucket",S3Key="my-app-v1.zip"
```
