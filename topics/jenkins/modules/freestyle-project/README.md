# Freestyle Project
## Overview
Freestyle projects in Jenkins are a type of job you can create for pretty much any automated task.
These are the best place to start for building any sort of general purpose automation in Jenkins.
## Create a Freestyle Project
Go ahead and select `New Item` from the Jenkins dashboard and then create a new Freestyle Project called `freestyle-project`:
![Freestyle Project](https://i.imgur.com/qGGXAKX.png)
## Source Code Management
This section is used for configuring a source code repository to download.
The job will download the repository you provide into the jobs workspace.
## Build Triggers
The most simple way to run a Jenkins job is by pressing the build button for the job.
However jobs can be triggered in many ways, often not manually.
### Build Periodically
You can create a schedule here in which to execute the job, every hour or at 6:15 PM every Thursday for instance.
### GitHub Hook
This is where GitHub can send a HTTP POST request, AKA webhook to your Jenkins server to trigger a build of the job.
This must be configured in GitHub and your Jenkins instance must be accessable from the internet for this to work.
### Poll SCM
This feature can be used if your Jenkins instance is not accessible on the internet.
Jenkins will check on schedule that you define, whether a change has been made on the configured SCM repository.
As soon as a change has been detected then the job will be executed.
The minimum polling interval is every 1 minute.
## Build Environment
### Delete Workspace Before Build Starts
You will likely want this option checked.
The folder on the host machines files system that the job runs in will be deleted before building again every time.
### Secret Texts & Files
You may securely use secret texts and files that you have configured in the Credentials section here in the job.
These secrets will also be hidden in the Jenkins logs as well.
## Build
This is likely where you will spend most of you time on a Jenkins job.
The most common build step here is `Execute shell`, other options are available depending on what plugins you have installed.
Exactly what your job accomplishes is configured here.
## Post-build Actions
You may want to configure your job to reacthow the build went.
For instance if the job failed, you can be notified by email.
If the job completed successfully and you want a report published that can be done to.
Like with most of the options, the sky is the limit depending on what plugins are installed.
## Tasks
1. If you haven't created a Fresstyle Project already, go ahead and create one now
2. Lets configure it to download this project and checkout to this subdirectory:
    ![Source Code Management](https://i.imgur.com/6itMbjh.png)
3. Now add an `Execute shell` build step and enter the following into it:
    ```bash
    sh run.sh
    ```
4. Run the job
5. Navigate to the jobs logs, you should see the contents of this `README.md` file displayed in the logs
