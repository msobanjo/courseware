# Lab-1 Installing Azure CLI

In this lab you will go through the steps required to install the Azure CLI.

## Installing Azure CLI on Windows
1. Go to the following [URL](https://aka.ms/installazurecliwindows) this will automatically start downloading the 
installer required
2. Open the downloaded file, you will most likely see an image like this:
![alt text](lab-1-images/image1.png)
3. Click on *Run*
4. Accept the license agreement and click *Install*
![alt text](lab-1-images/image2.png)
5. Wait until the files are copied over and click *Finish*
![alt text](lab-1-images/image3.png)
6. Open *Command Prompt*
7. Let's check that the Azure CLI has been successfully installed by running the following command
`az --help` and press enter
![alt text](lab-1-images/image4.png)
8. If you got the help output the installation was successful, if you didn't get the help output ask your trainer for help

## Installing Azure CLI on Linux
1. Open terminal
2. Run the following command `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
![alt text](lab-1-images/image5.png)
3. You will most likely be asked to enter password, enter it
4. Once the installation has been completed run the following command to make sure installation was successful
`az --help`
![alt text](lab-1-images/image6.png)
5. If you got the help output the installation was successful, if you didn't get the help output ask your trainer for help

## Summary

In this lab we have learned how to install Azure CLI on either Windows or Linux

# Lab-2 Connecting to Azure and using interactive mode

In this lab you will connect to the Azure services through the terminal and learn how to use the interactive mode.

1. Open a terminal
2. Execute the following command `az login`, your default browser will open up a Microsoft page
![alt text](lab-1-images/image7.png)
3. Enter the details for the Azure account you're using
![alt text](lab-1-images/image8.png)
![alt text](lab-1-images/image9.png)
4. You will be redirected to the page that should say
![alt text](lab-1-images/image10.png)
5. On the terminal you should see a similar output but with your details
![alt text](lab-1-images/image11.png)
6. Execute the following command to invoke interactive CLI mode `az interactive` it will take a few minutes the first 
time you're using it to download and install all the requirements
7. You can choose to send or not to the telemetry data
![alt text](lab-1-images/image12.png)
8. After choosing your option about the telemetry data you will then be taken to the interactive CLI window
![alt text](lab-1-images/image13.png)
`az interactive` gives a couple of benefits like auto-completion, command descriptions and examples
9. Pick a style for the interactive mode from the available list by running the command `az interactive --style styleName`
![alt text](lab-1-images/image14.png)
10. You can also execure shell commands by using `#`, let's list all the contents of the current directory by executing
`#dir` you should see the terminal display the contents

## Summary

In this lab you have learned how to log in to your Azure services through CLI, as well as how to start the CLI 
interactive mode

# Lab-3 Creating a VM through CLI

In this lab we'll be creating a Virtual Machine and other required resources through CLI

1. Open terminal
2. Log in
3. First we'll create a new resource group in the *ukwest* region by executing the following command
`az group create --name my-first-vm --location ukwest`
![alt text](lab-1-images/image15.png)
We can see that under the *properties -> provisioningState* the value is *Succeeded* this means that your resource
group has been successfully created

























