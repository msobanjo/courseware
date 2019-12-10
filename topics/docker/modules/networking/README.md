# Networking

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

We can utilise networking in Docker when we would like to have multiple containers working together. 

For example a frontend and backend application with a database. 

The frontend application needs to be able to communicate with the backend and the backend application needs to be able to communicate with the database.

We can have these three different applications running in separate containers. 

This is because if they were all in the same container, then everything would need to be redeployed whenever any of the three have been updated.

## Network types

There are several different types of network drivers, for different networking purposes. 

Some are for single host solutions while others are for spreading containers across more than one host. 

The main focus for this module will be with bridge networks because overlay networks are for Docker Swarm setups and macvlan networks are for legacy applications.

### Bridged Networks

Bridged networks are for connecting multiple containers on a single host. 

You will be able to access the container with it’s private IP address. 

Mapping ports to the host needs to be done explicitly.

### Host Networks

This network type should be used when you want container application ports to map to the host automatically. 

Instead of explicitly publishing a port from a container to the host, applications that listen on a port will be available from the host on that same port. 

Be careful of ports clashing between applications when you use this.

Something to keep in mind with *host networks* is at the time of writing this host networks are only available on Linux hosts running Docker. 

If you list the networks that you have, you should see that there is one network called host. 

To get a container onto this network you can just specify the network name when connecting the container to it.

### Overlay Networks

This is where Docker allows you to scale your application, overlay networks allows network connectivity over multiple hosts. 

Your applications deployed on different hosts will be able to communicate to each other, this kind of networking appears when using Docker Swarm, a container orchestration tool but can also be used for standalone containers.

### Macvlan Networks

Some legacy applications or tools which monitor network traffic expect to be on a physical network, which Docker networks are definitely not. 

Macvlan networks are for these kinds of applications.

## Bridged Networks

There are two kinds of bridged networks, user defined and default. 

When containers are started a --link flag can be provided to link it to another container using the default bridge network. 

The default bridge is legacy method in Docker for networking and is not recommended anymore by Docker, so we shall avoid that going forward.

User defined bridged networks provide many benefits:

* **Isolation from other containers on the same host that aren’t in the same network.**
  When two containers are on the same user defined bridge network, all ports are open to each other and they can communicate freely.
* **Automatic DNS Resolution**
  When a container is put on a bridge network it will have a private IP address. 
  A DNS entry is automatically configured to this IP address which is just the container name. 
  For instance if there were two containers running, one called nginx and the other called application, and the application container had a server listening on port 8080. 
  The nginx container would be able to connect to the application running in the other container by its name (http://application:8080).
* **Connect and Disconnect Containers on the Fly.**
  You can connect and disconnect containers to a bridge network without having to stop the containers.
  
## Managing networks

### Creating a network

Containers can set to connect to a network when you are creating them by providing the **--network** flag.

When you create a network with the *docker network* command the default network type is bridged. 

To create a bridged network you need to provide the name of the new network.

Here's an example of creating a bridged network:

`docker network create my-network`

### Viewing your Docker Networks

You can view what networks you already have along with their details such as what type of network they are and the names of them.

Here's an example command:

`docker network list`

### Connect an Already Existing Container to a Network

If you have a container that exists already but you want to add it to a network without having to recreate it then you can use the network connect command, providing the network name and the container name.

Here's an example command:

`docker network connect my-network my-container`

### Disconnect a Container from a Network

Disconnecting a container from a network can be done just like when you connect an existing container to a network, provide the network name and the container name.

Here's an example command:

`docker network disconnect my-network my-container`

### Delete a Network

You can only delete a network if there are not containers connected to it otherwise you will get an error message.

`docker network rm my-network`
  
## Tasks
