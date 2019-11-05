# Variables

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Default](#default)
- [Providing a value](#providing-a-value)
- [Variable Precedence](#variable-precedence)
- [Tasks](#tasks)

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
- having Terraform interactively prompt you to enter values for missing variables. 
This may work for small exercises but is painful to re-enter the values every time you issue a plan or apply. 
It is also not applicable for automation.
- using the -var command line option for both plan and apply commands. 
You specify the variable name followed by an equal sign and the value you want to use for the variable. 
You can use any many -var options as required, but the commands can get very long if you have more than a few variables.
- using variable files. 
Variable files use HCL syntax for defining the variable values. 
Variable files can be included using the var-file option or they can be automatically included if they are in your current working directory and are either named *terraform.tfvars* or have a file extension of *.auto.tfvars*. 
You can use multiple variable files. 
Variables defined using the -var-file option override variables defined using automatic variable files.
- using environment variables. 
When setting Terraform variables using environment variables the name of the environment variable must begin with TF_VAR_ and be followed by the name of the Terraform variable. 

## Variable Precedence

When a variable is defined multiple times, the value of the variable is usually set to the highest precedent definition. 
One thing to note is that map variables are set to the highest precedent definition. 
Instead the values of the map variable definitions are merged. 
All other variables are overridden by the highest precedent value.

The order of precedence from lowest to highest is as follows:

- default values have the lowest precedence
- then environment variables
- followed by automatic variable files
- and -var and -var-files share the highest precedence level

When variables are defined within the same precedence level, the last value is used. 
For example, if you define a variable in a var-file and a -var option, the one that you specify last on the command-line will take precedence.

## Tasks

### AWS task

<details>

<summary>In this task you will use a variables file to give values to your variables while creating a resource on AWS.</summary>

### Prerequisites

1. Have **aws cli** installed
    2. You can install it by running the following python command, keep in mind you need to have python installed:
    `pip install awscli`
3. Know your AWS `access` and `secret` keys

### Authenticating

First let's authenticate with aws so that terraform could execute the configuration file, run the following command:
`aws configure`
You will be asked to provide the following things:
* **AWS Access Key ID** this is where you would need to provide your *access* key
* **AWS Secret Access Key ID** this is the *secret* key
* **Default region name** would be **eu-west-2**
You might get asked additionally to specify what formatting you want to use, enter **json**.

### Creating the directory and configuration file

For the next step create a new folder, you can pick any name for it but a suggested one would be `example_4`.

Within the newly created folder, create a new file called `main.tf`.

Additionally create a file called `variableValues.tfvars`.

### Adding the provider

Now paste the following contents into the `main.tf` file:
```hcl
provider "aws" {
	region = "eu-west-2"
}
``` 
You may have noticed that there is only the region declared and no `access_key` or `secret_key` declared, this is done on purpose. 

We're doing it in this way so that when you will be uploading these configuration files to GitHub you wouldn't accidentally expose them.

In later steps we will configure the *access* and *secret* keys using *aws cli* which is the more secure way of doing it.

### Adding resource

Paste the following below the variable in the `main.tf` file:
```hcl
resource "aws_instance" "example" {
	ami = var.ami
	instance_type = var.type
}
```

In this resource block we're specifying what amazon machine image to use for the operating system, it's value is held by **ami** argument where the value is received by making a reference to **var*, it allows us to get a specific variables value by referring to it's name. 

In this case when we want to use the value of the **ami** variable we need to make a reference to it like this: `var.ami`.

The second argument is **instance_type** which specifies which machine configuration to use, it will determine how many vCPU's will be assigned as well as the amount of RAM. 

Similarly in order to get the value of the variable we need to make a reference to it like this: `var.type`.

### Adding variables

Create a new file called `variables.tf` in the `example_4` directory.

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

## Adding variable values in variableValues file

Open `variableValues.tfvars` file and place the following text in the file:

```hcl
ami = "ami-f976839e"
type = "t2.micro"
```

Now the variables defined in the `variables.tf` file will have the values set once TF starts running.

### Formatting

Format the configuration files by running the command:
```shell script
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

In this task you used three configuration files to deploy a resource in AWS.

You may have noticed that there was no need in making a reference to the variables configuration file in order to get the variables value.

This is because terraform appends configuration files and the variables would end up in the same scope.

Additionally the variable values were defined in a different file from where the variables are declared.

### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
`terraform destroy` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

</details>