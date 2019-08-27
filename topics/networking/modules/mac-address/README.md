# MAC Address
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Relevence & Day to Day Application](#relevence--day-to-day-application)
	- [Public Wifi](#public-wifi)
- [Viewing Your MAC Address](#viewing-your-mac-address)
	- [Windows](#windows)
	- [Linux](#linux)
- [Format](#format)
	- [Hexadecimals](#hexadecimals)
	- [OEM & Unique ID](#oem--unique-id)
- [Spoofing](#spoofing)
	- [Why?](#why)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
A media access control address of a device is a unique identifier assigned to a network interface controller.
For communications within a network segment, it is used as a network address for most IEEE 802 network technologies, including Ethernet, Wi-Fi, and Bluetooth.  
MAC addresses are used as physical hardware addresses for devices on a network.
These are important because they are unique for every piece of networking hardware.
This means that they can be used on a low level of networking when delivering frames (packets of data) over Local Area Networks (LAN) to make sure that the data is getting to the correct device.
## Relevence & Day to Day Application
Because MAC addresses are used on such a low level for LAN; any network connection made, be it browsing the internet or making a video call, will end up using MAC addresses at some point for the connection to be established.
### Public Wifi
MAC addresses are there for identifying a device, so this can be utilised for something like public Wifi.
When you try to log into a Wifi network in an Hotel or Coffee shop for example, you will likely be faced with a pay wall.
After purchasing Wifi access, the MAC address of the current device you are using can be stored on their servers, so that any traffic coming from your device will be allowed onto the Internet.
## Viewing Your MAC Address
### Windows
On a Windows machine you can use the `ipconfig /all` command inside a command prompt or Power Shell to see what your MAC address is.
### Linux
Depending on what tools are installed on your system there are several ways that you can get your MAC address:
```bash
# using ifconfig
ifconfig -a
# using ip
ip link show
```
## Format
### Hexadecimals
MAC addresses are 6 bytes (48 bits) of data represented as a hexadecimal:
```
1C-B7-2C-B9-27-09
```
### OEM & Unique ID
The first 3 bytes in a MAC addres is issued to the Original Equipment Manufacturer (OEM) to assign to the device.
The last 3 bytes are unique to the device which are created and assigned by the OEM.
For example in the MAC address `1C-B7-2C-B9-27-09`; `1C-B7-2C` would be the part issued to the OEM to assign and `B9-27-09` is what was created and assigned by the OEM.
## Spoofing
Although the MAC address for your device is basically hard-coded into the network interface, modern network drivers will typically allow you to change the MAC address temporarily.
This is easy enough to do on Linux by turning off the interface, changing the address to what you like and then starting the interface again:
```bash
# find the interface to change the address of, enp1s0 for example
ip link show
# bring down the interface
ip link set [INTERFACE] down
# set the address
ip link set dev [INTERFACE] address XX:XX:XX:XX:XX:XX
# bring the interface back up
ip link set dev [INTERFACE] up
```
### Why?
Changing a devices MAC address can be used for bypassing or "tricking" access control in place by disguising itself as another device.
This is typically a technique used for malicious purposes but can be used for penetration testing and ensuring your services are robust enough to not be susceptible to this.
## Tasks
- Find the MAC address of the current device that you are using, remember you can use `ipconfig /all` on Windows an `ip link show` on Linux.
- Use the first 3 bytes of your MAC to find out who manufactured your network interface card (NIC), usually just putting it in a Google search will show you this.
