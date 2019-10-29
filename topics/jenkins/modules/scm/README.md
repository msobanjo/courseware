<!--
{
    "prerequisites": [
        "git/remotes"
    ]
}
-->

# Source Code Management (SCM) 

<!--TOC_START-->
## Contents
	- [Contents](#contents)
- [Overview](#overview)
- [Repositories](#repositories)
	- [Multiple Repositories](#multiple-repositories)
	- [Branches to Build](#branches-to-build)
- [Triggering Builds from SCM Changes](#triggering-builds-from-scm-changes)
	- [Poll SCM](#poll-scm)
		- [CRON](#cron)
	- [Web Hooks](#web-hooks)
- [Demo](#demo)
	- [Setup Git Repositories](#setup-git-repositories)
	- [Upload the Provided Code](#upload-the-provided-code)
	- [Create the Jenkins Jobs](#create-the-jenkins-jobs)
	- [Webhook Configuration](#webhook-configuration)
	- [Push a New Change](#push-a-new-change)

<!--TOC_END-->
## Overview
Source Code Management, also reffered to as Version Control, Source Control Management, SCM, or by simply refferring to a tool such as Git, plays an important role in automating project builds and deployments with Jenkins.

The most common way of using SCM in one of your jobs is by utilising the suggested GitHub plugin for Jenkins.

## Repositories
Here we can see a very simple configuration for SCM in a project.
This example will download the `master` branch from this repostory in the projects workspace:

![Jenkins SCM Configuration](https://lh3.googleusercontent.com/vy3PzZydHTEF7g1oH7J4gEURjTVcKoJVyX01E6AFqAvFAboUEMx3Uz5YK7ZwDwV4-I8EFcpad9ajdGW9ULsaYqNJZ2Wg5aonqu210kabj04GVkcOtbCDTprsDEbFLuvnnoqI-Hn75HrLgudXSG5-Og09492SI_tOxGVeGepfG2ahrQEBZViM5RAMFiu5p73tkcKAVX7nJVcyuSR8hJ4vNT1Al39j-FZ3UeUJV6t2VSC_JRGyq3_-Xn0ikgM2WXp4XJJun7No9T-ebGug1rEjlqApdy-NADc03tJQ7IHKMPG8-D6ysb_R-0AfmRTjbwv_JGqN6ylzfwP5p2EQuKYfPAYn-Uq-_Ybsnfalar2Y9X6YIz7qEjZTfw05oSZCmNw5oAKHdldzsfdRVzIq81dNsgbMPKqs7eydnJOxRprqVIPm5rIgQg2BVd8XE8LsdqeD_PqcJFx64-Vj1FUEkfeiTVMnh--WQfwjpm9Q00o7HALGVbLrGI-Iuj5L7LF-kdSeyL0HXLs3_sqBHiPp8gdb9kG9ERenP5XaAkckY62_NDhkQctAYOEWdF6QkiN431byRPUoAJvGJ0k9jpxnAIDDDaABPv4YrnXZQHsv1PR41blsWioYYgetl0r-FCnFycKEUBNwWVQ3oMpZRfXPPVeMzDcNFZrX2MyKeutS0OQ9ZNqoKUZke7h6B7IdelVHJSiuIJkh3Fa_OInkJ9Jjot7h5UcpohATWJzrsa_T6pUtLbdkGnRm=w1174-h696-no)

### Multiple Repositories
You may have noticed the `Add Repository` button which will allow us to download more than one repository at a time.

You would want to use this feature when more than one repository must be downloaded and built at the same time, for instance if one repository had a build dependency on another.
Otherwise it would be best to just have each repository built in another jenkins job so that each application component that you have can be built separately.

These are all downloaded into the same workspace but with different remotes setup for Git.
The last repository specified will be the one that is checked out to in the project workspace.

The first repository will have a remote set as `origin`, then for every repository added, a number will be appended.

For example, if you had 3 repositories being downloaded, the remotes would be named `origin`, `origin1`, `origin2`.

This default behavior isn't ideal, so it's recommended that you configure the name of the remotes yourself under the `Advanced...` option and in the `Name` field for each repository that you add.

### Branches to Build 
After specifying which repositories that you want to fetch, you can also choose which branches that you would like to build.
There are some quite complex different ways of checking out code that you can do here but usually being simple is better; there isn't a great deal of reasons to use anything other than the default value here (`*/master`) on simple projects.

If you would like to be able to build different branches easily then you could use a string parameter by entering something like `*/${BRANCH}` into the `Branch Specifier` field.

## Triggering Builds from SCM Changes
Jenkins jobs can be automatically triggered by changes in SCM.
When some changes have been push to a repository, the job can be triggered automatically by this.

There are two main ways to trigger builds in this way, depending on your situation:
- Poll SCM:
    This method is preferred if your instance of Jenkins is **not** accessible from the internet.
- Web Hooks (Preferred)
    Web Hooks are the preferred way of triggering build automatically from SCM if your instance of Jenkins can be accessed from the internet.

### Poll SCM
Poll SCM works by checking for changes on a schedule.
For the given schedule, Jenkins will make a request to your Git repository to check if there has been any changes.

This can be configured by selecting `Poll SCM` in the `Build Triggers` section.
A `Schedule` text box will then appear for you to configure the schedule.

#### CRON
The format for configuring the schedule is cron time format.
If you haven't heard of this before you can head over to [crontab guru](https://crontab.guru/#*_*_*_*_*); this site will give you a change to play around with different schedules quite easily.

The shortest time schedule that you can have is "every minute", which can be configured by entering `* * * * *` into the `Schedule` field.

### Web Hooks
As discussed before, this is the preferred method if your instance of Jenkins can be accessed from the internet.
This is because instead of constantly checking for new changes, the job can be triggered but a Webhook which is really just a HTTP POST request to the jenkins server.

These Web Hooks can be configured on websites like GitHub, Bitbucket and GitLab to send a HTTP POST request to `/github-webhook/` on your Jenkins server.

This POST request will contain either a JSON or XML payload with information about which repository and branch has been updated.
Jenkins can then use this information automatically build the correct job.

To configure Web Hooks to work you will need to check the `GitHub hook trigger for GITScm polling` option under the `Build Triggers` section on your Jenkins job that you are wanting to automatically trigger.
You will then need to configure your Git service provider (such as GitHub) to send Webhooks to `[JENKINS_ADDRESS]/github-webhook/`.

## Demo
In this demo we'll be automating the deployment of a simple website.
There are two main components to this application:
- Frontend
    A HTML and JavaScript website that makes calls to the Backend service.
    This website is hosted with NGINX as a webserver
- Backend
    A Python Flask server which can connect to a database
- Database
	MySQL Database.

#### Prerequisites
- Jenkins installed on a Ubuntu/Debian machine, ideally a virtual machine so that it can be deleted afterwards.
- Full sudo access for the `jenkins` user with no password required.
- Jenkins must not be installed in a Docker container for this demo
- Ports `8080` and `80` accessible to the machine

### Setup Git Repositories
For this example we are going to need couple of Git repositories.
Go ahead and create these repositories on GitHub:
- `jenkins-scm-frontend`
- `jenkins-scm-backend`
- `jenkins-scm-database`

### Upload the Provided Code
Upload the code found in the `frontend`, `backend` and `database` folders in this module to these repositories that you created.
You can do this by initializing the folders as Git repositories and then configuring your GitHub repositories as remotes.

### Create the Jenkins Jobs
You will need a Jenkins job for each GitHub repository; `frontend`, `backend` and `database`.

Lets create the database job first.
- Configure the source code management section to download the master branch from database repository.

	![SCM Database Configuration](https://lh3.googleusercontent.com/jDpha-CZud0YiduYDoSGzwT5xJWwiXFxBAc32yHbcL1ndp5HJtd5XdeyEDlZA3EFnTgiBEleYhqdaOuPz0uIZ-Egm1LO7Wq3Z7h10_79MMiP2AI_T3i01I1yzyA27aIjOpIo2PuYUy2_abpeswg6Op-p1LnYkj-J_0I6M9TCxkaB9-vgeOpSlEfCu6bzJnawJaqZZAkqlY6WBXAeitjlsJv04gGm_HW-nzqESxel1bXQL-26InaDA3Epknuna7oiMFswAEUxkFXd_h7XYA509rApIpUIMf2-RRyKMeCONEmIu0vxgz0l2iZey-097m9uhSTpLZOyIetJgcsfQan9WDlcnZI9LXrh9VkkxRq33Ge7qHPKcyPcC8Mod9fNI8guppk795huU1n0b7h8BZtz7vXjbi5vvvPG7Vh1KH_qz81eapBY8LdUbN6U0mrxMbh6Ddf8kEXiHZaRf-06uGlMQxwT8Z1RcD3SUh3-YQRnYpR5GExU-VW0Y0mBMhvpsU2lZDPEDJGEYhG8KkTqsFgt_rzomcBYMoa5RhbquE810Cg1WSmR2e_1eLENXuJcUlPAA00dL86NQkTqtFpBQX5WDZftLpvF3hsQWj0S-6jEDwwCYSZG7Gtui3aqnyIEaL829tTO9XnIz2g8ld27PFsjnx-EUf6a61G--NPsgidAK90AeCfJvJhE5Jf5J2OislkozkbsLBgi3AIZAMPZNPuK0JNATqV1gpy3Ilq_kSU75JzUZUNA=w1423-h556-no)

- Check the `GitHub hook trigger for GITScm polling` option under the `Build Triggers` section.
- Under `Build Environment`, select `Use secret text(s) or file(s)`. Add a `Username and Password (separated)` and a `Secret text` binding. Use the add button to create credentials for these and name the variables as shown below:

	![Credential Bindings](https://lh3.googleusercontent.com/YPbkikXksHPdkplrXt3WV4hAGWLNhdcn7lmoGPC3X-ryb8ZEuDxbm4_o5Of19tmLlNhoWJxAPicYD4g9ZGq_8c7AivsAIY-ytjGIq0ohpeYMiKyEcKRQPJbQd1Tqg_-S5ektGoBVIvVmE0Keo63bTebH6ZmR7lbk9wwK1isbsHNynZSoj0Tn0jnyEUwCjEBGpURdPl2dtN0ll7EWpWpbqd5sm5FC06dM2lVZix4-mJOqf09LoCr3y9pwK6xvDgj6MGbxW1jT24AC38AbUe6Vyrx-gb8ebTwW0gx-UPQlGFJNBDG1hHr4lkrdiJtNyV1wGutOgU4_PFTO9Jy5f1WBbTagUJzS8SoNnoBWWaz0ypET7AFlnWEgghKJdK2CNaumVh73qJaqyJ88kFqlTm0XKISbCmB7mMiQEkwMgLvOQ5Jz5-39y7iBFi-OPwbM1BEnn1uv1cnw496WrmJtg_HpvNjQQ2DGZY67nXpuw-gNbntrpO5wp4Aa5yzyaHzI8YWcYoEkA6Fo127oI_i-5tq6bdFt0Uy4LvUBOHPkM2GTdk5rYb9jSsiHVZmlEw30e7zzNX5FnErSiF2vgXho3XFOOWUeY9BN6cjO1sBMKxAf8FOQoOtyGGmKj2Sh_mkfRCgPwLIB1WtCDvi7IKxABIdovtNNVuucU6r-19iRC0WhIB13VRsfHs7-LPyQxwkILQHeaJf4H-11ERxgx4bXiAEWLmLMuOeTh6NmFb_Wp2jabUpWEeA5=w1428-h456-no)

	The actual value of the credentials (password contents etc) can be whatever you like.

- Add an `Execute shell` build step with the following configured as the command:

	```bash
	export MYSQL_USER
	export MYSQL_PASSWORD
	export MYSQL_ROOT_PASSWORD
	export MYSQL_HOST="localhost"
	export MYSQL_DATABASE="bookshelve"
	./setup.sh
	```
- Build the job to make sure that it succeeds

Now that you have a working Job for the database, complete the same steps as above for the, backend and frontend.
Make sure to reuse any credentials that you made previously, don't create new ones.

### See the Application Working
You should now be able to navigate to your machine's address on port `80`to see the application working.

### Webhook Configuration
We have already configured the Jenkins jobs to accept Webhooks as triggers so now we just need to setup the Webhook on a Git service provider like GitHub etc.
For this example we will be discussing how you can use GitHub to send Web Hooks to your instance of Jenkins, do the following for each of the GitHub projects that you have created:
1. On your GitHub project navigate to the `Settings` tab.
2. Click on `Webhooks`
3. Set the `Payload URL` to be `[JENKINS_ADDRESS]/github-webhook/`; **Don't miss the trailing `/` on the end of the Payload URL!**
4. Set the `Content type` to be `application/json`
5. Select `Add Webhook`

### Push a New Change
We can now have a look at making some changes on the remote repositories to trigger automatic deployments of our new changes.

#### Frontend
Add `<h1>UPDATE</h1>` after line `9` in the `frontend/index.html` file.
Push the new changes to the GitHub repository, then then you should see the frontend Job automatically build.

Now try navigating to the site to see your changes.

#### Database
We can add a new item into the database to see the changes.
In the `database/setup.sql` append the statement shown below, then push the changes to the database repository:
```sql
INSERT INTO Books (
        Name, Author, Image
) VALUES (
        "Harry Potter and the Philosopher's Stone",
        "J.K. Rowling",
        "https://books.google.com/books/content/images/frontcover/39iYWTb6n6cC?fife=w200-h300"
);
```

The changes that you made should then be reflected on the running site.

### Clean Up
To finish up here the virtual machine being used can be deleted.
