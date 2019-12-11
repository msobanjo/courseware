# Registry

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Image Naming for Registries](#image-naming-for-registries)
- [Creating Your Own Registry](#creating-your-own-registry)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

In Docker, a **Registry** is a server side application that can store Docker Images for us. 
This Registries can be accessed remotely, meaning that Docker images can be downloaded from any location. 
When you run a container with an image that you didn’t build, NGINX for instance, the image will be downloaded from a *Registry* first. 
The default registry that Docker images will be pulled down from is *docker.io*, also known as *Docker Hub*.

## Image Naming for Registries

You may have noticed from using Docker in the past, an image name prefixed with *docker.io*, such as *docker.io/nginx:latest*. 
This is referring to the registry that it has been pulled from and where it  would also be pushed to if you wanted to upload the image.

## Creating Your Own Registry

Having your own Registry deployed can contribute really well to your own CI/CD setup. 
Images can be stored and retrieved quickly as well as having the benefit of not having your images uploaded and stored to someone else’s registry. 
Registries also have the ability to execute Web Hooks which could trigger a deployment for instance when an image has been successfully uploaded to the registry.

There is a prebuilt image that we can use to deploy, so getting a Registry working for a test environment is really as simple as executing a docker run command. 
The Registry service listens on port 5000.

Here's the command for it:

`docker run -d -p 5000:5000 --name registry registry`

## Tasks

<details>

<summary>Expand guided task</summary>

This exercise will take you through creating your own registry that you can push and pull images to.

**Create the registry**

Start by creating the Registry and make sure that the port 5000 has been published. 

The command for it is:

`docker run -d -p 5000:5000 --name registry registry`

**Upload an Image to the Registry**

To upload an image to the Registry, we first need one that has been tagged appropriately.
 
Start by pulling an NGINX down.

`docker pull nginx:latest`

Re-tag it to be **localhost:5000/my/nginx**.

`docker tag nginx:latest localhost:5000/my/nginx`

Use the `docker push` command to push the image to the *Registry* that you have created.

`docker push localhost:5000/my/nginx`

**Download an image from the Registry**

Delete the NGINX images, both yours **localhost:5000/my/nginx** and the official **nginx** image. 

The command for this is:

`docker rmi nginx:latest localhost:5000/my/nginx`

Now we can run a docker pull command to prove that the image has been stored in the Registry that we deployed, remember to pull you docker image as **localhost:5000/my/nginx**.

The command for this is:

`docker pull localhost:5000/my/nginx`

Check that the image has been pulled by executing:

`docker images`

**Clean up**

Stop registry container:

`docker stop registry`

Remove registry container:

`docker rm registry`

Remove images:

`docker rm registry localhost:5000/my/nginx`

</details>

<details>

<summary>Expand individual task</summary>

Stop and remove all containers, remove all the images.

Try to create a shell script that can pull down a project from GitHub, build the Docker image and push it to the registry.

</details>
