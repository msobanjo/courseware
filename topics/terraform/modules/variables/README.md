# Variables

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Default](#default)
- [Providing a value](#providing-a-value)
- [Variable Precedence](#variable-precedence)
- [Tasks](#tasks)
	- [AWS Variables with TFVARS File](#aws-variables-with-tfvars-file)
		- [Prerequisites](#prerequisites)
		- [Authenticating](#authenticating)
		- [Creating the directory and configuration file](#creating-the-directory-and-configuration-file)
		- [Adding the provider](#adding-the-provider)
		- [Adding resource](#adding-resource)
		- [Adding variables](#adding-variables)
		- [Adding variable values in variableValues file](#adding-variable-values-in-variablevalues-file)
		- [Formatting](#formatting)
		- [Final configuration file states](#final-configuration-file-states)
		- [Running the configuration file](#running-the-configuration-file)
		- [Summary](#summary)
		- [Clean up](#clean-up)
	- [AWS Variables with CLI Option](#aws-variables-with-cli-option)
		- [Prerequisites](#prerequisites-1)
		- [Providing values through the terminal](#providing-values-through-the-terminal)
		- [Running the configuration file](#running-the-configuration-file-1)
		- [Summary](#summary-1)
		- [Clean up](#clean-up-1)
	- [Passing variable values with -var option](#passing-variable-values-with-var-option)
		- [Prerequisites](#prerequisites-2)
		- [Providing values through the terminal](#providing-values-through-the-terminal-1)
		- [Running the configuration file](#running-the-configuration-file-2)
		- [Summary](#summary-2)
		- [Clean up](#clean-up-2)
	- [Passing value through environment variable](#passing-value-through-environment-variable)
		- [Prerequisites](#prerequisites-3)
		- [Providing values through the terminal](#providing-values-through-the-terminal-2)
		- [Adding environment variables](#adding-environment-variables)
		- [Running the configuration file](#running-the-configuration-file-3)
		- [Summary](#summary-3)
		- [Clean up](#clean-up-3)

<!--TOC_END-->
## Overview

Variables are a key part of the TF syntax, we will now take a deeper look at them in order to understand them better.

## Default

The **default** key for a variable specifies what value to use if no other value is assigned.

In this example you can see that we're providing a default value for the variable.

```hcl
variable "ami" {
  default     = "ami-f976839e"
}
```

The **default** value is used by Terraform to infer the type of the variable. 

When no default is given and no type is specified, the default type of **string** is used. 

## Providing a value

The **default** value can’t use interpolations, you will learn about interpolations in a separate module.
 
When no **default** is provided, you must specify a value. 

You have several options for specifying the value of a variable.
 
If you specify a value when a **default** is provided, the specified value is used overriding the **default**.

Other ways to provide a value include:
- **Have Terraform interactively prompt you to enter values for missing variables.**
This may work for small exercises but is painful to re-enter the values every time you issue a plan or apply. 
It is also not applicable for automation.
- **Using the `-var` command line option for both plan and apply commands.**
You specify the variable name followed by an equal sign and the value you want to use for the variable. 
You can use any many `-var` options as required, but the commands can get very long if you have more than a few variables.
- **Using variable files.**
Variable files use HCL syntax for defining the variable values. 
Variable files can be included using the var-file option or they can be automatically included if they are in your current working directory and are either named *terraform.tfvars* or have a file extension of *.auto.tfvars*. 
You can use multiple variable files. 
Variables defined using the `-var-file` option override variables defined using automatic variable files.
- **Using environment variables.**
When setting Terraform variables using environment variables the name of the environment variable must begin with **TF_VAR_** and be followed by the name of the Terraform variable. 

## Variable Precedence

When a variable is defined multiple times, the value of the variable is usually set to the highest precedent definition. 

One thing to note is that map variables are set to the highest precedent definition. 

Instead the values of the map variable definitions are merged. 

All other variables are overridden by the highest precedent value.

The order of precedence from lowest to highest is as follows:

- default values have the lowest precedence
- then environment variables
- followed by automatic variable files
- and -var and `-var-files` share the highest precedence level

When variables are defined within the same precedence level, the last value is used. 
For example, if you define a variable in a var-file and a -var option, the one that you specify last on the command-line will take precedence.

## Tasks

### AWS Variables with TFVARS File

<details>

<summary>In this task you will use a <i>variablesValues</i> file to give values to your <i>variables</i> while creating a resource on AWS.</summary>

#### Prerequisites

- Have **aws cli** installed
    - You can install it by running the following python command, keep in mind you need to have python installed:
    `pip install awscli`
- Know your AWS `access` and `secret` keys

#### Authenticating

First let's authenticate with aws so that terraform could execute the configuration file, run the following command:

`aws configure`

You will be asked to provide the following things:
* **AWS Access Key ID** this is where you would need to provide your *access* key
* **AWS Secret Access Key ID** this is the *secret* key
* **Default region name** would be **eu-west-2**
You might get asked additionally to specify what formatting you want to use, enter **json**.

#### Creating the directory and configuration file

For the next step create a new folder, you can pick any name for it but a suggested one would be `terraform-variables`.

Within the newly created folder, create the following new files within the directory:
- `main.tf`
- `variables.tf`
- `variableValues.tfvars`

#### Adding the provider

Now paste the following contents into the `main.tf` file:
```hcl
provider "aws" {
	region = "eu-west-2"
}
``` 

#### Adding resource

Paste the following below the variable in the `main.tf` file:
```hcl
resource "aws_instance" "example" {
	ami = var.ami
	instance_type = type
}
```

Notice that there's no need to use `var.` in order to point to the variables value, you can make a direct reference to it.

#### Adding variables

Paste the following into the `variables.tf` file:

```hcl
variable "ami" {
  description = "machine image"
}

variable "type" {
  description = "machine size"
}
```

As you can see there are no set default values, they will be set in the `variableValues.tfvars` file.

#### Adding variable values in variableValues file

Open `variableValues.tfvars` file and place the following text in the file:

```hcl
ami = "ami-f976839e"
type = "t2.micro"
```

Now the variables defined in the `variables.tf` file will have the values set once TF starts running.

#### Formatting

Format the configuration files by running the command:
```shell script
terraform fmt
```

#### Final configuration file states

Let's check that you have all the configuration files ready.

`main.tf` configuration file should look like this:

```hcl
provider "aws" {
  region     = "eu-west-2"
}

resource "aws_instance" "example" {
  ami           = ami
  instance_type = type
}
```

`variables.tf` configuration file should look like this:

```hcl
variable "ami" {
  description = "machine image"
}

variable "type" {
  description = "t2.micro"
}
```

`variableValues.tfvars` configuration file should look like this:

```hcl
ami = "ami-f976839e"
type = "machine size"
```

If the configuration files are like this, continue with the task. 

If the configuration files you have are different, update them to match them.

#### Running the configuration file

Next, open a terminal in the directory where the configuration files are.

First let's execute the following command to get the plugins for AWS:

`terraform init`

Next let's execute to see what changes will be made, we will need to tell TF where the variable values are defined, it's done through `-var-file` flag and then providing a value to where the file is located.

We placed `variableValues.tfvars` in the same directory, therefore we can make a reference to it directly.

`terraform plan -var-file="variableValues.tfvars"`

Lastly let's create the resource by executing:

`terraform apply -var-file="variableValues.tfvars"`

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

#### Summary

In this task you used three configuration files to deploy a resource in AWS.

Additionally the variable values were defined in a different file from where the variables were declared.

#### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
`terraform destroy -var-file="variableValues.tfvars"` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

</details>

### AWS Variables with CLI Option

<details>

<summary>In this task you will attempt to provide variable values in a different way.</summary>

#### Prerequisites

In order to do this task you need to have the *AWS Variables with TFVARS File* (previous) task completed and have the `main.tf`, `variables.tf` files.

#### Providing values through the terminal

Create a new directory like `terraform-variables-aws-using-cli`.

Copy the `main.tf`, `variables.tf` files into the directory.

#### Running the configuration file

Next, open a the terminal in the directory where the configuration files are.

First let's execute the following command to get the plugins for AWS:

`terraform init`

Next let's execute the following command in order to see what changes will be made, as in this task there is no `variablesValues.tfvars` file to provide the variable values. 
Once you're going to execute the following command, you will be prompted to provide values for the variables. 
A name of the variable will be displayed, similarly if there is a `description` it will be printed to you as well in order to give some context.

`terraform plan`

Lastly let's create the resource by executing, you will be prompted to provide variable values again as you execute the following command:

`terraform apply`

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

#### Summary

In this task you provided variable values directly in the terminal when you were prompted for them.

#### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
`terraform destroy` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

</details>

### Passing variable values with -var option

<details>

<summary>In this task you will pass in variable values directly by using the <b>-var</b> flag option.</summary>

#### Prerequisites

In order to do this task you need to have the *AWS Variables with TFVARS File* (previous) task completed and have the `main.tf`, `variables.tf` files.

#### Providing values through the terminal

Create a new directory like `terraform-variables-aws-using-cli-continuation`.

Copy the `main.tf`, `variables.tf` files into the directory.

#### Running the configuration file

Next, open a the terminal in the directory where the configuration files are.

First let's execute the following command to get the plugins for AWS:

`terraform init`

Next let's execute the following command to see what changes will be made, observe that the variable values are passed directly:

`terraform plan -var='ami=ami-f976839e' -var='type=t2.micro'`

Lastly let's create the resource by executing:

`terraform apply -var='ami=ami-f976839e' -var='type=t2.micro'`

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

#### Summary

In this task you provided variable values directly in the terminal when you were prompted for them.

#### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
`terraform destroy -var='ami=ami-f976839e' -var='type=t2.micro'` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

</details>

### Passing value through environment variable

<details>

<summary>In this task you will provide variable values through environment variables.</summary>

#### Prerequisites

In order to do this task you need to have the *AWS Variables with TFVARS File* (previous) task completed and have the `main.tf`, `variables.tf` files.

#### Providing values through the terminal

Create a new directory like `terraform-variables-aws-environment-variables`.

Copy the `main.tf`, `variables.tf` files into the directory.

#### Adding environment variables

Remember that the environment variables have to start with `TF_VAR`.

The first environment variables name will be `TF_VAR_ami` and the value associated with it should be `ami-f976839e`.

The second environment variables name should be `TF_VAR_type` and the value associated with it should be `t2.micro`. 

#### Running the configuration file

Next, open a the terminal in the directory where the configuration files are.

First let's execute the following command to get the plugins for AWS:

`terraform init`

Next let's execute the following command to see what changes will be made.

`terraform plan`

Lastly let's create the resource by executing:

`terraform apply`

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

#### Summary

In this task you provided variable values through the environment variables.

#### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
`terraform destroy` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

</details>
