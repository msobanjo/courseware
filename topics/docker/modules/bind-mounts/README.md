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

## Tasks
