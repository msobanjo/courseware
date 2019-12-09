# Virtual Machine Scale Sets

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Why use them?](#why-use-them)
- [Monitoring Scale Sets](#monitoring-scale-sets)
- [Demo](#demo)

<!--TOC_END-->
## Overview

Azure Virtual Machine Scale Sets allow you to create and manage a group of identical, load balanced **V**irtual **M**achines (VMs).

With this service, you can automatically increase or decrease the number of running VMs, in response to demand or a defined schedule.

## Why use them?

If demand for your application is high, you may need to use a load balancer to distribute traffic evenly across all the VMs in your scale set. 

Doing this increases the resiliency of the application, as it is able to easily handle surges in traffic. 

This also allows for an update, or maintenance, to be performed on one application instance (one VM in the scale set), whilst traffic is directed to other instances. 

Doing this means your application will still be available during updates and maintenance windows.

Other benefits include:

* Easy to create and manage multiple, consistant VMs
* Provides high availability and resiliency
* Allows your application to automatically scale as demand changes
* Works at a large scale

## Monitoring Scale Sets

**Azure Monitor for VMs** will automate the collection of important CPU, memory, disk and network performance counters from the VMs in your scale set. 

It also includes additional monitoring capabilities and pre-defined visualisations that help you focus on the availability and performance of your scale sets.

You can also configure an **availability test** to simulate user traffic and further verify the availability of your application.

## Demo

For this demo, we will be using the **Azure Portal**.
