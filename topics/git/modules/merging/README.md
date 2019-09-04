<!--PROPS
{
    "estTime": 30
}
-->
## Merging
Joining two or more branch histories through `git merge` incorporates changes into the current branch. This command is 
used by `git pull` to incorporate changes from a different repository as well as to merge change from one branch into 
another.

If we assume that we have a history like this and the current branch is **master** 
```
      E---F---G issue
     /
A---B---C---D master
```
By executing `git merge issue` would result in adding (E, F, G) changes into master and result in a new commit
, ending up in the following history.
```
      E---F---G issue
     /         \  
A---B---C---D---H master
```

<!--TOC_START-->
### Contents
	- [Merge conflicts](#merge-conflicts)
	- [Causing a merge conflict](#causing-a-merge-conflict)

<!--TOC_END-->
### Merge conflicts
Merge conflicts happen when more than one person edited a file and the line numbers that were affected are the same
. It Can also happen if someone deleted a file another person was working on.

This conflict only affects the person doing the merge, the rest of the team wouldn't be affected by it.

If the merge conflict happens, *Git* will automatically halt the merge process and mark the file or files that are
 being conflicted, it is then up to the developer to resolve them.
 
### Causing a merge conflict
You will now go through the steps required to cause a merge conflict.

1. Open a terminal
2. Create a new directory by executing `mkdir git-merge-conflict`
3. Change directory by executing `cd git-merge-test`
4. Initialise this directory as a git repository by executing `git init .`
5. Create a new text file *hello.txt* in the directory
6. Add some text like "hello world" to the *hello.txt* file, save and close the file
7. Now you need to make git track changes for the *hello.txt* file, execute the following command to do this `git add
 hello.txt`
8.Now you need to create a save point which is known as commit and will have the current state of the *hello.txt file, execute the following command to achieve this `git commit -m "initial commit"` </br>
![Fork >](https://imgur.com/cm8Oky3.png)

Now that you have a repository and a master branch with a file on it the next step is to create a new branch which
 will be used to cause the merge conflict.
 
1. Checkout a new branch by executing `git checkout -b new-branch`
2. Open the text file *hello.txt* and add a new line to it with text like "making a change to the file", your text
 file should now look like this:
```
hello world
making a change to the file
```
3. Let's make Git keep track of the hello.txt file to which we made the change by executing `git add hello.txt`.Now you
 need to commit again, but this time with a message that reflects the change made `git commit -m "made a change to
  hello.txt file"`. The change we made will now try to override the changes in master branch for the text file *hello.txt*.
4. A change to the text file *hello.txt* is required now before we can cause a merge conflict, let's go back to
 *master* branch by executing the following command `git checkout master`
5. Open the text file *hello.txt* and add a new line to it with text like "making a bigger change", your
 text file on master should now look like this:
```
hello world
making a bigger change
```
The *hello.txt* on branch *new-branch* should look like this:
```
hello world
making a change to the file
```
Let's commit the change we made to the *hello,.txt* file to the master branch, first execute `git add hello.txt` then
 execute `git commit -m "modified hello.txt file"`. </br>
![Fork >](https://imgur.com/y6GoKCn.png) 
Now what we want is to merge changes from *new-branch* to *master* branch, but can Git figure out which version of
 the second line to use? The answer is that it can't, this will cause a merge conflict and the developer will be responsible for resolving it.
6. Let's cause the actual merge conflict by executing the following command `git merge new-branch` you should get
 output about merge conflict similar to this:</br>
![Fork >](https://imgur.com/yFzxuUD.png)
7. Let's take a look at the contents of the *hello.txt* file now, it should look similar to this:
```
hello world
<<<<<<< HEAD
making a bigger change
=======
making a change to the file
>>>>>>> new-branch
```
What is visible is that the first line `hello world` doesn't have a conflict, but there is a conflict between the
 second lines of the *master* and *new-branch* branches.
