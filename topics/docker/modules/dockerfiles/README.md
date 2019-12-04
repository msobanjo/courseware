# Dockerfiles

<!--TOC_START-->
## Contents
- [Overview](#overview)

<!--TOC_END-->
## Overview

We can build our own *Docker Images* by using *Dockerfiles*. 

A **Dockerfile** contains a list of instructions for creating a new image, effectively a build script for *Docker Images*. 

Each instruction in a Dockerfile creates intermediate images and stores them, like a cache. 

For instance, if there are four instructions in a Dockerfile and your build fails on the fourth,  when you attempt to build the image again, the build can start on step four, because the previous steps have already been built.

An easier way to think of intermediate images is like a layer of a cake. 

You don't just end up making a cake in one go, you make it layer by layer, similarly Dockerfiles allow you to make a final image by doing it in a similar way where you will have multiple layers until the final image is ready.
