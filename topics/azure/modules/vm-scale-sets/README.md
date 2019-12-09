# Virtual Machine Scale Sets

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Why use them?](#why-use-them)
- [Monitoring Scale Sets](#monitoring-scale-sets)
- [Demo](#demo)
	- [Load Balancer](#load-balancer)
	- [VM Scale Set](#vm-scale-set)
- [Task](#task)
	- [Cleaning up](#cleaning-up)

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

### Load Balancer

The first thing we need to do is create a **Load Balancer**:

1. In the search box at the top of the home page, we can search "Load Balancer" and click on it when it pops up

2. We'll click **+Add** in the top left

3. In the **Basics** tab of the **Create a load balancer** page, we can enter or select the following:

* Subscription - our sunscription
* Resource Group - we will create a new one called "**scalesetRG**" for this demo
* Name - we'll type "**myLoadBalancer**"
* Region - we can select **uk south**
* Type - we will select **Public**
* SKU - we'll select **Standard**
* Public IP Address - we'll select **Create new**
Public IP address name - we can type "**myPip**" for this
* Assignment - we'll choose **Static**
* Availability Zone - we will select **Zone-redundant**

![loadbalancer](https://i.imgur.com/MF2NxHz.png)

![loadbalancer2](https://i.imgur.com/d1i5df4.png)

4. We will then select **Review + create**

5. After it passes validation, we can click **Create**

### VM Scale Set

Now, we can look at creating a Virtual machine scale set:

1. First, we type "Scale set" in the search bar and select "Virtual machine scale sets"

2. We click **+Add** in the top left

3. In the **Basics** tab, we will choose the correct subscription

4. We'll create a new resource group named "**vmScaleSetRG**"

5. The name of our scale set can be "**myScaleSet**", and for the location, we can choose **UK South**.

6. For **Orchestrator**, we can leave the default value of **ScaleSet VMs**

7. We will choose **Ubuntu Server 18.04 LTS** as the image

8. Then we can choose **Password**, and go ahead and create a username and password we want to use

9. We then select **Next**:

![SSbasics](https://i.imgur.com/mEy3sL0.png)
![SSbasics2](https://i.imgur.com/OZwj8J6.png)

10. The we can select **Next** until we get to the **Networking** page

11. Here, under **Load balancing**, we'll select **Yes**

12. In **Load balancing options**, we can select **Azure Load balancer**

13. In **Select a load balancer**, we'll choose the load balancer that we created earlier

14. For **Select backend pool**, we'll choose **Create new**, type "myBackendPool" and then click **Create**

![SSnetworking](https://i.imgur.com/IVMvxd5.png)
![SSnetworking2](https://i.imgur.com/rX1GJFo.png)

15. We'll select **Review + create**

16. Once validation is passed, we can select **Create**

We've just deployed a load balanced Azure Virtual Machine Scale Set!

## Task

Now, it's your turn!

Use the demo above to:

1. Create a load balancer

2. Create a Virtual Machine Scale Set using the load balancer from step 1

### Cleaning up

To clean up, use the hamburger menu at the top left of the Portal, and choose **Resource groups**.

Here, you will see the resource groups you created.

If you click on each one, and then choose **Delete resource group**, you will be able to delete the resource group and therefore all the resources inside of it.
