# Registry

## Overview

In Docker, a **Registry** is a server side application that can store Docker Images for us. 
This Registries can be accessed remotely, meaning that Docker images can be downloaded from any location. 
When you run a container with an image that you didn’t build, NGINX for instance, the image will be downloaded from a *Registry* first. 
The default registry that Docker images will be pulled down from is *docker.io*, also known as *Docker Hub*.



## Tasks