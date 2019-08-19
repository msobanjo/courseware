# Reverting

## Reviewing history of a repository

The best way to view the history is by using the following command.

``git log``

This command will show the history of all commit for the current branch with the output including: date, commit message
 and the SHA-1 identifying hash. There are also has additional flags that make this command easier to use. 

``git log --oneline``

Using ``--oneline`` flag addition simplifies the output into one line per commit.

``git log --branches=*``

By using the ``--branches=*`` flag we are making Git return the history of all commits for all the branches. The asterisk
acts as a wildcard including all the branches. To get the data for a specific branch the log command would need to be
used like this:

``git log branchname``

Where ``branchname`` would be the name of the branch you wish to get the history of. If you aren't sure of what are the 
existing branch names you can make use of the commad ``git branch -a`` 

## Reverting to an older commit with checkout

Once you know the commit to which you want to return ``git checkout`` can be used to load your chosen commits state.
Usually git would have the HEAD pointing to master or some other local branch, although this changes once you invoke
the ``git checkout`` command. From then the HEAD points directly to the commit and this is called `detached HEAD`.

Let's assume that your ``git log --oneline`` looks similar to this:

```
875f31e (HEAD -> master) fourth commit
483856a third commit
2dd011d second commit
bcabb84 first commit
```

Now we want to revert back to the third commit which has the SHA-1 of ``483856a``. The checkout command would look like this:

``git checkout 483856a``

After this command was executed the repository would go into the ``detached HEAD`` state, we wouldn't be on a branch any more.
Any new commits you would make afterwards would be orphaned when we would change branches to create a new branch.
Orphaned commits get deleted by Git's garbage collector, which runs in specific intervals and destroys all orphaned commits.
In order to avoid orphaned commits to be destroyed we need to make sure we are on a branch, and this can be done from
the ``detached HEAD`` state by executing ``git branch -b newbranchname``. Now there would be a new history for the repositories
timeline without the ``fourth commit``. Now work can go on just like the fourth commit never happened. This solution comes
with an issue, where if the previous branch is required, let's say it was the ``master`` then this particular strategy wouldn't work.

## Reverting to a previous commit with revert

Let's assume that your ``git log --oneline`` looks similar to this:
             
 ```
 875f31e (HEAD -> master) fourth commit
 483856a third commit
 2dd011d second commit
 bcabb84 first commit
 ```

By executing 

``git revert HEAD``

Git will then create a new commit which will do the opposite of the previous commit. You can also use revert to go back
to a specific SHA-1 that's not the last commit. The history will still contain the fourth commit, but it's changes will be
undone. Using ``revert`` allows the usage of the same branch and is considered the better revertion solution.

## Reverting with reset

We will work with the same ``git log`` history like in the previous examples. By invoking:

``git reset --hard 483856a``

This command will return the state to the selected commit. The difference between the previous solutions is that the Git
history will no longer contain the fourth commit and work can resume just like the ``fourth commit`` never happened.
This way has the smallest effect on history. Resetting local changes poses no complication, although using it for a shared
remote repository will increase the complexity.

If the reset happened to a commit that is already shared on Git with others, and we tried to push some changes afterwards,
git would throw an error as it would think that our local git history is not up to date. In these scenarios it's more
appropriate to use ```git revert``` strategy.

## Summary
* ``log`` checking on the commit hisotry
* ``checkout`` moving around and reviewing commit history
* ``revert`` shared work undoing
* ``reset`` local work undoing

## Tasks

### Task 1

* Create a folder called "tmp", after the task we'll delete the files therefore this will make it easier to delete them
* Within the folder open up git bash
* Initialise the folder as a git repository
* Create a new text file, call it test.txt
* Place some text within the file
* Stage the file and commit
* Repeat the previous two steps until you have done 4-5 commits
* Now check the git log history for the branch you are on
* Try out the additional flags for viewing the git log history
* Pick one of the previous commits to which you would like to revert the changes back and keep note of the SHA-1 which
will look similar to this ``e367834``
* Now use the revert command to go back to your chosen commit
* Create a new branch with your chosen name
* Delete the previous branch
* Once you're done with the task, remove the tmp folder and all of the files inside it

Continue on working like the changes by the commits we reverted back never happened.



### Task 2

* Create a folder called "tmp", after the task we'll delete the files therefore this will make it easier to delete them
* Within the folder open up git bash
* Initialise the folder as a git repository
* Create a new text file, call it test.txt
* Place some text within the file
* Stage the file and commit
* Repeat the previous two steps until you have done 4-5 commits
* Now check the git log history for the branch you are on
* Try out the additional flags for viewing the git log history
* Pick one of the previous commits to which you would like to revert the changes back and keep note of the SHA-1 which
will look similar to this ``e367834``
* Now use the reset command and do a hard reset to your chosen commit
* Check on the git commit log history whether the commit we chose to reset are part of the history

Continue on working on the same branch like the commits we chosen to revert never happened. Keep in mind this should
only be used for the local changes reset, not when you have already pushed your work up.

#### Task Summary
* Learned how to check git commit history
* Learned how to revert and reset back to a previous commit
* Learned about the differences between the revert and reset and the use cases for them