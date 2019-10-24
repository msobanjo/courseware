# Configuration language

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Modules and Resources](#modules-and-resources)
- [Basic syntax](#basic-syntax)
- [Configuration files](#configuration-files)
- [Order of configuration](#order-of-configuration)
- [Comments](#comments)
- [Tasks](#tasks)
	- [Prerequisites](#prerequisites)
	- [Clean up](#clean-up)

<!--TOC_END-->
## Overview
Terraform uses it's own configuration language. 

It's designed to describe infrastructure in a concise way. 

The language is declarative meaning it describes an intended goal rather than the steps of how to reach that goal.

## Modules and Resources

Main purpose of Terraform language is to declare resources. 

Any additional features that the language has are meant to aid the primary purpose. 

A *resource* describes a single object of infrastructure, but multiple resources can be combined into a *module* where relationships between them could be defined.

## Basic syntax

There are three main building blocks to Terraform syntax they are: Arguments, Blocks and Expressions.

**Blocks** - block is like a container that holds the configuration for an object like a resource. 
Blocks have a type. 
Can contain zero or more labels.
Body can contain zero or more arguments or nested blocks.
Majority or Terraform features are controlled from configuration files by top level blocks.

**Arguments** - allows to assign a value to a name. 
They appear within blocks.

**Expressions** - are like variables, their purpose is to represent a value, either literally, referencing or combining with other values. 
Expressions appear like values for arguments as well as within other expressions. 

Now let's take a look at how they would look like in use:
```
<BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK LABEL>" {
  # Block body
  <IDENTIFIER> = <EXPRESSION> # Argument
}

resource "aws_instance" "example" {
	ami = "ami-2757f631"
	instance_type = "t2.micro"
}
```

## Configuration files

Terraform language configuration files uses an extension of `.tf`, an example file name would be `main.tf`. 

Although, that isn't the only supported file extension, there is also the JSON syntax where the files have the extension of `.tf.json`, an example file name would be `main.tf.json`. 
Terraform allows for JSON to be used because it is machine-readable, meaning that Terraform configurations themselves could be automated.

Configuration files need to use the `UTF-8` encoding. 

Even though both windows and unix style line endings are supported you should use the unix style ones. 

This is to make sure that Terraform is reading the configuration file that you made correctly.

Windows line endings are represented as `\r\n` where unix are `\n`.

*Module* is a one or more configuration files in the same directory where the configuration files are either with `.tf` or `.tf.json` extension. 

The root directory would be built from the files and in the in the current working directory. 

Other child modules can be referenced from child directories.

In it's simplest form the root module would contain a single file of `.tf` or `.tf.json` extension. 

Configuration can expand by adding new configuration files within the root module, or by organising resources through child modules.

e.g If you required 3 VM's on AWS but you wanted to have separate configuration files, your projects root directory file structure could look like this:
```
example_2
|---main.tf
|---db.tf
|---backend.tf
|---frontend.tf
```
Where each file would be a separate configuration file for a resource.

## Order of configuration

The order of blocks is not significant as the language is declarative. 

There is only one exception to this rule which is the `provisioner` block.

Resources will be automatically processed in the correct order based on what are the relationships between the resources. 

Hence, it's up to the implementer to decide on how to structure the files and how many to have.

## Comments

There are three types of comments supported:
- `#` used for single line comments
- `//` also used for single line comments, an alternative way to `#`
- `/*` start of the multi line comment where `*/` ends the multi line comment

`#` is the preferred way of leaving comments in the configuration files. 

Formatting tool converts the `//` into `#` comments, the reason for this is that the `//` style is not idiomatic.

## Tasks

You will now create a resource on AWS, using some functionality from this module.

### Prerequisites

1. Have **aws cli** installed
    2. You can install it by running the following python command, keep in mind you need to have python installed:
    `pip install awscli`
3. Know your AWS `access` and `secret` keys

First let's authenticate with aws so that terraform could execute the configuration file, run the following command:
`aws configure`
You will be asked to provide the following things:
* **AWS Access Key ID** this is where you would need to provide your *access* key
* **AWS Secret Access Key ID** this is the *secret* key
* **Default region name** would be **eu-west-2**
You might get asked additionally to specify what formatting you want to use, enter **json**.

For the next step create a new folder, you can pick any name for it but a suggested one would be `example_2`.

Within the newly created folder, create a new file called `main.tf`.

Open the `main.tf` with a text editor of your choosing.

Now paste the following contents into the `main.tf` file:
```
provider "aws" {
	region = "eu-west-2"
}
``` 
You may have noticed that there is only the region declared and no `access_key` or `secret_key` declared, this is done on purpose. 

We're doing it in this way so that when you will be uploading these configuration files to GitHub you wouldn't accidentally expose them.

In later steps we will configure the *access* and *secret* keys using *aws cli* which is the more secure way of doing it.

Now let's declare two variables that we'll use for the resource declaration. 

Paste the following below the *provider* block:
```
variable "ami" {
	description = "machine image"
	default = "ami-f976839e"
}

variable "type" {
	# instance type
	/*
		This will determine how many CPU and RAM will be assigned
	*/
	default = "t2.micro"
}
``` 
We're declaring two variables, the first variable is called **ami**, and the value it holds is under the **default** argument. 

It also holds a description about this variable.

The second variable is **type**, we can see that it has two types of comments, a single line comment and a multi line comment.

The default argument is holding the value of what will be the type of instance we'll be creating.

Paste the following below the variables:
```
resource "aws_instance" "example" {
	ami = var.ami
	instance_type = var.type
}
```

In this resource block we're specifying what amazon machine image to use for the operating system, it's value is held by **ami** argument where the value is received by making a reference to **var*, it allows us to get a specific variables value by referring to it's name. 

In this case when we want to use the value of the **ami** variable we need to make a reference to it like this: `var.ami`.

The second argument is **instance_type** which specifies which machine configuration to use, it will determine how many vCPU's will be assigned as well as the amount of RAM. 

Similarly in order to get the value of the variable we need to make a reference to it like this: `var.type`.

Next switch to the terminal, if you have closed it already, re-open it in the directory where the `main.tf` file is located at. 

First let's execute the following command:

`terraform init`

Next let's execute:

`terraform plan`

Lastly let's create the resource by executing:

`terraform apply`

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
    `terraform destroy` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.
