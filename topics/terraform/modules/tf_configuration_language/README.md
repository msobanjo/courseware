# Configuration language

### Overview
Terraform uses it's own configuration language. 
It's designed to describe infrastructure in a concise way. 
The language is declarative meaning it describes an intended goal rather than the steps of how to reach that goal.

### Modules and resources

Main purpose of Terraform language is to declare resources. 
Any additional features that the language has are meant to aid the primary purpose. 

A *resource* describes a single object of infrastructure, but multiple resources can be combined into a *module* where relationships between them could be defined.

### Basic syntax

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

