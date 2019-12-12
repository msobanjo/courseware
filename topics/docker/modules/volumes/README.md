# Volumes

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

**Volumes** are another way in Docker to persist data from the container. 
Unlike *Bind Mounts*, *Volumes* are managed by Docker. 
Bind Mounts rely on a host's directory structure. 
Volumes are a newer addition to Docker compared Bind Mounts, because of this they have more functionality and benefits. 
The main benefit about using volumes is that they are easier to manage. 
Bind Mounts are great for just plugging one file into one container, but when you want to start sharing files or directories across multiple containers, then volumes becomes a much more manageable solution.

## Managing volumes

Before even creating a container you can create and manage volumes in Docker.

### Creating a volume

Just provide the name to create a volume in Docker.

```shell
docker volume create my-volume
```

### List volumes

We can view a list of all the volumes available on the Docker host.

```shell
docker volume ls
```

### Remove volume

Provide the name of the volumes to delete it.

```shell 
docker volume rm my-volume
```

### Inspecting volumes

The inspect command can be used to see more details about a volume in Docker.

```shell 
docker volume inspect my-volume
```

## Mounting volumes

Just like with Bind Mounts, you can choose to use either the volume or mount flags. 
Mounting the volumes into containers is very similar to creating Bind Mounts, except for the source we are pointing to the volume that we want to be mounted not a location on the host file system. Options for mounting volumes as read only are available, just like with Bind Mounts.

When specifying a volume name with any of these commands, if the volumes doesn’t exist then Docker will create one for you. 
This is a handy feature as it allows us to skip a step if need be, but make sure to spell your volume name correctly because Docker won’t care if you don’t.

###  --volume Flag

When using the volume flag we need to provide the name of the volume that is going to be mounted and the location which the volume is going to be mounted in the container.

```shelll
docker run --volume my-volume:/usr/share/nginx/html
```

### --mount Flag

With the mount flag provide the volume name and the destination on the container to mount the volume.

```shell 
docker run --mount source=my-volume,destination=/usr/share/nginx/html
```

## Tasks
