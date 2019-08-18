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

Where ``branchname`` would be the name of the branch you wish to get the history of.

