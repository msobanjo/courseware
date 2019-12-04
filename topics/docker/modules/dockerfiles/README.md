# Dockerfiles

<!--TOC_START-->
## Contents
- [Overview](#overview)

<!--TOC_END-->
## Overview

We can build our own *Docker Images* by using *Dockerfiles*. 

A **Dockerfile** contains a list of instructions for creating a new image, effectively a build script for *Docker Images*. 

Each instruction in a *Dockerfile* creates intermediate images and stores them, like a cache. 

For instance, if there are four instructions in a *Dockerfile* and your build fails on the fourth,  when you attempt to build the image again, the build can start on step four, because the previous steps have already been built.

An easier way to think of intermediate images is like a layer of a cake. 

You don't just end up making a cake in one go, you make it layer by layer, similarly *Dockerfiles* allow you to make a final image by doing it in a similar way where you will have multiple layers until the final image is ready.

## Creating Dockerfile

*Dockerfile* is a file with the name of `Dockerfile` with no extension.

It doesn't require specific permissions, but depending on your systems configuration it might require you to elevate it's privileges.

## Executing Dockerfile 

In order to execute the *Dockerfile* the command for this is:

`docker build .`

This command needs to be executed when the terminals working directory is the same as where the *Dockerfile* is.

Additionally if you want to execute a *Dockerfile* from a directory that is not your terminals working directory you can do it through the `-f` flag.

The command for it would be:

`docker build -f /path/to/file .`

You can also specify an *Image Name*, *Tag* & *Repository*, here's an example of it:

`docker build -t myapp:latest .`

## Tasks