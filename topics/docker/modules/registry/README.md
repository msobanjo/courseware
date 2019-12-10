# Registry

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