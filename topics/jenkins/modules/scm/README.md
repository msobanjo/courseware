<!--
{
    "prerequisites": [
        "git/remotes"
    ]
}
-->
# Source Code Management (SCM) 
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Configuration](#configuration)
	- [Multiple Repositories](#multiple-repositories)
		- [Working with Multiple Repositories](#working-with-multiple-repositories)

<!--TOC_END-->
## Overview
Source Code Management, also reffered to as Version Control, Source Control Management, SCM, or by simply refferring to a tool such as Git, plays an important role in automating project builds and deployments with Jenkins.

The most common way of using SCM in one of your jobs is by utilising the suggested GitHub plugin for Jenkins.

## Configuration
Here we can see a very simple configuration for SCM in a project.
This example will download the `master` branch from this repostory in the projects workspace:

![Jenkins SCM Configuration](https://lh3.googleusercontent.com/vy3PzZydHTEF7g1oH7J4gEURjTVcKoJVyX01E6AFqAvFAboUEMx3Uz5YK7ZwDwV4-I8EFcpad9ajdGW9ULsaYqNJZ2Wg5aonqu210kabj04GVkcOtbCDTprsDEbFLuvnnoqI-Hn75HrLgudXSG5-Og09492SI_tOxGVeGepfG2ahrQEBZViM5RAMFiu5p73tkcKAVX7nJVcyuSR8hJ4vNT1Al39j-FZ3UeUJV6t2VSC_JRGyq3_-Xn0ikgM2WXp4XJJun7No9T-ebGug1rEjlqApdy-NADc03tJQ7IHKMPG8-D6ysb_R-0AfmRTjbwv_JGqN6ylzfwP5p2EQuKYfPAYn-Uq-_Ybsnfalar2Y9X6YIz7qEjZTfw05oSZCmNw5oAKHdldzsfdRVzIq81dNsgbMPKqs7eydnJOxRprqVIPm5rIgQg2BVd8XE8LsdqeD_PqcJFx64-Vj1FUEkfeiTVMnh--WQfwjpm9Q00o7HALGVbLrGI-Iuj5L7LF-kdSeyL0HXLs3_sqBHiPp8gdb9kG9ERenP5XaAkckY62_NDhkQctAYOEWdF6QkiN431byRPUoAJvGJ0k9jpxnAIDDDaABPv4YrnXZQHsv1PR41blsWioYYgetl0r-FCnFycKEUBNwWVQ3oMpZRfXPPVeMzDcNFZrX2MyKeutS0OQ9ZNqoKUZke7h6B7IdelVHJSiuIJkh3Fa_OInkJ9Jjot7h5UcpohATWJzrsa_T6pUtLbdkGnRm=w1174-h696-no)

### Multiple Repositories
You may have noticed the `Add Repository` button which will allow us to download more than one repository at a time.

These are all downloaded into the same workspace but with different remotes setup for Git.
The last repository specified will be the one that is checked out to in the project workspace.

The first repository will have a remote set as `origin`, then for every respository added, a number will be appended.

For example, if you had 3 repositories being downloaded, the remotes would be named `origin`, `origin1`, `origin2`.

This default behaviour isn't ideal, so it's recommended that you configure the name of the remotes yourself under the `Advanced...` option and in the `Name` field for each repository that you add.
