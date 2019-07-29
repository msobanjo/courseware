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
## String Interpolation (GStrings)
String interpolation can be used to get the value of variables into a string easily, in Groovy these are known as GStrings.
The syntax is to include the variable reference within `${}` inside of a literal string:
```groovy
def name = "bob"
println "Hello, my name is ${name}"
```
This doesn't stop at variables, you can also make function calls which return a string to interpolate into the literal string.
```groovy
def getName() {
    "Bob"
}
println "Hello, ${getName()}"
```
## Optional Parenthesis
### Overview
In an attempt to make code more readable, with Groovy you have the choice of omitting parenthesis if you choose to.
For exmaple on function calls, you can omit parenthesis:
```groovy
// calling a function like in java
System.out.println("Hello")
// and the "groovy" way...
println "Hello"
```
### When you need parenthesis
One example of a time that you will need a set of parenthesis is when you are calling a function with no parameters.
We need to include parenthesis here or else Groovy will think that you are trying to access a property, not a function.
```groovy
// accessing a property
println person.name
// accessing a function
println person.getName()
```
### Omitting Parenthesis with Named Parameters
Named parameters can be used whilst ommitting parenthesis:
```groovy
myObject.myFunction param1: "First Parameter", param2: "Second Parameter"
```
## Tasks
Here are some tasks to try out some of the syntax dicussed above.
For any of the tasks where you are writing code, please add them to a `groovy-syntax.groovy` file in this folder.
### Commenting
Create a comment at the top of the file which contains the following:
```text
  ___  ____   __    __   _  _  _  _    ____  _  _  __ _  ____  __   _  _
 / __)(  _ \ /  \  /  \ / )( \( \/ )  / ___)( \/ )(  ( \(_  _)/ _\ ( \/ )
( (_ \ )   /(  O )(  O )\ \/ / )  /   \___ \ )  / /    /  )( /    \ )  (
 \___/(__\_) \__/  \__/  \__/ (__/    (____/(__/  \_)__) (__)\_/\_/(_/\_)
 ```
<details>
<summary>Show Solution</summary>
The easiest way to implement this is by using a multi-line comment:

```groovy
/*
  ___  ____   __    __   _  _  _  _    ____  _  _  __ _  ____  __   _  _
 / __)(  _ \ /  \  /  \ / )( \( \/ )  / ___)( \/ )(  ( \(_  _)/ _\ ( \/ )
( (_ \ )   /(  O )(  O )\ \/ / )  /   \___ \ )  / /    /  )( /    \ )  (
 \___/(__\_) \__/  \__/  \__/ (__/    (____/(__/  \_)__) (__)\_/\_/(_/\_)
 */
```

</details>

<!--
- commenting (applied)
- println hello world or something
- string interpolation
    - working example
    - provide output, ask to code it using example as reference
- optional parenthesis
    - example for ommitted paranthesis
    - ask them to build another example using this one as a reference
-->


[Go Back](../)
