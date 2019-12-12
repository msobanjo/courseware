# Functions

<!--TOC_START-->
## Contents
- [Overview](#overview)

<!--TOC_END-->
## Overview

Azure Functions are one of Azure's serverless computing offerings.

They are really useful for when you are only concerned about your running code, and not the underlying infrastructure it is running on.

Microsoft manages the infrastructure for you, meaning you never directly interact with a server (hence the term "**_serverless_**").

## Functions

Azure Functions are really versatile and can execute code in almost any modern programming language.

They are **event-driven**, which means they respond to an event (or a "**trigger**") such as a REST request, a timer or a message from another Azure service.

### Speed

They are designed to execute **incredibly fast**. Work can usually be completed by an Azure Function in less than a second!

### Scaling

Azure Functions **scale automatically** on demand, so they are really useful when the demand is variable.

## Cost

This model of scaling based on demand is great for saving on costs. To explain this, we should look at an example:

### Scenario

>Your app tracks sports players wearing GPS devices.
> 
> These GPS devices generate lots of data at quite a speed. To monitor this data, you have another solution in place on Azure (for example, an IoT solution)
>
> The data is only coming in whilst the players are training or playing a game

In this Scenario, we could use a more traiditonal, VM (Virtual Machine) based approach. The other Azure service monitors the data being generated and our code runs on a VM.

If we use this model, **we will incur costs even when the VM is idle**. This isn't very logical, as our code will only ever need to run when the other service is monitoring data coming in from the players' GPS units (when the players train or play a game).

The more logical approach is to use Azure Functions to run our code. The function will run after being triggered by messages from our other Azure service. Once it's ran, it will automatically deallocate resources.

This saves costs, as **we only pay for the CPU time used while our function runs** (which should take less than a second!).

## Types of Function

* **Stateless**: This is the _default_. This type of function will behave as if it has **restarted every time it responds to an event**.

* **Stateful**: These are called "_Durable Functions_". In these, a **context** is passed through the function to track prior activity.

## Task

To learn more about Azure Functions, take some time to watch [this video](https://www.youtube.com/watch?v=7ZaIJjOM8NI)
