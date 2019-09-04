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
8.
