# Cloning

## Overview
`git clone` allows the cloning of a repository to a newly created directory. Additionally the command creates remote
tracking branches for the ones in the repository and checks out the initial branch which is the current active branch.

Once the cloning is done `git fetch` can be executed without additional arguments to get updates for the remote 
branches. Similarly a `git pull` without arguments would merge the remote branch into the current branch.

### Cloning a repository
In order to clone a repository there are a couple of prerequisites:
* Git installed on the machine
* URL of the repository

To get the URL of the repository you would need to find a repository you would like to have on your machine. Once you 
you found the repository click on the *Clone or Download* and copy the URL, make sure you copy it with the *.git* 
ending. </br>
![Fork >](https://imgur.com/hkzKOvt.png)
![Fork >](https://imgur.com/hOQZaFu.png)

Open a terminal and navigate to the directory where you want to have the project saved. You can create a directory 
*projects* or use and existing one. In the example below, a new directory is created. </br>
![Fork >](https://imgur.com/3b4KMCR.png)

After the cloning has been completed, change directory and run `git branch` to check that the active branch has been 
checked out. </br>
![Fork >](https://imgur.com/UEAW1EN.png)

## Tasks

### Task 1

* Create a new repository
    * Initialise the repository with a README.md file
* Clone the repository to desired location
* Check that an active branch has been checked out
