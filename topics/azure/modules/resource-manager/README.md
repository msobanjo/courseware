# Resource Manager

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Benefits](#benefits)

<!--TOC_END-->
## Overview

**A**zure **R**esource **M**anager (ARM) is the deployment and management service in Azure.

It provides a management layer that enables you to create, update and delete resources in your Azure subscription.

## The Portal

For this module, we will look at ARM through the Azure Portal. 

The Azure Portal uses ARM templates to create resources, which are **JSON files** describing how a resource is configured, but this is done under the hood.

More advanced users can create their own ARM templates, to repeatedly and consistently deploy a number of resources, configured in a particular way.

## Benefits of ARM

* Allows you to create and manage infrastructure through declarative templates, rather than scripts

* Deploy, manage and monitor resources as a group, instead of individually

* Apply access control to all resources in a resource group

* Apply tags to resources to logically organise them

* View the costs for a group of resources sharing the same tag, which can allow clarity when dealing with billing.

## Working with ARM to manage resources

The first thing we are going to do is create a Resource Group with some resources inside it:

![RM1](https://i.imgur.com/cCNFA9z.png)

This group has two Virtual Machines (VMs) in it.

If we wanted, we could now manage these VMs as a group, rather than individual instances. 

To delete both VMs (including their disks, networks, etc) we would simply delete the resource group. 

Inside the group, we can also filter the resources by Tag, which allows us a more granular management of resources. 

In this case, "Jay" owns some resources inside the group and "Bob" owns the others. 

If we want to see just the resources that "Jay" owns, we could click "Add filter":

![RM2](https://i.imgur.com/vNma9k8.png)

Then we can choose "Owner" and use the checkbox to pick "Jay". This will show us that "Jay" is only tagged as the owner of VM1:

![RM3](https://i.imgur.com/cbQqKCu.png)

As well as this, we could have filtered resources by location or type. 

There are many ways you can use the management tools offered by ARM, and this is just one example of how to organise resources effectively when working in a team.

## Other Features

ARM provides a suite of tools to automate standard operations for each resource or resource group.

You can:

* Turn off a VM at scheduled times to save costs

* Configure disaster recovery to create a back- up of a resource group and all its resources

* Monitor the resources as a group, which is particularly useful if the resource group houses an application

and much more!

## Task

In this task, you are going to leverage a publicly available ARM template to create a web app:

1. Create a new Resource Group in the Azure Portal:

    Click the hamburger menu (top left) and choose "Resource groups". Click "+Add", name the resources group, pick a location and click "Create".

2. Go to this [Azure ARM Template](https://azure.microsoft.com/en-gb/resources/templates/101-webapp-basic-windows/).

3. Click on "Deploying to Azure".

4. Choose the resource group from step 1.

5. Configure the Web App name to anything you wish, but make it **unique!**

6. Agree to the terms and conditions and click "Purchase".

7. After a few minutes, you should see that, inside your resource group, a web application has been deployed just from one template!

8. To clean up, click "Delete resource group" from inside the resource group screen.

