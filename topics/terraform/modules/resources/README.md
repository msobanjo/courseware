# Resources

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Meta-parameters](#metaparameters)
		- [depends_on](#dependson)
		- [count](#count)
		- [for_each](#foreach)

<!--TOC_END-->
## Overview

This module will cover *resources* more in depth.

A resource in Terraform is simply a component of your infrastructure.

Terraform resources can be anything from cloud virtual machine instances, to GitHub repositories and DNS records. 

Each type of resource has their own attributes and arguments.

### Meta-parameters

All resources do have several things in common, starting with meta-parameters. 

Meta-parameters are configuration keys available to all resources.

An example of a resource meta-parameter could be provider aliases. 
A resource can explicitly declare a provider to use with the provider key.

This is an example configuration file to better visualise what meta-parameter is. 
In this example meta-parameters would be: provider. 

```hcl
provider "aws" {
  region = "eu-west-2"
  alias  = "aws-uk"
}

resource "aws_instance" "example-uk" {
  provider = "aws.aws-uk"
  ami           = var.ami-uk
  instance_type = var.type
}
```

In total there are six meta-parameters:
- **depends_on**
- **count**
- **for_each**
- **provider**
- **lifecycle**
- **provisioner and connect**

#### depends_on

**depends_on** meta-argument is used to handle hidden resource dependencies when Terraform can't automatically infer them.

You would need to explicitly specify a dependency when a resource relies on another resources behaviour, but doesn't access the resources data.

If **depends_on** is present, it must be a list of references to other resources of the same module.

The **depends_on** argument should be used only as a last resort mean, additionally it would be a good practice to leave a comment explaining why is it used.

Here is an example of **depends_on** being used:

```hcl
resource "aws_iam_role_policy" "example-admin-role" {
  name   = "example-admin"
  role   = aws_iam_role.owner
}

resource "aws_instance" "example-instance" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
  depends_on = [
    aws_iam_role_policy.example,
  ]
}
```

In this example `example_instance` has a dependency on the `example-admin-role`.

#### count

By default, terraform configures only one real infrastructure object. 

Although, in some cases you want to manage several similar objects. 

Terraform has two ways to do this: **count** and **for_each**, first we'll look at *count*.

*Count* accepts a whole number, it then creates that number of instances of the resource. 

Here's an example of creating four instances through the use of count:

```hcl
resource "aws_instance" "server" {
  count = 4
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

After creating these four resources if we wanted to do something with one of the instances we could get access to it through it's index. 

In the resource block where the count is used, an additional object for `count` is created and it has an attribute `index`. 
This allow to access the index of which resource you would be using. 
It's zero based index.  
In order to get access to the index the syntax would be: 
`count.index`

Here's an example of using the first instance:
`aws_instance.server[0]`

If your resource instances are identical or close to being identical, count is appropriate to use. 
If some of the instance arguments need distinct values that can't be directly derived from an integer number, it's would be easier to achiebe by using **for_each**.

#### for_each

The default behaviour of a resource block is that it only creates a single infrastructure object. 

There may be a case where you would require multiple similar resources, then there are two options of how to implement it: 
- **for_each**
- **count**

**for_each** requires either a **map** or a **set** of string arguments. 

For every provided argument an infrastructure object will be created. 

Each infrastructure object is distinct, what this entails is that every object is created, updated, destroyed separately when the configuration is applied.

<details>

<summary>AWS example</summary>

In this example, there are two instances being created. 

Iteration is done with for_each where the the value in the map are the two availability zones. 
 
Within the resource *example* the value of current iteration is used as the value for the *availability_zone*.

```hcl
provider "aws" {
  region = "eu-west-2"
  alias  = "aws-uk"
}

variable "ami-uk" {
  description = "machine image uk"
  default     = "ami-f976839e"
}

variable "type" {
  default = "t2.micro"
}

variable "zone" {
  description = "map of availability zones for eu-west-2"
  default     = {
    1 = "eu-west-2a"
    2 = "eu-west-2b"
  }
}

resource "aws_instance" "example" {
  provider = "aws.aws-uk"

  for_each = var.zone

  availability_zone = each.value # each is covered in the section below
  ami           = var.ami-uk
  instance_type = var.type
}
```

</details>

