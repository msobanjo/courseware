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
## Calling Functions

## Parameters
### Creating Functions with Parameters
We can provide parameters to functions with or without types:
```groovy
def functionWithoutTypes(param1, param2) {
    println "${param1}, ${param2}"
}
def functionWithTypes(String param1, String param2) {
    println "${param1}, ${param2}"
}
```
### Calling Functions with Parameters

## Tasks
Please create any files for these tasks in this folder.
### Create Some Basic Functions
#### Current User Message Function
Create a file called `current-user-message.groovy`.
The following function can take a string parameter, a message, and then add the current user's name to the message provided, this string will then be returned.
Add the function and function call to `current-user-message.groovy` and execute the file to see it working.
```groovy
String formatMessageForCurrentUser(String message) {
    "Hi ${System.getenv("USER")}, ${message}"
}
println formatMessageForCurrentUser("how are you?")
```
#### Addition Function
Try to create another function that can add two numbers together and return the value as an `int` type.
Create this in a file called `addition-function.groovy`
<details>
<summary>Show Solution</summary>

```groovy
int sumOf(int firstNumber, int secondNumber) {
    firstNumber + secondNumber
}
println sumOf(1, 2)
```

</details>
