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

### Configuration files

Terraform language configuration files uses an extension of `.tf`, an example file name would be `main.tf`. 
Although, that isn't the only supported file extension, there is also the JSON syntax where the files have the extension of `.tf.json`, an example file name would be `main.tf.json`. 

Configuration files need to use the `UTF-8` encoding. 
Even though both windows and unix style line endings are supported you should use the unix style ones. 
Windows line endings are represented as `\r\n` where unix are `\n`.

*Module* is a one or more configuration files in the same directory where the configuration files are either with `.tf` or `.tf.json` extension. 

The root directory would be built from the files and in the in the current working directory. 
Other child modules can be referenced from child directories.

In it's simplest form the root module would contain a single file of `.tf` or `.tf.json` extension. 
Configuration can expand by adding new configuration files within the root module, or by organising resources through child modules.

### Order of configuration

The order of blocks is not significant as the language is declarative. 
There is only one exception to this rule which is the `provisioner` block.

Resources will be automatically processed in the correct order based on what are the relationships between the resources. 
Hence, it's up to the implementer to decide on how to structure the files and how many to have.

