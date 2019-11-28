# Images

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Image layers](#image-layers)
	- [Practical benefits](#practical-benefits)
- [Image properties](#image-properties)
	- [Repository](#repository)
	- [Tag](#tag)
	- [ID](#id)
- [Managing images](#managing-images)
	- [Searching](#searching)
	- [Downloading](#downloading)
	- [Renaming](#renaming)
	- [Uploading](#uploading)
	- [Deleting](#deleting)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

A *Docker image** is a read only file that is effectively a *snapshot* (the state of a system at a particular point in time) of a *container*. 

For instance if you could take a *snapshot* of the current state of the computer you are using, move it to another computer and run it so that its in exactly the same state as when you took the *snapshot*, then this is a similar concept to how *Docker images* work. 

## Image layers

*Docker images* are composed of layers. 

Because *images* are read only meaning that you can’t change them, only create new ones, **image layers** become a very useful feature for building new *images*. 

Multiple steps are often taken to get an *image* configured to a state we want it to be in before installing an application on it, wouldn’t it be nice if all we had to do is install the application on an already configured image? 

This is what the **layers** allow us to do.

### Practical benefits

The benefit of *image layers* is that you can build off other Docker images. 

Let’s say that we wanted to run a *Java application*, we could take an existing *image* that has a *Java environment* already configured and all we have to do is copy our application onto the *image* and run it. 

Each *layer* is a file that can be downloaded individually and reused for other *images*, this means that the same Java "base image" can be used for multiple applications which is very efficient.

## Image properties

Before managing *Docker images* it is useful to understand what different **attributes** they have so that they can be properly utilised when managing *images*.

The properties discussed below can be found when you run the `docker images` command.

### Repository

The location and name of the image, which follows the format of: **<host>/<author>/<application>**

- **Host** - *remote registry* that the *image* is stored in. 
If it is left empty then the *local registry* will first be checked, if the *image* is not there then the *default* remote registry (**docker.io**) will be consulted for the *image*.
- **Author** - who created the *image*, for example if you are trying to upload *images* to Docker Hub (**docker.io**) then this value will be your *Docker Hub **username***.
- **Application** - name of the *application*, *service* or *solution* that has been built and configured inside of the *docker image*.

### Tag

Tagging *images* is a way of differentiating between them, more commonly known as versioning. 
If no *tag* is provided when referencing an *image* then the default ***latest** tag* is used.

### ID

ID is an identifier that is *unique* for every *image* thus making it the a reliable property when referencing the *image*

## Managing images

As there are many images in the Docker hub repository, we need ways of managing them. 

You will learn about the core commands needed to manage them.

### Searching

One of the most useful parts about *Docker* is the contributions from the *community* and *developers*. 

There are already images that exist for most application services and base images for more popular languages.

This is an example of command signature:

**docker search <image>:<tag>**

Now if you wanted to search for *Java 8* the command to execute would be:

`
docker search java:8
`

### Downloading

Before an *image* can be used, it must be present in the *local registry*, the `docker pull` command can accomplish this. 

Note that the `docker run` command *downloads* the *image* as well as running it if it does not exist locally.

This is an example of command signature:

**docker pull <image>:<tag>**

If you wanted to download the image to have it in the *local repository* the command would be:

`docker pull java:8`

### Renaming

**Name** of the image effects where it will be uploaded and how it will be referenced, there are many reasons you might want to do this, the *docker tag* command effectively *renames* the *image*.

This is an example of command signature:

**docker tag <old-image>:<old-tag> <new-image>:<new-tag>**

If you wanted to rename the Java 8 image and prepend it with your username then the command would look like:

`docker tag java:8 apples1992/java:8`

### Uploading

*Docker images* that you have created can also be **uploaded** using the `docker push` command, just provide the *image name*.

This is an example of command signature:

**docker push <image>:<tag>**

If you wanted to upload an image the command would look like this:

`docker push myusername/java:8`

Although for the previous command to work there are two conditions that need to be satisfied first:
- you need to be **logged in* to *Docker hub* within the terminal from which you would be executing the `docker push` command, the command for logging in is:

    `docker login --username=yourdockerhubusername --email=youremail@company.com`

- the *image* needs to have your *username* **prepended** to the *images tag*

If your *Docker hub username* was **apples1992** then the *image tag* for your version of *Java:8 image* should look like **apples1992/Java:8**.

Then the command to push the *image* would be:

`docker push apples1992/Java:8` 

### Deleting

An important part of managing *Docker images* is **deleting** them, although *Docker* is efficient at storing them, depending on what *images* you are building they can take up quite a lot of space on your machine.

This is an example of command signature:

**docker rmi <image>:<tag>**

If you wanted to delete the Java 8 image then the command for it would be:

`docker rmi java:8`

## Tasks

Try completing the following tasks, there will be solutions provided, although you might need to change some of the values to make them work for you.

**Find the latest official *Java* image**

<details>

<summary><b>Show solution</b></summary>

`docker search java`

Notice in the image below, **java** is on line four. 

Additionally, there is a *column* called **OFFICIAL** and **java** has a status **OK** under it.

This means that this is the official *java* version you are looking for.

![docker search](https://imgur.com/MtTvXAe.jpg)

</details>

**Download the latest official *Java* image**

<details>

<summary><b>Show solution</b></summary>

`docker pull java`

To check that you have downloaded the image, execute the following command:

`docker images`

![docker download java](https://imgur.com/NWAu1Fx.jpg)

</details>

**Delete the *java* image**

<details>

<summary><b>Show solution</b></summary>

`docker rmi java`

To check that you have removed the image, execute the following command:

`docker images`

![docker delete](https://imgur.com/tdXHSgB.jpg)

</details>

**Download the *java 8* image**

<details>

<summary><b>Show solution</b></summary>

`docker pull java:8`

To check that you have downloaded the image, execute the following command:

`docker images`

![docker download java 8](https://imgur.com/RQXTrQ1.jpg)

</details>

**Rename the Java 8 Docker image so that it is prefixed with your *Docker hub* name**

<details>

<summary><b>Show solution</b></summary>

`docker tag java:8 tvaidotas/java:8`

To check that you have renamed the image, execute the following command:

`docker images`

![docker tag](https://imgur.com/zrGPuK5.jpg)

</details>

**Log in to *Docker hub* with your username**

<details>

<summary><b>Show solution</b></summary>

**REPLACE *tvaidotas* with your username**

`docker login --username=tvaidotas`

**You will be prompted for your password, make sure you enter it correctly**

You will get a message saying that you're logged in successfully if you entered correct **username** and **password**.

![docker login](https://imgur.com/boDz2Fq.jpg)

</details>
