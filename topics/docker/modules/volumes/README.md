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



## Tasks
