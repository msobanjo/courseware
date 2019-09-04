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

<!--TOC_END-->
### Merge conflicts
Merge conflicts happen when more than one person edited a file and the line numbers that were affected are the same
. It Can also happen if someone deleted a file another person was working on.

This conflict only affects the person doing the merge, the rest of the team wouldn't be affected by it.

If the merge conflict happens, *Git* will automatically halt the merge process and mark the file or files that are
 being conflicted, it is then up to the developer to resolve them.
 
 ### Causing a merge conflict
