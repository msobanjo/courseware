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



## Tasks
