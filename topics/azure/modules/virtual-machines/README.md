# Virtual Machines

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Images](#images)
- [Why VMs?](#why-vms)
- [Demo](#demo)
	- [Linux VM](#linux-vm)
	- [Windows VM](#windows-vm)
- [Connecting to the VMs](#connecting-to-the-vms)
	- [Linux](#linux)
	- [Windows](#windows)
- [Task](#task)

<!--TOC_END-->
## Overview

Azure offer the Azure Virtual Machine service, allowing you to create both Linux and Windows **V**irtual **M**achines (VMs).

These VMs can range in size from extra small (shared CPU cores, 768mb memory) to extra large (8 CPU cores, 14gb memory), and are priced accordingly.

## Images

Images are files that emulate an actual computer, and these are, in essence, what a VM is! 

As far as an end user is concerned, a VM feels and acts like a real computer.

Azure Virtual Machine service uses images to specify which version of Linux or Windows is on a created VM.

For Azure, they have data centres all over the world with huge physical servers in. 

When a user requests a VM with a certain image, Azure packages that request up and uses their physical hardware to serve up the image to the user.

More advanced users can create custom images that can be used on multiple VMs. For example, you can create an image with your application on it and use this image on multiple VMs without having to configuring the environment in full again.  

## Why VMs?

VMs are great because they aren't limited by the physical hardware you have, or can afford.

You rent a certain amount of power from Azure, paying a fraction of the price it would cost to get physical hardware with an equivalent power output.

You can also have a VM running for only as long as you need it, which, again, can save costs.

If you buy physical hardware and then suddenly don't need that amount of power, you are simply stuck with it. Even if you have a good warranty, you would have to return it, which is a hassle!

Once you are done with an Azure VM, you can simply delete it and you only pay for what you have used.

## Demo

In this module, we will be using the Azure Portal to create both a Linux and Windows VM.

The first thing is to create a new resource group, which we can do by clicking the hamburger menu in the top left corner and choosing "Resource groups":

![RG](https://i.imgur.com/sQW6O8U.png)

Then, we can click "+Add":

![RG2](https://i.imgur.com/iyE2TTe.png)

Here, we can name the resource group and pick a location to have it in:

![RG3](https://i.imgur.com/A02i9WX.png)

Lastly, we will click "Review & Create" and then "Create" to create the resource group:

![RG4](https://i.imgur.com/zMF2A9R.png)

### Linux VM

For this, we need to first go to the hamburger menu again, but this time click "Virtual machines":

![VM1](https://i.imgur.com/Uvuqos2.png)

Then, we click "+Add":

![VM2](https://i.imgur.com/OfmBFNZ.png)

We will need to choose our new resource group from the drop down menu, give the machine a name and pick a region for it to be deployed into.

The image can be "Ubuntu Server 18.04 LTS", and the Size can be "Standard D2s v3":

![VM3](https://i.imgur.com/bkcXpvp.png)

We need to choose "password" for authentication type, and create a username and password. 

We also need to ensure that Port 22 is open, so we can SSH into the machine later (this should be checked by default):

![VM4](https://i.imgur.com/CrgA3WK.png)

After clicking "Create", our Linux VM is created!

### Windows VM

A Windows VM is created almost exactly the same as the Linux one above. 

However, we need to choose the "Windows Server 2019 Datacenter" image this time:

![VM5](https://i.imgur.com/7UE81Ar.png)

And ensure that port 3389 is open (again, this should be by default):

![VM6](https://i.imgur.com/7sAZ7HS.png)

And once we click "Create", our Windows VM will be created!

## Connecting to the VMs

### Linux

We need to go to our Resource Group, which can be found by opening the hamrburger menu and choosing "Resource group". Then, we need to click on the correct Resource Group to see the following:

![VM7](https://i.imgur.com/woBgc1g.png)

This shows both our Linux and Windows VMs. If we click on our Linux VM, we get the following:

![VM8](https://i.imgur.com/sBWIdC7.png)

We need to click "connect" and then copy the command under "Login using VM local account":

![VM9](https://i.imgur.com/sBWIdC7.png)

![VM10](https://i.imgur.com/Yz0x1uq.png)

Then we need to go to our Windows CMD prompt, or Linux Terminal and paste the information in. 

Once this is done, we will be prompted to type "yes" and enter the password we set previously:

![VM11](https://i.imgur.com/ZkXmXUu.png)

We are now connected to our Linux machine.

### Windows

For the Windows VM, we can do the same steps as above to get to the "Connect to virtual machine" blade:

![VM12](https://i.imgur.com/Bd6Avzq.png)

From here, we need to click "Download RDP file". 

Once this is downloaded, we can double click the file, and, when prompted, click "Connect":

![VM13](https://i.imgur.com/L2Dud6Q.png)

From here, we put the credentials in we configured earlier, and click "OK":

![VM14](https://i.imgur.com/b7hwy0E.png)

If prompted, we need to click "yes" to start up the VMs Graphical User Interface, so we can interact with the machine:

![VM15](https://i.imgur.com/kOHxlud.png)

## Cleaning Up

To clean up, go back to the Resource Group page, click your resource group you used for this module, and then choose "Delete".

Once you type the name of the resource group to confirm deletion, this will be deleted along with everything inside of it.

## Task

Now it is your turn to create and connect to a Linux and Windows VM:

1. Create a Linux VM from the Azure Portal
2. Create a Windows VM from the Azure Portal
3. Connect to the Linux VM via SSH
4. Connect to the Windows VM via RDP
