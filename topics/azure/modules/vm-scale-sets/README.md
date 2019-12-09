# Virtual Machine Scale Sets

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Why use them?](#why-use-them)
- [Monitoring Scale Sets](#monitoring-scale-sets)
- [Demo](#demo)
	- [Load Balancer](#load-balancer)
	- [VM Scale Set](#vm-scale-set)
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

1. In the search box at the top of the home page, search "Load Balancer" and click on it when it pops up

2. Click **+Add** in the top left

3. In the **Basics** tab of the **Create a load balancer** page, enter or select the following:

* Subscription - your sunscription
* Resource Group - we will create a new one called "**scalesetRG**" for this demo
* Name - type "**myLoadBalancer**"
* Region - select **uk south**
* Type - select **Public**
* SKU - select **Standard**
* Public IP Address - select **Create new**
Public IP address name - type "**myPip**"
* Assignment - Static
* Availability Zone - select Zone-redundant

![loadbalancer](https://i.imgur.com/MF2NxHz.png)

![loadbalancer2](https://i.imgur.com/d1i5df4.png)

4. Select **Review + create**

5. After it passes validation, click **Create**

### VM Scale Set

Now, we can look at creating a Virtual machine scale set:

1. Type "Scale set" in the search bar and select "Virtual machine scale sets"

2. In the **Basics** tab, choose the correct subscription

3. Create a new resource group named "**vmScaleSetRG**"

4. The name of your scale set can be "**myScaleSet**"

5. Leave the default value of **ScaleSet VMs** for **Orchestrator**

6. Choose **Ubuntu Server 18.04 LTS** as the image

7. Choose **Password**, and go ahead and create a username and password you want to use

8. Select **Next**:

![SSbasics]

9. Select **Next** again, top get to the **Networking** page

10. Here, under **Load balancing**, select **Yes**

11. In **Load balancing options**, select **Azure Load balancer**

12. In **Select a load balancer**, choose the load balancer that you created earlier

13. For **Select backend pool**, choose **Create new**, type "myBackendPool" and then click **Create**

![SSnetworking]

14. Select **Review + create**

15. Once validation is passed, select **Create**

Congratulations! You've just deployed a load balanced Azure Virtual Machine Scale Set!

## Cleaning up
