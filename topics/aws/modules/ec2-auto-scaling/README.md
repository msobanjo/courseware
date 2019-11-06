# EC2 Auto-Scaling

Auto-scaling is cool

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

## Tasks

The aim of this task is to create a simple auto-scaling group that contains one instance, we will then be terminating the instance to represent an Application failing and watch as the system 'self-heals',

Navigate to the EC2 console from services.

Click on **Launch Configurations** in the left pane, it is below the **AUTO SCALING** heading.

Click the blue **Create launch configuration** button.

Select an AMI image to use, for the purposes of this task we will be using the Linux AMI.

Now select the size of the instance, for the purposes of this task we will be using a t2.micro.

Click the **Next: Configure details** button

Create a name for you launch configuration, for example:

```
test-launch-configuration
```

Click **Skip to review**

Click the blue **Create launch configuration**.

You do not need to worry about having a key pair to connect to this instance as we will not be interacting with the instance once it has been provisioned.

**Create an Auto Scaling group using this launch configuration**

The previous steps were setting the *template* our group will use, we next need to configure the Auto Scaling group itself, continue following the  wizard.

Give the group a name, for example:

```
test-auto-scaling-group
```

We now need to select the size of the group, starting with 1 instance is fine as we are just aiming to demonstrate a self-healing system.

Choose all the subnets from within the selected region, for Ireland for instance, there should be 3 subnets, one for each AZ.

Click **Next: Configure scaling policies**.

Click **Review**.

At this point you should review the group you are creating, when you have finished reviewing it, click **Create Auto Scaling Group**.

Click **Close**.

You are returned to the **Auto Scaling Group** Dashboard, here you can view information about the group you have just created.  For now however, click **Instances** in the menu to the left.

You will see that a new instance has appeared and will be *intialising*, wait until it has completed the Status Checks.

We do not need to interact with this instance at the moment, actually what we want to do is **terminate** this instance, this is to represent the instance failing.

Stay on this page and wait whilst the instance is terminated, it should take less than 1 minute.

After another 2 - 5 minutes you should see that a new instance is now *Initializing*.  The Auto-Scaling group had noticed that the first instance was no long meeting its health checks and has created a new instance to fulfil the requirement.

Navigate back to the **Auto Scaling Groups** dashboard

Select the scaling group we created.

At the bottom of this page, select the **Activity History** tab, read through the information in this tab and you will see how the Auto-Scaling Group has responded to the termination of the first instance. 

Ensure that you delete the Auto-Scaling Group and all associated instances before you continue.
