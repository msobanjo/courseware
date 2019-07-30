# Groovy Closures
## Overview
A closure in Groovy is an open, anonymous, block of code that can take arguments, return a value and be assigned to a variable.
A closure may reference variables declared in its surrounding scope.
In opposition to the formal definition of a closure, Closure in the Groovy language can also contain free variables which are defined outside of its surrounding scope.
While breaking the formal concept of a closure, it offers a variety of advantages.
## Basic Usage
### Create
Here is a very simple example of a Closure:
```groovy
def simpleClosure = {
    println "Hi"
}
```
### Execute
We can execute a closure either just like we would a function by using `()` or by using the `call()` function:
```bash
def simpleClosure = {
    println "Hi"
}
// using ()
simpleClosure()
// using the call() function
simpleClosure.call()
```
### Parameters
Closures can be configured to have parameters very easily:
```groovy
// one parameter
def singleParamClosure = { param -> {
    println "${param}"
}
// two parameters
def multiParamClosure = { param1, param2, param3 -> {
    println "${param1}, ${param2}, ${param3}" 
}
```
### Implicit "it" Parameter
## Closure as Parameter
### each Function Example
### findAll Function Example

