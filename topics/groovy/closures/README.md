# Groovy Closures
## Overview
A closure in Groovy is an open, anonymous, block of code that can take arguments, return a value and be assigned to a variable.  A closure may reference variables declared in its surrounding scope.  In opposition to the formal definition of a closure, Closure in the Groovy language can also contain free variables which are defined outside of its surrounding scope.
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
### Implicit `it` Parameter
If you define a closure without parameters, it can still take a single parameter that will stored in a variable called `it` implicitly:
```groovy
def justAnotherClosure = {
    println "Value of it: ${it}"
}
justAnotherClosure "test"
```
## Closure as Parameter
Because closures are just stored as variables, they can be passed to other functions and closures as such:
```groovy
def myClosure = {
    println "Hello from myClosure"
}

void myFunction(exec) {
    exec()
}

myFunction myClosure

// Hello from myClosure
```
### `each` Function Example
We can pass a closure to the each function which will execute the closure for each element in the array:
```groovy
def students = ["bob", "jay", "shafeeq", "dev"]
students.each {
    println it
}
```

### `find` Function Example
The find function can be used to select an element from an array, all we have to do is pass it a closure that returns a boolean value, the the boolean value is true, then that element will be returned:
```groovy
def students = ["bob", "jay", "shafeeq", "dev"]

def numberOne = students.find {
    it.equals "shafeeq"
}

println numberOne
```
