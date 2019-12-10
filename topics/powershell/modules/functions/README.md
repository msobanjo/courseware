# Functions



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Powershell Functions](#powershell-functions)
- [Basic Functions](#basic-functions)
- [Task](#task)

<!--TOC_END-->
## Overview

Instead of copying and pasting the same code over and over again, we can use a function.
We will be learning about functions in Powershell in this module, but the concepts also translate across all programming languages.

## Powershell Functions

When you first start out with Powershell, you aren't always too concerned with things such as modularity, reusibility and "best practices".
As time goes on, you will very quickly realise that you are repeating yourself in code often.

This is where functions become really useful. Copying and pasting isn't sustainable, so instead we create small "building blocks" that can be reused.

In Powershell, there are two different types of functions: **Basic** fuctions and **Advanced** functions.

If the function only needs to carry out simple and quick tasks, such as generating a random 12-digit number and adding 12 random letters to it (maybe you are generating a password), a Basic Function would be perfect.

However, if you need the function to perform more advanced tasks, such as those that require error streams or pipeline input, you would need to use an Advanced Function.

## Basic Functions

These are the simplest form of function in Powershell. It is created or declared by using the _function_ statement, followed by a set of curly braces:

```powershell
function Hello{}
```

Although this is a viable function in Powershell, it doesn't do very much. To make it useful, we would need to add some code inside it. Let's fix this now:

```powershell
function Hello{
    Write-Host "Hello From Function"
}
```

We could then call the function in Powershell, by simply using the name of the function. In this case, the following would return `Hello From Function` to the console:

```powershell
Hello
```

This is great, but what if we wanted to pass something into the code inside the function when it's running?
This can be done by creating one, or more, parameters inside of a parameter block:

```powershell
function Hello{
    param($Name)
    Write-Host "Hello $Name!"
}
```

Here, we have created a parameter called `Name`, which can then be used in the statement in the next line of code.

To use this parameter, we need to pass it a value when we call the function:

```powershell
Hello -Name 'Bob'
```

This would return `Hello Bob!` to the console.

## Task

1. Create a Basic Function in Powershell that:

    * Takes 2 parameters: a user's name and their favourite food
    * Outputs the following message to the console, replacing the text in brackets with the parameters - `"(name)'s favourite food is (food)"`.
