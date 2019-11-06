# Resources

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Meta-parameters](#metaparameters)

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

