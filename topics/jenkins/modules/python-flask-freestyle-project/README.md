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

# Python Flask Freestyle Project

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tutorial](#tutorial)
	- [Prerequisites](#prerequisites)
	- [Jenkins Job](#jenkins-job)
	- [Shell Script](#shell-script)
- [Exercises](#exercises)
	- [Try this on Another Project](#try-this-on-another-project)

<!--TOC_END-->
## Overview
Basic deployment of a Python Flask server, using systemd and a Freestyle Project.
Included in this module folder is a Python Server that uses the Flask framework.

The sample project included for this example is a single python script.
There is also a systemd service configuration included, for running the application as the `pythonadm` user.
Please note that, because of systemd, this example will not work inside a docker container.

## Tutorial

### Prerequisites
There are a few prerequisites for this module, so make sure the following has been configured on your machine by running the script below:
- Linux (Ubuntu/Debian) operating system, not in a container such as Docker
- Jenkins installed & running
- Python 3 installed
- `virtualenv` installed
- `jenkins` user, configured as a sudo user with no password
- `pythonadm` user created

```bash
# create the users if they don't exist
users=( jenkins pythonadm )
for user in "${users[@]}"; do
    if ! awk -F : '{ print $1 }' /etc/passwd | grep -w "${user}" > /dev/null; then
        sudo useradd -m -s /bin/bash ${user}
    fi
done
# add jenkins to sudoers
jenkins_sudoers_entry='jenkins     ALL=(ALL:ALL) NOPASSWD:ALL'
sudoers='/etc/sudoers'
if ! sudo grep -w "${jenkins_sudoers_entry}" ${sudoers}; then
    echo "${jenkins_sudoers_entry}" | sudo tee -a ${sudoers}
fi
# apt dependencies
sudo apt update
sudo apt install -y openjdk-8-jre python3 virtualenv
# jenkins setup
sudo su - jenkins -c "curl -L https://updates.jenkins-ci.org/latest/jenkins.war --output jenkins.war"
sudo tee /etc/systemd/system/jenkins.service << EOF > /dev/null
[Unit]
Description=Jenkins Server
[Service]
User=jenkins
WorkingDirectory=/home/jenkins
ExecStart=/usr/bin/java -jar /home/jenkins/jenkins.war
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl restart jenkins
```

### Jenkins Job
Using the Jenkins instance installed on your machine, create a Freestyle Project called `flask-app` and configure it to download this code onto its filesystem; this can be configured in the Source Control Management section:
- `Repository URL` set to `https://github.com/bob-crutchley/courseware`

### Shell Script
We will need a script that completes the steps shown below, there is a shell script included afterwards for this:
- **Change directory to this module's folder.**  
  The files that are being used are stored in the `resources` folder for this courseware module, we'll be operating on the files here frequently so we may as well change directory to it.
- **Install the systemd service script.**  
  The service script (`flask-app.service`) will show systemd how to run your application, it will need to be installed into a folder such as `/etc/systemd/system`
- **Reload the systemd service scripts.**  
  Whenever you change a service script, you must let systemd know that there has been a change and reload the installed service scripts.
- **Make sure the old service is stopped.**  
  Before we can install the new application, the current one that is running must first be stopped.
- **Install the application files.**  
  The new files for the application will need to be installed to replace the old ones.
- **Setup the python virtual environment and dependencies.**  
  A virtual environment can be used to keep deployments consistent, dependencies can be stored in `requirements.txt` file and loaded from there.
- **Start the service.**  
  The application will need to be stared for it to be functional.

These requirements can be accomplished by putting the script below into an `Execute shell` build step on the Jenkins job:

```bash
# move to module folder
cd ./topics/jenkins/modules/python-flask-freestyle-project/resources
# install the service script
sudo cp flask-app.service /etc/systemd/system/
# reload the service scripts
sudo systemctl daemon-reload
# stop the old service
sudo systemctl stop flask-app
# install the application files
install_dir=/opt/flask-app
sudo rm -rf ${install_dir}
sudo mkdir ${install_dir}
sudo cp -r ./* ${install_dir}
sudo chown -R pythonadm:pythonadm ${install_dir}
# configure python virtual environment and install dependencies
sudo su - pythonadm << EOF
cd ${install_dir}
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
EOF
# start the flask app
sudo systemctl start flask-app
```

## Exercises

### Try this on Another Project
Use another Python Flask application and deploy it as a systemd service using the tutorial above.
If you don't have a Flask app available to you then feel free to use this provided example: https://github.com/qac-devops/python-flask-example
