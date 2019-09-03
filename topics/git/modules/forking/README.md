# Forking

<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Proposing a change](#proposing-a-change)
- [Your idea](#your-idea)
- [Forking a repository](#forking-a-repository)
- [Updating forked repository from original](#updating-forked-repository-from-original)
- [Summary](#summary)

<!--TOC_END-->
# Overview

In layman terms forking is creating a copy of an existing repository under your account. 

Forking a repository allows to freely experiment with the existing code base without the fear of breaking the project.
Another use case is to contribute to the project by adding additional functionality. 

## Proposing a change

In a scenario where you are using someones project and you find a bug, instead of submitting an issue about it you can try 
fixing it. The steps would be:
1. Fork the repository
2. Create a new branch
3. Fix the issue
4. Submit a pull request to the owner of the original project

If the owner approves your fix, your work should then be merged into the original repository.

## Your idea 

If a project is under public license that allows you to freely use it, you could use the project as a starting point for
your own take on the project. In a scenario where you find a web application that you like, it's under the public license
you can then fork the project and add any additional functionality and it will be yours to freely use or distribute.

## Forking a repository

You will now for a remote repository, set up upstream to get updates from the original and propose a change to the owner

1. Ask your trainer to create a repository with some files on it
2. Navigate to the repository your trainer created
3. Make sure you're logged in to your github account
4. Click on "Fork", this will then create a copy of the repository under your account <br />
![Fork >](https://imgur.com/X0bNG7K.png)
5. You will be redirected to your accounts version of the repository
6. Click on the green button "Clone or download" and copy the URL <br />
![Fork >](https://imgur.com/hkzKOvt.png)
7. Open a Bash terminal in the location you want to clone your project
8. Run `git clone URL`, replace the URL with the repository URL you copied in the previous step
9. Change directory to the project you just cloned
10. Run the following command to see that you have cloned the correct repository: `git remote -v`. You should get a 
similar output for `fetch` and `push` but the URL will be pointing to your repository <br />
![Fork >](https://imgur.com/FOASYQ2.png)

## Updating forked repository from original

Now you will set up your local project to receive updates from the original repository. This is required so that when
the owner of the original repository add new functionality, bug fixes etc. you would have the ability to get them as well.

1. Open your Bash terminal in the root directory of your project, you should be able to see that you're on the master 
branch. Next you want to execute `git remote -v` to make sure that the upstream to original repository is not set up yet.
You should see similar output to this. <br />
![Fork >](https://imgur.com/lqS0EUr.png)
2. Navigate your browser to the original git repository and copy the repository URL. You can do this by clicking on the
green button "Clone or download" and copy the URL <br />
![Fork >](https://imgur.com/hkzKOvt.png)
3. In your Bash terminal execute the following command, but replace the URL with the one you just copied
`git remote add upstream URL` 
4. Next you want to check that it has been successfully added, execute the following command `git remote -v`, it should 
look similar to this: <br />
![Fork >](https://imgur.com/KpAfGaP.png)
5. Now you will pull the changes from original repository into yours, do this by executing the following command in your
Bash terminal `git fetch upstream` and then depending if there are new changes or not you will see different outputs, like: <br />
![Fork >](https://imgur.com/L7S2JB1.png)
6. You want to update the master branch therefore we will merge the *upstream/master* into the *local origin/master*, do this
by executing the following command: `git merge upstream/master` keep in mind there may be merge conflicts that you will
 need to resolve. If you have resolved the merge conflicts or if there were none you should *push* to update your 
 *origin/master* branch. <br />
![Fork >](https://imgur.com/OYejtWC.png)

## Summary

In this module you have learned: 
* What is *forking*
* What are the use cases for *forking*
* How to fork a repository
* How to pull the changes into forked repository from the original repository
