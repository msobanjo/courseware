# Variables

## Overview

Variables are a key part of the TF syntax, we will now take a deeper look at them and try to understand them better.

## Default

The default key for a variable specifies what value to use if no other value is assigned.

In this example you can see that we're providing a default value for the variable.

```hcl
variable "ami" {
  description = "machine image"
  default     = "ami-f976839e"
}
```

The default value is used by Terraform to infer the type of the variable. 

When no default is given and no type is specified, the default type of string is used. 

## Providing a value

The default value can’t use interpolations.
 
When no default is provided, you must specify a value. 

You have several options for specifying the value of a variable.
 
If you specify a value when a default is provided, the specified value is used overriding the default.

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
