# MAC Address
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Viewing Your MAC Address](#viewing-your-mac-address)
	- [Windows](#windows)
	- [Linux](#linux)

<!--TOC_END-->
## Overview
A media access control address of a device is a unique identifier assigned to a network interface controller.
For communications within a network segment, it is used as a network address for most IEEE 802 network technologies, including Ethernet, Wi-Fi, and Bluetooth.  
MAC addresses are used as physical hardware addresses for devices on a network.
These are important because they are unique for every piece of networking hardware.
This means that they can be used on a low level of networking when delivering frames (packets of data) over Local Area Networks (LAN) to make sure that the data is getting to the correct device.
## Viewing Your MAC Address
### Windows
On a Windows machine you can use the `ipconfig /all` command inside a command prompt or Power Shell to see what your MAC address is.
### Linux
Depending on what tools are installed on your system there are several ways that you can get your MAC address:
```bash
# using ifconfig
ifconfig -a
# using ip
ip a
```
