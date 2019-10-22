# Introduction

### Overview

Terraform allows you to control your infrastructure on the cloud service provider the big providers like: AWS, GCP, Azure are supported. 
Your infrastructure can be described as code, allowing you to have a blueprint of your data-center that can be versioned like any other piece of code.

### Infrastructure as Code

Infrastructure as code means that we can use a high level or descriptive programming language to describe and manage infrastructure. 
There is a known issues with pipelines and that is environment drift, which means over time, an environment can end up in unique configuration that cannot be automatically recreated. 
When environments become inconsistent, deployments can be affected and testing can be made invalid. 
With infrastructure as code, the infrastructure configurations can be versioned and maintained, so if another environment needs to be created, you can be sure that you are using up to date configurations.

### Common use cases

* **Multi-Tier Applications** - It is very common to have applications with multiple tiers, each tier having different requirements and dependencies. 
With Terraform we are able to describe each tier of the application as a collection of resources so that the dependencies for each tier can be handled automatically.
* **Software Demos** - Although tools like Vagrant can be used to create environments for demos, vagrant can’t completely mimic production environments additionally depending on how large the infrastructure for the application is, it might be a challenging to run it on a laptop.
 Because configurations for vagrant can be distributed, demos can be run against the end user’s infrastructure with ease. 
 Parameters for the Terraform configurations can also be tweaked so that the software can be demoed at any scale.
* **Disposable Environments** - It is common to have a staging environment before deploying to production, which is a smaller clone of the production environment. 
Production environments over time can become more complex and require more effort to mimic on a smaller scale. 
With Terraform, the infrastructure will be kept as code and can easily applied to other new environments for testing and then be disposed. 
Spinning up and disposing environments this easily means that costs can also saved on environments that do not need to be operational 24/7 and only for a fraction of that time.
* **Multi-Cloud Deployments** - Terraform has the ability to configure infrastructure across more than one cloud service.
 This hybrid solution might be due to a customer wanting to take advantage of the features available on different cloud provider solutions. 
Another reason for multi-cloud deployments could be for extra fault tolerance.

### Tasks

We will now install terraform and check that the installation was successful.

### Windows

1. Navigate to https://www.terraform.io/downloads.html in a web browser and download Terraform for 64-bit windows
2. Extract the .zip file
3. Copy the terraform.exe file from where you decided to extract it to a new folder: `C:\tools\terraform\`
4. We now need to configure the PATH environment variable so that Terraform can be used easily on the command line.
    5. Press **Windows key + R** to open the **Run program**
    6. Type **SystemPropertiesAdvanced** and click **OK**
    <img align="left" src="https://imgur.com/6y4t3MX.jpg">
    7. Select **Environment Variables** button
    <img align="left" src="https://imgur.com/XihMpT9.jpg">
    8. Under *User Variables* for <your-username>, select **New…** and enter the Variable name: **TERRAFORM_HOME** and the Variable value: `C:\tools\terraform`, then click **OK** button
    <img align="left" src="https://imgur.com/EaIt6Jv.jpg">
    9. Under *User Variables* for <your-username>, select the variable called **Path** then click **Edit…** then enter **%TERRAFORM_HOME%**
    <img align="left" src="https://imgur.com/bkXxBsK.jpg">
    10. Click **OK** button on the *Environment Variable Windows* and close the *System Properties* window
    
### Linux

