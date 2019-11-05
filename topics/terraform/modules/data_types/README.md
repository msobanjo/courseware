# Data types

## Overview

In this module you will learn about the various data types that are available in HCL. 

### Strings

The primitive types include **strings**, which are always enclosed in double quotation marks.
Here's an example of a string data type:
```hcl
provider "aws" {
  region     = "eu-west-2"
}
```
Both `aws` and `eu-west-2` are of string data type.

### Numbers

**Numbers** is also a primitive data type, different from strings they are not encased in double quotation marks.
Here's an example of a number value:
```hcl
provider "aws" {
  region = "eu-west-2"
  version = 2.7
}
```
In this example `version` value is a number data type.

### Boolean

**Boolean** belongs to primitive data types. 
It has two possible values:
- true
- false

Here is an example of a boolean:
```hcl
variable "active" {
  default = false
}
```
You can see that in this example the value of **false** is used as the default value for the `active` variable. 

### Lists

**List** is a complex data type which is enclosed in brackets and separate items of primitive types with a comma.


### Maps