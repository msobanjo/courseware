# Configuration File Discovery

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Loading order](#loading-order)
- [Task](#task)
	- [AWS task](#aws-task)
		- [Prerequisites](#prerequisites)
		- [Authenticating](#authenticating)
		- [Creating the directory and configuration file](#creating-the-directory-and-configuration-file)
		- [Adding the provider](#adding-the-provider)
		- [Adding resource](#adding-resource)
		- [Adding variables](#adding-variables)
		- [Formatting](#formatting)
	- [Final configuration file states](#final-configuration-file-states)
	- [Running the configuration file](#running-the-configuration-file)
	- [Overview](#overview-1)
		- [Clean up](#clean-up)

<!--TOC_END-->
## Overview

There is a specific order in how your configuration files are discovered by TF. 

When you run a Terraform command, it will inspect the current directory for files ending with *.tf* to discover any configuration files written in HCL.

If you are using *JSON*, the file extension should be *.tf.json* 

Terraform can read in a mixture of HCL and JSON configuration files. 

You, the implementer, decide on whether you will use one *.tf* file or more. 

It's common for bigger projects to use more than one configuration file.

For example, *variables*, *outputs*, and *main resource configuration* are commonly split into three files.

## Loading order

The configuration files are loaded in alphabetical order. 

The loaded files are essentially appended. 

This means that if you have two resources with the same name Terraform will throw an error instead of using the last declared resource with the name. 

Beyond splitting your configuration across multiple files, there is another feature available to you for organizing your configurations which is modules.

## Task

### AWS task

<details>

<summary>Deploying an AWS resource with multiple configuration files</summary>

#### Prerequisites

1. Have **aws cli** installed
    2. You can install it by running the following python command, keep in mind you need to have python installed:
    `pip install awscli`
3. Know your AWS `access` and `secret` keys

#### Authenticating

First let's authenticate with aws so that terraform could execute the configuration file, run the following command:
`aws configure`
You will be asked to provide the following things:
* **AWS Access Key ID** this is where you would need to provide your *access* key
* **AWS Secret Access Key ID** this is the *secret* key
* **Default region name** would be **eu-west-2**
You might get asked additionally to specify what formatting you want to use, enter **json**.

#### Creating the directory and configuration file

For the next step create a new folder, you can pick any name for it but a suggested one would be `configuration_file_discovery`.

Within the newly created folder, create a new file called `main.tf`.

#### Adding the provider

Now paste the following contents into the `main.tf` file:
```hcl
provider "aws" {
	region = "eu-west-2"
}
``` 
You may have noticed that there is only the region declared and no `access_key` or `secret_key` declared, this is done on purpose. 

We're doing it in this way so that when you will be uploading these configuration files to GitHub you wouldn't accidentally expose them.

#### Adding resource

Paste the following below the variable in the `main.tf` file:
```hcl
resource "aws_instance" "example" {
	ami = var.ami
	instance_type = var.type
}
```

In this resource block we're specifying what amazon machine image to use for the operating system, it's value is held by **ami** argument where the value is received by making a reference to **var**, it allows us to get a specific variables value by referring to it's name. 

In this case when we want to use the value of the **ami** variable we need to make a reference to it like this: `var.ami`.

The second argument is **instance_type** which specifies which machine configuration to use, it will determine how many vCPU's will be assigned as well as the amount of RAM. 

Similarly in order to get the value of the variable we need to make a reference to it like this: `var.type`.

#### Adding variables

Create a new file called `variables.tf` in the `example_3` directory.

Paste the following into the `variables.tf` file:

```hcl
variable "ami" {
  description = "machine image"
  default     = "ami-f976839e"
}

variable "type" {
  default = "t2.micro"
}
```

#### Formatting

Format the configuration files by running the command:
```bash
terraform fmt
```

### Final configuration file states

Let's check that you have configuration files ready.

`main.tf` configuration file should look like this:

```hcl
provider "aws" {
  region     = "eu-west-2"
}

resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.type
}
```

`variables.tf` configuration file should look like this:

```hcl
variable "ami" {
  description = "machine image"
  default     = "ami-f976839e"
}

variable "type" {
  default = "t2.micro"
}
```

If the configuration files are like this, continue with the task. 

If the configuration files you have are different, update them to match them.

### Running the configuration file

Next, open a the terminal in the directory where the configuration files are.

First let's execute the following command to get the plugins for AWS:

`terraform init`

Next let's execute to see what changes will be made:

`terraform plan`

Lastly let's create the resource by executing:

`terraform apply`

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

### Overview

In this task you used two configuration files to deploy a resource in AWS.

You may have noticed that there was no need in making a reference to the variables configuration file in order to get the variables value.

This is because terraform appends configuration files and the variables would end up in the same scope.

#### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
`terraform destroy` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

</details>
