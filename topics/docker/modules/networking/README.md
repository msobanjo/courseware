# Networking

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

### Overlay Networks

This is where Docker allows you to scale your application, overlay networks allows network connectivity over multiple hosts. 

Your applications deployed on different hosts will be able to communicate to each other, this kind of networking appears when using Docker Swarm, a container orchestration tool but can also be used for standalone containers.

### Macvlan Networks

Some legacy applications or tools which monitor network traffic expect to be on a physical network, which Docker networks are definitely not. 

Macvlan networks are for these kinds of applications.




## Tasks