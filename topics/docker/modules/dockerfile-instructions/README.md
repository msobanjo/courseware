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



## Tasks
