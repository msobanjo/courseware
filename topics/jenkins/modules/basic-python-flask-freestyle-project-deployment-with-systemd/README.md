<!--PROPS
{
    "prereqs": [
        "jenkins/web-setup",
        "jenkins/jobs",
        "jenkins/freestyle-project",
        "linux/systemd",
        "linux/sudo"
    ]
}
-->
# Basic Python Flask Freestyle Project Deployment with systemd
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Sample Project](#sample-project)
- [Host Machine Configuration](#host-machine-configuration)
- [Jenkins Job](#jenkins-job)
	- [Configure Source Control Management](#configure-source-control-management)

<!--TOC_END-->
## Overview
Basic deployment of a Python Flask server using systemd and a Freestyle Project
Included in this module folder is a Python Server that uses the Flask framework.
## Sample Project
The sample project included for this example is a single python script.
There is a systemd service configuration included also for running the application as the `pythonadm` user.
Please note that this example will not work inside a docker container because of systemd.
## Host Machine Configuration
There are a few prerequisites before getting this to work, so make sure the following has been configured on your machine:
- Linux operating system with systemd, not in a container
- Jenkins installed & running
- Python 3 installed
- Jenkins user configured as a sudo user with no password
## Jenkins Job
Create a Jenkins Freestyle Project called flask-app and configure it to deploy this application:
### Configure Source Control Management
We need Jenkins to download to download this code onto its filesystem, this can be configured in the Source Control Management section:
-
