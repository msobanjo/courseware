# Bind mounts

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

Bind Mounts are a very old feature in Docker and the most basic way of sharing a file or folder between a container and the host machine. 
Compared to Volumes in Docker, they do not have a great deal of functionality. 
This doesn’t mean that they are worse by any means, sometimes you just want a file from the host machine mounted in the container, this is a nice and simple way of accomplishing that. 
Bind Mounts has good performance but you need to have the directory structure for the files and directories that you are sharing on the host in place.

There are two flags, or options that you can use with Docker for creating Bind Mounts, the **-v** and **--mount** flags. 
Which one you will use for creating a Bind Mount will dependent on a mixture of which one you prefer using and what functionality you need.

## --volume Flag

We have the **-v** or **--volume** way of creating a bind mount which takes three fields, separated by colons (**:**). 
All the fields provided must be in order. 
This example mounts a configuration file for NGINX, giving the container read only access.

Here's an example command:

```shell
docker run -d -p 80:80 --volume $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro nginx
```

### First Field

The First field you provide is the file or directory that is on the host. 
The location that you give must be the full path to it, notice in the example, we can mount a file from the same directory easily by using a command substitution of pwd. 
If the file or directory does not exist on the host when you run this command then Docker will create it for you, be aware though, if Docker creates the directory for you then it will be owned by root.

### Second Field

The location that the file or directory from the host is going to be mounted in the container. 
In the example, the default configuration for the NGINX application is being replaced.

### Options

Options are usually for access rights to the Bind Mount from within the container or platform specific requirements, for instance running on MacOS machine as opposed to Linux. 
Multiple options can be provided by  separating them with commas.

Options:
* **ro** - Only allow read access to the file or directory that has been mounted in the container.
* **rw** - Allow read and write access to the file or directory that has been mounted in the container.

Configuring SELinux Labels (-v/--volume only)

On some Linux distributions like CentOS and RHEL, Security Enhanced Linux (SELinux) is enforced which effects the file permissions when the file or folder is mounted into the container. 
By using any of these options you will be modifying the SELinux labels for the host’s file or directory.

Options:
* **z** - Indicate that the file or directory is going to be accessed by more than one container.
* **Z** - Indicate that the file or directory is going to be accessed by just one container.

## --mount flag

The mount flag is a newer option that you can use as opposed to using volume flag. 
The mount flag can actually do nearly everything that the volume flag can, apart from using the SELinux labels. 
The reason for having this flag as an option is because it is intended to be more verbose and clear about what it is accomplishing. 
Instead of having an ordered listing of options that need to be provided, the options for the mount flag are key-value pairs and comma separated in any order.

Here's an example command:

```shell
docker run -d -p 80:80 --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx
```

The mount flag tends to be the preferred flag one because of how clear it is to understand, as you can see from the example above.

Mount flag options:

* **source** - The file or directory on the host to create a bind mount from. When using the mount flag, if the file or directory doesn’t exist on the host then Docker will throw an error.
* **target** - The File or directory that is going to be mounted inside the container.
* **destination** - Appears to have the same functionality as the target option.
* **type** - Mount is also a tool for mounting volumes in docker, the type option allows us to specify that we want to use Bind Mounts, as opposed to volumes.
* **readonly** - Only allow read access to the file or directory that has been mounted in the container. 
It is Read/Write by default.

## Tasks


