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
List is allowed to be empty.

Here's an example of a list:
```hcl
variable "users" {
  type    = "list"
  default = ["admin", "accountant"]
}
```
In this example we see that the values in the map are encased within the square brackets and separated with comma. 
If you wanted to add more values you would need to follow the same rule and separate them with commas.

When retrieving a value from the list you need to use a function `element` it takes two arguments. 
First argument is the list we want to get the element from. 
Second argument is the index of the element. 
Index starts at zero.

Here's an example of retrieving element from a list:
```hcl
element(["a", "b", "c", "d"], 2)
```
As the list index is zero based, the returned value would be `c`. 

### Maps

**Map** are enclosed in braces and assign a collection of keys and values pairs.
Map is allowed to be empty.

Here's an example of a map:
```hcl
variable "images" {
  type    = "map"
  default = {
    "eu-west-1" = "ami-f976839e"
    "eu-west-2" = "ami-f976839e"
  }
}
```
In this example we can see two key value pairs. 
The first pair is where the key is `eu-west-1` and the value assigned to it is `ami-f976839e`. 
Second pair is where the key is `eu-west-2` and the value assigned to it is `ami-f976839e`. 
Take note of how map values are not in square brackets compared to a list.

When retrieving a value from the map you need to use a function `lookup` it takes three arguments. 
First argument is the list we want to get the element from. 
Second argument is the key associated with the value.
Third argument is the default value to be used if there will not be a value associated with the key provided.

Here's example of retrieving a value from a map:
```hcl
lookup({password="supersecure", username="accountant"}, "username", "not found")
```

### Task

#### Knowledge check

Let's test your knowledge of how well you remember this module.

##### Question 1

How many data types there are?

<details>

<summary>Click to reveal answer</summary>
5
</details>

##### Question 2

How many primitive types there are?

<details>
<summary>Click to reveal answer</summary>
3
</details>

##### Question 3

What are the primitive types?

<details>
<summary>Click to reveal answer</summary>
string, number, boolean
</details>

##### Question 3

What are the complex data types?

<details>
<summary>Click to reveal answer</summary>
list, map
</details>