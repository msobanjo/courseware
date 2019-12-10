# Networking

## Overview

We can utilise networking in Docker when we would like to have multiple containers working together. 

For example a frontend and backend application with a database. 

The frontend application needs to be able to communicate with the backend and the backend application needs to be able to communicate with the database.

We can have these three different applications running in separate containers. 

This is because if they were all in the same container, then everything would need to be redeployed whenever any of the three have been updated.



## Tasks