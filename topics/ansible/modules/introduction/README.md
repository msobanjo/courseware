<!--PROPS>
{
    "prerequisites": [
        "package-managers/pip-introduction",
        "linux/path-environment-variable"
    ], "supportedPlatforms": [
        "ubuntu-18"
    ]
}
<!-->

# Introduction

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Installation](#installation)
	- [Using Pip](#using-pip)
- [Task](#task)
	- [Install Ansible](#install-ansible)
	- [Configure a Playbook to Install a Web Server](#configure-a-playbook-to-install-a-web-server)
	- [Run the Playbook](#run-the-playbook)
	- [Check NGINX has been Installed Correctly](#check-nginx-has-been-installed-correctly)

<!--TOC_END-->
## Overview
Ansible is an open-source software provisioning, configuration management, and application-deployment tool.
It runs on and can configure many Unix-like systems, as well as Microsoft Windows. 

## Installation

### Using Pip
A good way to install Ansible is by using the Pip package manager.
<<<<<<< HEAD
This is because to run Ansible on any machine you are going to need Python installed, with Python installed the Pip package manager is a consistent way to install Ansible on any machine.
=======
Ansible requires Python to be installed to run on any machine. With Python installed, we can then use the Pip package manager to install Ansible on any machine consistently.
>>>>>>> 2aef3f76a4ada808ee46ff231d66b1501db850b8

We can also use Pip to install Ansible into the current user's home directory too, avoiding any need for elevated permissions on the machine.
```bash
# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
## install ansible with pip
pip install --user ansible
# check that ansible has been installed
ansible --version
```

## Task

### Install Ansible
Start by making sure that Python installed on your machine, then go ahead and install Ansible using Pip.

### Configure a Playbook to Install a Web Server
Ansible configures its hosts through playbooks; the intricacies of Ansible configurations will be discussed in another module.

Ansible is more commonly used to install applications and configurations on other remote hosts, but for this example, we will just install a web server on the same host to simply demonstrate how a playbook works.

Here we have a playbook which installs a basic NGINX web server so that we can use Ansible, so go ahead and create a file called `playbook.yml` which contains the following:
```yaml
---
- hosts: 127.0.0.1
  connection: local
  become: true
  tasks:
  - name: Install NGINX
    apt:
      name: nginx
      state: latest
      update_cache: true
  - name: Start NGINX Service
    service:
      name: nginx
      state: started
```

### Run the Playbook
The `ansible-playbook` command can be used to run our playbook and install NGINX on the server:
```bash
ansible-playbook playbook.yml
```

### Check NGINX has been Installed Correctly
The `curl` command can be used to check that our web server is running correctly:
```bash
curl http://localhost
```
You should get a response back similar to this:
```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
