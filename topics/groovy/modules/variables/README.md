# Variables
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
## Basic Usage
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
Variables are of course very commonly used, across all programming languages.
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
In Groovy, you can create variables with an implicit, fixed type, or by using the `def` keyword or by explicitly giving it a type such as `String`.
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
```groovy
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
def myString = "This variable does not have a fixed type"
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
String myOtherString = "This variable has a fixed type"
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
```
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
Variables that have been declared using the `def` keyword can have different types assigned to it at run time.
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
For example a variable created using `def` that starts out as a `String` type, could then have an `Array` type assigned to it later on:
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
```groovy
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
def myString = "My String"
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
myString = ["My", "String", "Variable", "Is", "Now", "An", "Array"]
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->
```
<!--TOC_START-->
- Basic Usage
- Tasks
	- Define and Access Variables

<!--TOC_END-->

## Tasks
### Define and Access Variables
Here is some Groovy code that stores the current users name in a variable and then prints out "Hello" and the users name:
```groovy
# get the current user on the system
String name = System.getenv("USER")
# say hello to the user
println "Hello ${name}"
```
Using the above as a reference, create a Groovy script that will also print a message for the user using a variable called `message` that is a `String` type.
The output should look something like this if the user was called Bob:
```text
Hi Bob, how are you?
```

<details>
<summary>Show Solution</summary>

```groovy
# get the current user on the system
String name = System.getenv("USER")
# set the message variable
String message = "how are you?"
# say hello to the user, with the message as well
println "Hello ${name}, ${message}"
```

</details>







