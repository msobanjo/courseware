# Dockerfiles

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Creating Dockerfile](#creating-dockerfile)
- [Executing Dockerfile](#executing-dockerfile)
- [Tasks](#tasks)

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

This exercise will get you to take the *NGINX Docker Image* and change the default *index.html* file that is served. 

This change will be packed into your own *Docker Image* that you can run and view the changes for yourself.

Please complete the tasks in the order they appear, otherwise will not work.

Additionally, please use a bash terminal.

**Create a new directory *dockerfile_exercises***

<details>

<summary><b>Show solution</b></summary>

In order to create a new folder with the name `dockerfile_exercises` execute the following command:

`mkdir dockerfile_exercises`

After creating the directory, change your current directory to the new one by executing:

`cd dockerfile_exercises`

</details>

**Make a Dockerfile**

<details>

<summary><b>Show solution</b></summary>

Set your terminals working directory to the newly created `dockerfile_exercises`

Then execute the following command to create a new file:

`touch Dockerfile` 

To make sure file is there, run the following command:

`ls`

Place the following contents within the `Dockerfile`:

```dockerfile
FROM nginx:latest
RUN printf "My Custom NGINX Image\n" > /usr/share/nginx/html/index.html
```

</details>

**Build the image from Dockerfile**

<details>

<summary><b>Show solution</b></summary>

Make sure your terminals working directory is set to `dockerfile_exercises`

We'll give the new image name `ournginx`, and the command to build from *Dockerfile* and give it a suitable name is:

`docker build -t ournginx .`

</details>

**Run *ournginx* image on port 80 **

<details>

<summary><b>Show solution</b></summary>

The command to run the image and map the port 80 is:

`docker run -d -p 80:80 --name nginx ournginx`

</details>

**Test the image is running correctly**

<details>

<summary><b>Show solution</b></summary>

In order to test the image is running correctly, navigate your browser to `localhost:80` if you're using docker on your machine.

You should see the following:

![nginx page](https://imgur.com/BV4buK0.jpg)

If you're using a VM in the cloud, execute the following command:

`curl localhost:80`

You should see the following image:

![nginx page](https://imgur.com/zOswi3z.jpg)

</details>

**Stop and remove the container**

<details>

<summary><b>Show solution</b></summary>

To stop the container execute:

`docker stop nginx`

To remove container execute:

`docker rm nginx`

</details>

**Remove the *ournginx* image**

<details>

<summary><b>Show solution</b></summary>

To remove image execute:

`docker rmi ournginx`

</details>

**Your own web page**

Try to create an image that will deploy your own static website, create an **index.html** file of your website in the same folder as the *Dockerfile*:

<details>

<summary><b>Show solution</b></summary>

Create a new directory by executing:

`mkdir new_dockerfile`

Change to the new directory by executing:

`cd new_dockerfile`

Create your *index.html* file by executing:

`touch index.html`

Place the following contents within the *index.html*:

```html
<html>
    <body>
        <h3>My very own website!</h3>
    </body>
</html>
```

Create *Dockerfile* by executing:

`touch Dockerfile`

Place the following contents into the *Dockerfile*:
```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/
``` 

Build the image by executing:

`docker build -t myimage .`

Run the image by executing:

`docker run -d -p 80:80 --name mycontainer myimage`

Stop the container by executing:

`docker stop mycontainer`

Remove the container by executing:

`docker rm mycontainer`

Remove the images by executing:

`docker rmi myimage nginx`

</details>
