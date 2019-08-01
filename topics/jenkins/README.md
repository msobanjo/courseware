# Jenkins
## Overview
Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.
Jenkins can be installed through native system packages, Docker, or even run standalone by any machine with a Java Runtime Environment (JRE) installed.

## Installation
### Docker (Any Platform)
You will of course need Docker installed but with Docker, getting Jenkins installed can be done with this command:
```bash
docker run -d -p 8080:8080 --name jenkins/jenkins:lts-alpine
```
### Windows
An installer can be downloaded and ran to get Jenkins running on Windows here: https://jenkins.io/download/
### Linux
There is a script (`jenkins-install.sh`) in this directory that you can use to install Jenkins on popular Linux distrobutions like Debian/Ubuntu, CentOS & RHEL.
Please note if you are using the script then you will have to have sudo access on the machine you execute it on.
Simply put this script on the machine you wish to install it on and execute it like this:
```bash
./jenkins-install.sh
```
