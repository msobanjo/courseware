# Jenkins Setup from the Portal
Configuring Jenkins using a graphical interface.
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Unlocking Jenkins](#unlocking-jenkins)
- [Customize Jenkins](#customize-jenkins)
- [Plugin Installation](#plugin-installation)

<!--TOC_END-->
## Overview
This document aims to guide you through the setup process of Jenkins through the graphical (web) interface.
## Unlocking Jenkins
To make sure that it is you who is trying to configure Jenkins, the setup requires you to enter an initial admin password that is stored on the file system of the machine that Jenkins is running on.
The page clearly states where this file is located, you just need to copy the contents of it into the text field and click `Continue`.
![Jenkins Initial Admin Password](https://i.imgur.com/Poqds4F.png)
## Customize Jenkins
Jenkins is highly configurable due to the amount of plugins that you can install.
This is fantastic however if you are new to Jenkins you might not have much of an idea about what plugins you would want.
Fortunately the setup gives you the option to install suggested plugins, select this option.
![Customize Jenkins](https://i.imgur.com/hg1BlXL.png)
## Plugin Installation
For this part there isn't much to do but wait.
The suggested plugins or plugins that you selected will be installed, how fast they are installed depends on your internet speed.
If plugins are failing to install then make sure that you have the latest version on Jenkins installed.
![Plugin Installation](https://i.imgur.com/tNnEJVf.png)
## Create the First Admin User
At this point you can either fill in the form to have your details saved into the first admin account or continue as admin, which will mean that the admin user account name is `admin` and the password will stay as the initial admin password that you entered.
Be careful to not enter actual passwords and information here if you are connected to a Jenkins instance over the internet with no TLS or SSL configured (HTTPS secure connection).
![Create First Admin User](https://i.imgur.com/DIzyESa.png)
## Instance Configuration
All you will need to for this step is select `Save and Finish`.
![Instance Configuration](https://i.imgur.com/SPPAiXG.png)
## Dashboard
You should now have Jenkins setup and have the following dashboard on you screen:
![Dashboard](https://i.imgur.com/JsVUo3x.png)
