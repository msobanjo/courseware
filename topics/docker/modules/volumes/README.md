# Volumes

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Managing volumes](#managing-volumes)
	- [Creating a volume](#creating-a-volume)
	- [List volumes](#list-volumes)
	- [Remove volume](#remove-volume)
	- [Inspecting volumes](#inspecting-volumes)
- [Mounting volumes](#mounting-volumes)
	- [--volume Flag](#volume-flag)
	- [--mount Flag](#mount-flag)
- [Volume Drivers](#volume-drivers)
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

## Volume Drivers

Whilst we won't be getting hands on with volume drivers here, they are definitely worth knowing about for future reference. 
When you do a listing for all the existing volumes, you might have noticed a **driver column** called **local**. 
This basically means that the volume is stored on the host machine. 
You may at some point want to develop a solution where the volume can be stored on a remote host or in a cloud storage solution perhaps. 
Plugins will allow you run different drivers to attach volumes to remote places like NFS servers or cloud storage.

## Tasks

This exercise will get you to create and manage volumes in Docker. 
You will be able to see that data can be persisted after a container is destroyed and how a single volume can be used across multiple containers at the same time. 
NGINX will serve as another good tool demonstrate this, we will create a simple webpage for NGINX to serve and store it on the volume. 
If the NGINX container is stopped and removed, when it is created again the same webpage will be served. 
If another NGINX server is created with the volume, the same webpage will be accessible from that instance of NGINX as well.

**Create a new directory**

Create a new directory called `docker_volumes`, execute the following command for this:

`mkdir docker_volumes`

Change the directory by executing:

`cd docker_volumes`

**Creating a volume**

Create a new volume called `webpage`, the command to do this is:

```shell 
docker volume create webpage
```

**Create an NGINX Container**

Create an NGINX container, expose port **80**, mount the `webpage` volume to **/usr/share/nginx/html**, execute the following command:

```shell 
docker run -d -p 80:80 --name nginx --volume webpage:/usr/share/nginx/html nginx
```

**Create a Webpage**

Let’s make a change to the default NGINX home page, so it is our page. 
You will need to connect to the container that you created and edit the index.html file, replacing the entire contents with our one. 
For that however we need a text editor such as vim or nano. 
The latest NGINX Docker image is based on Debian so you can use the apt package manager to install one of these.

Install dependencies for text editor:

`docker exec -it nginx apt update`

`docker exec -it nginx apt install -y nano`

Open the index.html file with a nano text editor by executing:

`docker exec -it nginx nano /usr/share/nginx/html/index.html`

Place the following into the file, use **SHIFT + INSERT**:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>NGINX</title>
</head>
<body>
       <h3>index.html file stored in a Docker Volume</h3>
</body>
</html>
``` 

**Destroy and recreate the container**

Stop the container

```shell 
docker stop nginx
```

Remove the container
```shell 
docker rm nginx
```

**Recreate the container**

Recreate the container, expose port **80**, mount the `webpage` volume to **/usr/share/nginx/html**, execute the following command:

```shell 
docker run -d -p 80:80 --name nginx --volume webpage:/usr/share/nginx/html nginx
```

As you can see the webpage is still the same as it's coming from the volume rather than the default NGINX page like you would have expected.

**Start Another NGINX Container**

Create another NGINX container using the same volume configurations and publish it to a different port on your host, when you connect to that instance of NGINX you will see your index.html there as well.

```shell 
docker run -d -p 81:80 --name nginx2 --volume webpage:/usr/share/nginx/html nginx
```

**Make a Change to the Webpage**

Connect to the second NGINX container that you created, install a text editor and make a change to the **/usr/share/nginx/html/index.html** file inside the "<h3>" tags. 
The changes you make should be reflected on both of the containers when you make a HTTP request to them.

Install dependencies for text editor:

`docker exec -it nginx2 apt update`

`docker exec -it nginx2 apt install -y nano`

Open the index.html file with a nano text editor by executing:

`docker exec -it nginx2 nano /usr/share/nginx/html/index.html`

Place the following into the file, use **SHIFT + INSERT**:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>NGINX</title>
</head>
<body>
       <h3>Updated file shown on both containers</h3>
</body>
</html>
``` 

**Stop and remove container**

Stop the containers:

```shell 
docker stop nginx nginx2
```

Remove containers:

```shell
docker rm nginx nginx2
```

**Remove NGINX image**

Remove the NGINX image:

`docker rmi nginx`
