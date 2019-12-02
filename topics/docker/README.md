# Docker

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Containerisation](#containerisation)
- [Containers vs Virtual Machines](#containers-vs-virtual-machines)
- [Linux installation](#linux-installation)
	- [Using Docker Commands Without Sudo on Linux](#using-docker-commands-without-sudo-on-linux)
- [Windows & macOS Installation](#windows--macos-installation)
- [Try out Docker](#try-out-docker)
- [Modules](#modules)

<!--TOC_END-->
## Overview

**Docker** is an open source tool that benefits both developers and system administrators, which is why it has become so popular as a "**DevOps**" tool. 

Developers should be able to focus on developing code, without worrying about configuring their environments, **Docker** provides a solution for this.
 
It uses containers to keep environments consistent; whether the code is running on production setup or a developer’s laptop.

Though Docker is the most popular container engine, there are several alternatives which are worth mentioning:
- **rkt**
- **LXD**
- **Linux VServer**
- **Windows Containers**

## Containerisation

Just like with real-life shipping containers, developers use **containers** for holding or transporting code.

Effectively, **containerisation** is a much more lightweight alternative to **virtual machines**, whilst still having the benefits of *encapsulating* (isolating from everything else) an application in its own operating environment.

## Containers vs Virtual Machines
There are several reasons why developers might use containers over virtual machines:
**Containers:**
- Containers use the same kernel (the core of the operating system) that the host operating system is using
- Resources are shared between containers where it is possible
- Extremely fast startup time

**Virtual Machines:**
- Virtual machines must emulate an entire computer to support an operating system
- There is complete separation between machines
- Far more resources are used to isolate the hosted application

![Containers VS VM's](https://imgur.com/gYBBO9w.jpg)

## Linux installation

To install *Docker* on *Linux* we can use a remote script for installing *Docker* on most distributions easily.

`
curl https://get.docker.com | sudo bash
`

### Using Docker Commands Without Sudo on Linux

On *Linux*, to be able to run *Docker* commands without having to prefix them all with `sudo`, we can add users to the *docker* group.

Once you have added your user to the *docker* group, ensure that you restart your shell session so that the change takes effect:

```shell script
# add yourself to the docker group, the remote script suggested above will
# have already created the docker group for you
sudo usermod -aG docker $(whoami)
```

## Windows & macOS Installation

*Docker* can be installed on *Windows (exe)* and *Mac (dmg)* through this link: [here](https://www.docker.com/products/docker-desktop)

For this method you will be required to create a *Docker* account.

## Try out Docker

Give *Docker* a go by running a **hello world container**. 

Use a `docker run` command to start the *container*.

 You will see *Docker* download the image, then run it.
 
  The script in the *hello-world container* will create an output which describes what just happened.

Run the following *docker* command (ignore the comment that starts with `#`):
```shell script
# --rm flag removes the container when it exits or when the daemon exits, whichever happens first
docker run --rm hello-world
```

You should see an output like this:
```text
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which it to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
<!--MODULES_START-->
## Modules
- [Images](./modules/images)
<!--MODULES_END-->
