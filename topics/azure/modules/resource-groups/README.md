# Resource Groups

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Resource Groups on the Portal](#resource-groups-on-the-portal)
- [Resource Groups on the CLI](#resource-groups-on-the-cli)
- [Cleaning Up](#cleaning-up)
	- [Portal](#portal)
	- [CLI](#cli)
- [Remember](#remember)
- [Task](#task)

<!--TOC_END-->
## Overview

When you provision a resource on Microsoft Azure, it needs to reside inside a **resource group**.

These resources are usually linked in some way, for example they are all a part of the same project.

Resource groups provide a way to monitor, control access and manage billing for a collection of resources. 

Grouping resources in this way allows policies to be set at the group level, meaning they are inherited by all resources in that group.

## Resource Groups on the Portal

To create a new resource group from the portal, we will firstly need to click the hamburger menu in the top left and choose "Resource groups":

![RG1](https://i.imgur.com/sQW6O8U.png)

Here, we can see any Resource Groups we currently have, and also have the option to click "+Add" to create a new one:

![RG2](https://i.imgur.com/iyE2TTe.png)

In the "Basics" tab, we need to pick the Subscription we want to use to create this group, give the group a name and choose a region to deploy it into:

![RG3](https://i.imgur.com/A02i9WX.png)

Once this is done, we can click "Next: Tags".

On the "Tags" tab, we can add **optional** tags to the group. 

These are especially useful to specify things such as the cost centre these resources fall under for the business, or which team the resources in this group belong to:

![RG4](https://i.imgur.com/78ypwnq.png)

After this, we can click "Next: Review + create".

The next screen will validate your configuration and confirm that it adheres to Azure's standards for the creation of a resource group:

![RG5](https://i.imgur.com/zMF2A9R.png)

We can now click "Create" to create the resource group.

This will take a small amount of time, but, once it is done, we should be able to see the new group in our resource groups list:

![RG6](https://i.imgur.com/DETPEv8.png)

## Resource Groups on the CLI

If you are familiar with the az CLI, you can quickly create new resource groups from there.

To do this, the command is:

```powershell
az group create --name NewResourceGroup --location uksouth
```

## Cleaning Up

### Portal

To delete the group we made, we need to click on the group name from our group list:

![RG7](https://i.imgur.com/DETPEv8.png)

From here, we should see the "Delete resource group" option:

![RG8](https://i.imgur.com/AFHVa5B.png)

The last step is confirming the resource group name, and then it will be deleted:

![RG9](https://i.imgur.com/kpp6Jij.png)

### CLI

To delete a resource group from the CLI, the following command will be needed:

```powershell
az group delete --name NewResourceGroup -y
```

The `-y` flag overrides the prompt asking you to confirm deletion of the resource group.

## Remember

When you delete a resource group, everything inside it will be deleted!

This is a great way of cleaning up, but make sure you want to delete every resource inside the group before deleting it.

## Task

It's time for you to create your own resource group from the Azure Portal:

1. Navigate to the resource group page
2. Choose to add a new resource group
3. Pick the subscription you want to use for this
4. Give the group a name
5. Pick a location to deploy the resource group into
6. Add a tag for a Cost Centre (name UK-9768) to the resource group
7. Review and create the group
8. Check it is created in the resource group page
9. Delete the resource group
