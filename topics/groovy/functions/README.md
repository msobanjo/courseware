# Groovy Functions
## Basic Usage
Functions can be defined by declaring a type to return, like `String` or specifying `void`, meaning that the function wont return anything and then including `() {}` after the function name:
```groovy
def myFunction() {
    // does lots of cool stuff
}
```
## Return Values
### No value (void)
To create a function that isn't going to return a value, the void keyword must be used:
```groovy
void myFunction() {
    // Do not return any values
}
```
### Returning a Type
You can specify a return types for functions as well:
```groovy
String myStringFunction() {
    // returning a string value
    return "Some String"
}
Account myAccountFunction() {
    // returning a new account project
    return new Account()
}
```
### Return Keyword
The return keyword is commonly used for specifying values to be returned from a function however this keyword can be omitted if you choose to do so:
```groovy
String withReturnKeyword() {
    return "String Example"
}
String withoutReturnKeyword() {
    "String Example"
}
```
## Parameters
We can provide parameters to functions with or without types:
```groovy
def functionWithoutTypes(param1, param2) {
    println "${param1}, ${param2}"
}
def functionWithTypes(String param1, String param2) {
    println "${param1}, ${param2}"
}
```
