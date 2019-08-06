<!--PROPS
{
    "prereqs": [
        "linux/nano",
        "linux/vi"
    ]
}
-->
# Sudoers
## Overview
The sudo tools allows a user to act as a superuser for a command.
You can think of running a command as sudo like running a an application as administrator on a Windows machine.
Of course not anyone can just run a sudo command on a Linux machine otherwise everyone would have administritive access.
Users who can use sudo are configured in the `/etc/sudoers` file.
This file is extremely important and **should not be edited directly**.
If the sudoers file is broken, then no one on the system can use sudo commands!
There is a tool called `visudo` which can be used to edit the file safely.
When you save the file when using `visudo`, the syntax will be checked first to make sure the file isn't currupt.
## Configuring a sudo User
An entry can be made into the sudoers file with the following format:
![Sudoers Entry](https://i.imgur.com/CACwueA.png)
### Run sudo Commands Without a Password
By default a sudo user needs to enter their password when running a command as sudo.
This is can be an issue however if the commands are being run in a script.
To get around this a sudo user can be aloud to use sudo without a password:
```text
# allow the user bob to run any command as sudo without a password
bob ALL=(ALL:ALL) NOPASSWD:ALL
```
### Only Allow Specific Commands
Allowing all commands for a user basically just makes them a proxy root user which often isn't what a system administrator would want.
We can allow the user to only run specific commands, for example a Jenkins user might only need to be able to manage a systemd service like so:
```text
jenkins ALL=(ALL:ALL) NOPASSWD:\
    /bin/systemctl start nginx,\
    /bin/systemctl stop nginx,\
    /bin/systemctl status nginx
```
Make sure that you include the full path to the binaries that you are using.
For instance the `systemctl` commands full path is `/bin/systemctl`.
To find the location of an application you can use the `type` command:
```bash
type systemctl 
# /bin/systemctl
```
