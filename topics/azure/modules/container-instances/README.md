# Container Instances

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Why ACI?](#why-aci)
- [Using ACI](#using-aci)
- [Using exec](#using-exec)
- [Logs](#logs)
- [The Portal](#the-portal)
- [Cleaning Up](#cleaning-up)
- [Task](#task)

<!--TOC_END-->
## Overview

**A**zure **C**ontainer **I**nstances (**ACI**) allow you to focus on designing and building your applications instead of managing the infrastructure that runs them.

**ACI** are especially useful when you want to run a container without orchestration, which usually means you don't need to scale the application or utilise load balancing.

## Why ACI?

The advantage of ACI over utlising your own containers is the managed infrastructure.

Typically, if you wanted to run an application in a container, you would need to either:

1. Use your local machine
2. Spin up a virtual machine (VM), install Docker and run the container

Both of these ways mean you have to manage the infrastructure yourself. 

ACI takes that away, with Microsoft managing and configuring the VM for you. You don't even see it in this entire process!

To work with ACI, all you need is a Docker image; this can either be pulled from your own DockerHub or another public registry. 

Azure actually has a container registry called **Azure Container Registry**, which you can make use of when working with ACI, if you'd prefer to use this over DockerHub.

# Using ACI

In this module, we are going to use the az CLI to work with ACI. 

We will be using a public Docker image that has the game 'Super Mario' on it.

The first thing we need to do is create a resource group:

```powershell
az group create -n mariogroup -l uksouth
```

Remember, `-n` is the shorthand flag for `--name`, which allows us to spercify the name we want to give our resource group. 

`-l` is the shorthand flag for `--location`, which allows us to specify the location we want to deploy the resource group into.

Next, we need to create the container and give it the correct image to use:

```powershell
az container create -g mariogroup -l uksouth -n mario --image jordangrindrod/mario --ip-address public --ports 8080
```

Here, we have ensured that the VM Azure spins up will have a Public IP address (`--ip-address public`) and that the application will be running on port 8080 (`--ports 8080`). 

`-g` specifies the resource group to deploy the container into, `-l` indicates the location where we want to deploy the container, `-n` is the name we want to give the container and `--image` is for specifying the image we want to use.

Once this has completed, you can run the following to see your running container and the ip address of it:

```powershell
az container list -o table
```

The `-o` flag here specifies the **output** we want to receive the information in. In this example, we have asked for the output to be in table form, which makes it much easier to read and understand the information being shown to us. Without this flag, you receive the information in json format.

After this, you can navigate to the browser and paste the ip address in, followed by `:8080`.

Have a couple of minutes playing Mario, then come back to the lesson...

## Using exec

Microsoft have leveraged Docker's `exec` command, so that you can interact with your container directly.

For example, we could have a look at our container's filesystem with the following command:

```powershell
az container exec -g mariogroup -n mario --exec-command ls
```

Here, `-g` is the resource group, `-n` is the name of the container, `--exec-command` is the command we want to run inside the container and `ls` is a Linux command that will list the contents of the current directory.

## Logs

The following command allows you to see the logs of a container instance, which can be incredibly useful for debugging (should something go wrong):

```powershell
az container logs -g mariogroup -n mario
```

Once again, `-g` here is the resource-group name and `-n` is the container name.

## The Portal

If you navigate to Container Instances in the Azure Portal, you will see your `mario` container up and running.

Metrics are automatically linked to each container instance you create, allowing you to see useful data about the instance, such as CPU usage. 

You can also view IAM, logs for each instance, add or remove tags, and much more, all from the Portal.

## Cleaning Up

To remove everything you have done in this lesson, simply run the following command:

```powershell
az group delete -n mariogroup -y
```

`-n` is needed here to specify the name of the resource group that you want to delete, and the `-y` flag is used to override the prompt asking you to confirm deletion of the resource group.

## Task

Now it is time for you to try this for yourself:

1. Create a new Resource Group:

```powershell
az group create -n games -l uksouth
```

2. Create a new container using a public Docker image:

```powershell
az container create -g games -l uksouth -n hangman --image jordangrindrod/hangman --ip-address public --ports 3000
```

3. Navigate to the IP Address, on port 3000, and check the application is up and running correctly. To get the ip address, use:

```powershell
az container list -o table
```

4. Clean up all resources used for this:

```powershell
az group delete -n games -y
```
