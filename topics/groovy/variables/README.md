# Variables
## Basic Usage
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

## Tasks
### Define and Access
View and then execute the `variable-definition.groovy` script in this folder.
Then edit the script to define a `message` variable that has the value `"how are you?"`, add this to the `println` function call. 

<details><summary>Show Solution</summary>
#### Solution
```python
print("hello world!")
```
</details>
