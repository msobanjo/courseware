# Dockerfile instructions

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

Dockerfiles are built up of instructions that are run in order, they help us to build and configure Docker Images in very specific ways. 

The format is as follows:

```dockerfile
# comment
INSTRUCTION arguments
```

- It’s convention to have the instruction in capital letters
- Any Dockerfile that you create must start with a FROM instruction
- Any line starting with a # is considered as a comment

## FROM

The **FROM** instruction creates a new build stage. 

Except for the *ARG* instruction (which will be covered later), this instruction must be at the beginning of a *Dockerfile*. 

It is used to set the *Base Image* that the *Docker image* is going to be created from.

Here's an example of setting the base image to *java 8*:

```dockerfile
FROM java:8
```

The *FROM* instruction can appear multiple times in a Dockerfile. 

This can be for creating multiple images or for using previous build stages as dependencies for others. 

For instance, one image can be created for compiling the application and creating an executable, the other image for running the application.

## RUN

We use the RUN instruction to run shell commands on the intermediate containers. 

The default shell that’s used is /bin/sh.

Here's an example of *RUN*:

```dockerfile
RUN apt update
```

This instruction lends itself well to how *Docker Images* are built because the build progress of the image after each command you run is effectively saved, so if one fails then the build can start where it was last successful.

## CMD

To provide a default execution for a container, or main process, we use the *CMD* instruction. 

There can only be one of these in a *Dockerfile*, if there is more than one then the last one in the *Dockerfile* will be the only one that takes effect.

Here's an example of *CMD*:
```dockerfile
CMD ["/bin/ping", "google.com"]
```

*CMD* can be used in conjunction with the *ENTRYPOINT* (will be covered later) instruction to set the arguments for a command. 

This is ideal if you plan on running the same executable every time you run a container, as it allows you to have default arguments which can be altered by the *docker run* command if necessary.

## LABEL

**Metadata** can be added to a *Docker image* by using this instruction. 

*Metadata* for *Docker Images* follows a key-value pair format.

Here's an example of *LABEL*:

```dockerfile
LABEL version="1.0"
LABEL description="A Docker Image."
```

*Images* can have more than one *LABEL*, you can view the labels for an image by using the `docker inspect` command. 

Keep in mind that you will need to have the image in your local registry to be able to inspect it.

Here's an example of inspecting labels for an image:

```dockerfile
docker inspect nginx
```

*Metadata* can have many uses cases, such as setting versions, descriptions etc for access by other tools. 

If you ever feel the need to add some extra information to a *Docker Image* that isn’t already available then labels are good solution for it.

## EXPOSE

This is purely an **informative instruction** for Docker to show which port the application is going to be listening on, it doesn’t *expose* or *open* a port from the container to the host, that’s what publishing (**-p**) is for in the `docker run` command. 

By default Docker will assume that the protocol is *TCP*, but *UDP* can be specified if that’s the protocol that your application is going to be using.

Here's an example of exposing port 80 in *TCP* protocol:

```dockerfile
EXPOSE 80
```

Here's an example of exposing port 80 in *UDP* protocol:

```dockerfile
EXPOSE 80/udp
```

If you want to expose both *TCP* and *UDP* then you can just do that over two lines:

```dockerfile
EXPOSE 80/tcp
EXPOSE 80/udp
```

## ENV

Setting *environment variables* can be done with **ENV**. 

Once you have created an *environment variable* in the *Dockerfile*, subsequent commands afterwards will be running in the same environment so they will be able to access it. 

The whole string beyond the space after the key will be taken as the value.

Here's an example of using *ENV*:

```dockerfile
ENV JENKINS_HOME /jenkins-home
```

After creating the image, *environment variables* can be viewed with `docker inspect` command.

## ADD

New Files, Directories and even remote file URLs can be added into the filesystem of the *Docker Image* by providing the source and destination.

Here are some examples of using add:

```dockerfile
# add a local file such as an application, relative to the context
ADD ./app.py /opt/application/app.py

# add an entire folder
ADD . /opt/application/

# add a remote file from a URL
ADD https://remote-server/file.txt /remote-file.txt

# add a tar file (relative to the context) and extract the contents to a folder
ADD ./application.tar.gz /opt/application
```

A common use case for needing to add a file to the images file system is for the application itself that you are going to want to run in the container. 

*ADD* is very similar to the *COPY* command.

## COPY

Files and Directories can be copied into the image file system with this instruction, sounds familiar right? 

So which one to use, *ADD* or *COPY*? 

The answer is fairly subjective however most of the time you will want to be using *COPY* just because it is more explicit about what it is doing, copying a file or directory.

The main difference between *ADD* and *COPY* is that *ADD* can add files from two more sources, a URL and a extracting a TAR file to a destination. 

Unless you want to extract a TAR file you may as well use *COPY*.

*COPY* works just the same as *ADD*, by providing a source and a destination for copying files.

Here's an example of *COPY*:

```dockerfile
# copy a local file such as an application, relative to the context
COPY ./app.py /opt/application/app.py

# copy an entire folder
COPY . /opt/application/
```



## Tasks
