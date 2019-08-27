# Lab-1 Installing Azure CLI

In this lab you will go through the steps required to install the Azure CLI.

## Installing Azure CLI on Windows
1. Go to the following [URL](https://aka.ms/installazurecliwindows) this will automatically start downloading the 
installer required
2. Open the downloaded file, you will most likely see an image like this:
![alt text](https://imgur.com/mq4ifPX.png)
3. Click on *Run*
4. Accept the license agreement and click *Install*

![alt text](https://imgur.com/bCxkRBt.png)
5. Wait until the files are copied over and click *Finish*
![alt text](https://imgur.com/M7FpuLz.png)
6. Open *Command Prompt*
7. Let's check that the Azure CLI has been successfully installed by running the following command
`az --help` and press enter
![alt text](https://imgur.com/wMIcO7n.png)
8. If you got the help output the installation was successful, if you didn't get the help output ask your trainer for help

## Installing Azure CLI on Linux
1. Open terminal
2. Run the following command `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
![alt text](https://imgur.com/unsKxs0.png)
3. You will most likely be asked to enter password, enter it
4. Once the installation has been completed run the following command to make sure installation was successful
`az --help`
![alt text](https://imgur.com/4dwOni0.png)
5. If you got the help output the installation was successful, if you didn't get the help output ask your trainer for help

## Summary

In this lab we have learned how to install Azure CLI on either Windows or Linux

