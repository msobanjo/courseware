# Groovy Syntax
## Overview
This document aims to cover the basics of the Groovy programming lanuguage's syntax.
Many of the concepts will be easier to pick up if you have used a programming language like Java before.

## Commenting
Comments in Groovy are just like Java:
### Single Line Comments
```groovy
// single line comment
```
### Multi Line Comments
Multi line comments start with `/*` and end with `*/`, this saves you having to put `//` on every commented line.
```groovy
/* 
    multi line comment
*/
```
### Inline Commenting
The same syntax for multi line comments can be used for commentin inline:
```groovy
println 1 /* one */ + 2 /* two */
```
### Shebang Line
As long as the `groovy` command is available on your `PATH`, you can add a shebang line to your Groovy scripts so that you can execute your script directly. Here's an example:
```groovy
#!/usr/bin/env groovy
println "Hello"
```
If the script above was in a file called `test.groovy` you would be able to execute it by running `./test.groovy`.
## Variables
Variables are of course very commonly used, across all programming languages.
In Groovy, you can create variables with an implicit, fixed type, or by using the `def` keyword or by explicitly giving it a type such as `String`.
```groovy
def myString = "This variable does not have a fixed type"
String myOtherString = "This variable has a fixed type"
```
Variables that have been declared using the `def` keyword can have different types assigned to it at run time.
For example a variable created using `def` that starts out as a `String` type, could then have an `Array` type assigned to it later on:
```groovy
def myString = "My String"
myString = ["My", "String", "Variable", "Is", "Now", "An", "Array"]
```
