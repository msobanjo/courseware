# Resources

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Meta-parameters](#metaparameters)
		- [depends_on](#dependson)
		- [count](#count)
		- [for_each](#foreach)
			- [each](#each)
	- [provider](#provider)
		- [lifecycle](#lifecycle)
			- [create_before_destroy](#createbeforedestroy)
			- [prevent_destroy](#preventdestroy)
			- [ignore_changes](#ignorechanges)
		- [provisioner and connection](#provisioner-and-connection)
	- [Operation timeouts](#operation-timeouts)
	- [Local only resources](#local-only-resources)
	- [Tasks](#tasks)
		- [Prerequisites](#prerequisites)
		- [Authenticating](#authenticating)
		- [Creating the directory and configuration file](#creating-the-directory-and-configuration-file)
		- [Populating the configuration file](#populating-the-configuration-file)
		- [Formatting](#formatting)
		- [Running the configuration file](#running-the-configuration-file)
		- [Clean up](#clean-up)

<!--TOC_END-->
## Overview

This module will cover *resources* more in depth.

A **resource** in Terraform is simply a component of your infrastructure.

Terraform resources can be anything from cloud virtual machine instances, to GitHub repositories and DNS records. 

Each type of resource has their own attributes and arguments.

### Meta-parameters

All resources do have several things in common, starting with meta-parameters. 

Meta-parameters are configuration keys available to all resources.

An example of a resource meta-parameter could be provider aliases. 

A resource can explicitly declare a provider to use with the provider key.

This configuration file shows an example meta-parameter **alias** 

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

*depends_on* meta-argument is used to handle hidden resource dependencies when Terraform can't automatically infer them.

You would need to explicitly specify a dependency when a resource relies on another resources behaviour, but doesn't access the resources data.

If *depends_on* is present, it must be a list of references to other resources of the same module.

The *depends_on* argument should be used only as a last resort mean, additionally it would be a good practice to leave a comment explaining why is it used.

Here is an example of *depends_on*:

```hcl
resource "aws_iam_role_policy" "example-admin-role" {
  name   = "example-admin"
  role   = aws_iam_role.owner
}

resource "aws_instance" "example-instance" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
  depends_on = [
    aws_iam_role_policy.example
  ]
}
```

In this example `example_instance` has a dependency on the `example-admin-role`

#### count

By default, terraform configures only one infrastructure object. 

If you wanted to configure several similar infrastructure objects that is possible as well. 

Terraform has two ways to do this: **count** and **for_each**, first we'll look at *count*.

*Count* accepts a whole number, it then creates that number of instances of the resource where it is declared. 

Here's an example of creating four instances by using count:

```hcl
resource "aws_instance" "server" {
  count = 4
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

After creating these four resources if we wanted to do something with one of the instances we could get access to it through it's index. 

In the resource block where the count is used, an additional object for `count` is created and it has an attribute `index` 

This allow to access the index of which resource you would be using. 

Index is zero based meaning that the first instance will be at the index of zero ([0]).

In order to get access to the index the syntax would be: 

`count.index`

Here's an example of using the first instance:

`aws_instance.server[0]`

If your resource instances are identical or close to being identical, count is appropriate to use. 

If some of the instance arguments need distinct values that can't be directly derived from an integer number, it's would be easier to achiebe by using **for_each**.

#### for_each

**for_each** requires either a **map** or a **set** of string arguments. 

For every provided argument an infrastructure object will be created. 

Each infrastructure object is *distinct*, what this entails is that every object is *created*, *updated*, *deleted* separately when the configuration is applied.

<details>

<summary>AWS example</summary>

In this example, there are two instances being created. 

Iteration is done with *for_each* where the the value in the map are the two availability zones. 
 
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

When *for_each* is used, Terraform is able to distinguish between the resource block and the resources associated with the resource block. 

This allows to make a reference to a specific instance. 

Instances are identified by the *map* or *set* key that was provided to the *for_each*.

Here is an example of making a reference to the first instance which has the key of `1` within another resource and re-using the *ami* and *instance_type*:

<details>

<summary>AWS example</summary>

```hcl
resource "aws_instance" "example" {
  provider = "aws.aws-uk"

  for_each = var.zone

  availability_zone = each.value
  ami           = var.ami-uk
  instance_type = var.type
}

resource "aws_instance" "example2" {
  ami = aws_instance.example[1].ami
  instance_type = aws_instance.example[1].instance_type
}
```

</details>

##### each

When *for_each* is used, an additional object is created under the name of **each**. 

This object gives the ability to make a reference to the current object and configure it like setting an instance to a particular availability zone.

There are two attributes to **each** object: 
- **key** - this is the key associated with the map or set for this instance
- **value** - this is the value associated with the map or set for this instance

### provider

Terraform allows multiple providers, there can be a default provider and multiple others as long as they will have aliases.

Multiple providers could be used when managing resources in different regions, or different cloud providers altogether.

**provider** meta-tag overrides the default provider with the one that is specified.

Here is an example of two providers and the *provider* meta-tag being used:

<details>

<summary>AWS example</summary>

In this example there are two providers defined, the first provider going from top to bottom will be the *default* one.

The second provider has an alias, this will be used to make a reference that this provider should be used when interacting with the resource in the resource block.
 
```hcl
provider "aws" {
  region = "us-east-1"
  version = "2.8"
}

provider "aws" {
  region = "eu-west-2"
  alias  = "aws-uk"
}

resource "aws_instance" "example-uk" {
  provider = "aws.aws-uk"
  ami           = "ami-f976839e"
  instance_type = "t2.micro"
}
```

</details>

#### lifecycle

Additional details about the resource lifecycle can be provided in the *resource* block by the use of **lifecycle** meta-tag.

**lifecycle** has additional meta-arguments like:
- **create_before_destroy**
- **prevent_destroy**
- **ignore_changes**

##### create_before_destroy

**create_before_destroy** requires a boolean value to be set.

Terraforms default behaviour is to destroy the resource if the requested change cannot be applied due to some limitations. 

After destroying the resource a new one will be created in it's place with the applied change and it will replace the initial resource.

**create_before_destroy** allows to change this behaviour. 

When *create_before_destroy* is set, a new resource will be created first with the applied change, and only then will the previous resource will be destroyed.

<details>

<summary>AWS example</summary>
 
```hcl
resource "aws_instance" "example-uk" {
  provider = "aws.aws-uk"
  ami           = "ami-f976839e"
  instance_type = "t2.micro"
  lifecycle {
    create_before_destroy = true
  }
}
```

</details>

##### prevent_destroy

**prevent_destroy** requires a boolean value to be set.

When this meta-argument is set to *true* any attempt to destroy the resource will be rejected with an error message, as long as this meta-argument is still present in the configuration file for the resource.

One of the use cases could be to prevent precious resources like a database from being destroyed. 

The only downside is that by having this enabled could be harder to make changes to the resource, additionally calling *destroy* command once the resource was created wouldn't actually destroy this resource.

<details>

<summary>AWS example</summary>
 
```hcl
resource "aws_instance" "example-uk" {
  provider = "aws.aws-uk"
  ami           = "ami-f976839e"
  instance_type = "t2.micro"
  lifecycle {
    prevent_destroy = true
  }
}
```

</details>

##### ignore_changes

**ignore_changes** take a list of attribute names.

Terraforms default behaviour is to check whether there are new changes to the current configuration files comparing it to the previous version.

There may be some cases outside of Terraform where a resource will be modified, then Terraform would attempt to fix that by setting the values back to the ones that are defined in the configuration file.

You might not always want this sort of behaviour and the **ignore_changes** allows to ignore changes happening to some attributes.

<details>

<summary>AWS example</summary>

In this example *tags* is passed in the list.

This example would make any changes happening outside of Terraform to the *tags* attribute to be ignored by Terraform.
 
```hcl
resource "aws_instance" "example-uk" {
  provider = "aws.aws-uk"
  ami           = "ami-f976839e"
  instance_type = "t2.micro"
  lifecycle {
    ignore_changes = [tags]
  }
}
```

</details>

#### provisioner and connection

There are certain cases where infrastructure object require additional actions to be taken before they're fully usable, for example an instance might require some file uploaded to it with credentials.

Resource provisioners are what allow these additional actions to be implemented.

Provisioner actions like copying a file to an instance should be used sparingly, the reason for it is that this action and the state of the file cannot be represented as declarative action, hence making it not possible for Terraform to manage it after the action took place.

Additional actions can also be done when resources are getting destroyed.

Provisioners will be covered more in depth within a different module.

### Operation timeouts

Certain resource types allow to define how long they can take for operations to take place, this is defined within the *resource* block.

For example *aws_instance*, allows to define **timeouts** for *create* (default 10min), *update* (default 10min), *delete* (default 20min).

<details>

<summary>AWS example</summary>

In this example the allowed time it takes for the creation of resource is overridden to five minutes and the destruction of it is overridden to two hours.
 
```hcl
resource "aws_instance" "example-uk" {
  provider = "aws.aws-uk"
  ami           = "ami-f976839e"
  instance_type = "t2.micro"
  timeouts {
    create = "5m"
    delete = "2h"
  } 
}
```

</details>

### Local only resources

While majority of the resources managed by Terraform are remote, where the management is done via an API, there are some resources that are local only to Terraform.

Things like: 

- **private keys**
- **TLS certificates**
- **ids that were randomly generated**

Local only resources share the same behaviour as any other resources on Terraform, difference being that the data is local to Terraforms state.

Destroying such a resource would only mean to remove it's state as well as discarding the data.

### Tasks

<details>

<summary>AWS task</summary>

This task will combine a couple of things that were covered in this module:
- two *aws_instance* will be created through *for_each*
- destruction of the instances will be prevented with the *lifecycle*
- timeouts will be set for the creation and deletion operations

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

For the next step create a new folder, you can pick any name for it but a suggested one would be `terraform_resources_example`.

Within the newly created folder, create a new file called `main.tf`.

Open the `main.tf` with a text editor of your choosing.

#### Populating the configuration file

Paste the following into the `main.tf` file.

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
  availability_zone = each.value
  ami           = var.ami-uk
  instance_type = var.type

  lifecycle {
    prevent_destroy = true
  }

  timeouts {
    create = "5m"
    delete = "2h"
  }

}
```

In this example you should notice a combination of things that make up the whole:
- instead of using a *default provider* an *alias* is given and used
- *variables* are used and declared in the same configuration file
- a *map variable* is used to define availability zones
- *for_each* is used to create two instances where the keys are coming from the map variable
- *each* is used to set a value of the *availability_zone* where the value for the availability zone is coming from the map variable
- *lifecycle* is used with the meta argument of *prevent_destroy* enabled
- *timeout* is used with meta arguments to set timeout times for the *create* and *delete* operations

#### Formatting

Format the configuration file by running the command:
```bash
terraform fmt
```

#### Running the configuration file

Next switch to the terminal, if you have closed it already, re-open it in the directory where the `main.tf` file is located at. 

First let's execute the following command to download the AWS provider plugin so that Terraform can communicate with AWS:

`terraform init`

Next let's execute this to see what Terraform plans on doing:

`terraform plan`

Finally, let's apply the configured resources by executing:

`terraform apply`

Ensure that you check the changes that this action will make to your infrastructure and type `yes` to agree.

Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 

Make sure that you are within the correct region, otherwise you won't be able to see the resource.

#### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:

`terraform destroy` 

Ensure that you check the changes that this action will make to your infrastructure and type `yes` to agree.

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource - even if it wasn't deleted!

</details>
