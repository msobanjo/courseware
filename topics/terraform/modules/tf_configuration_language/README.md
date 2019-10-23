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

