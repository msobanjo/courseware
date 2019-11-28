# ARP

## Overview
The **Address Resolution Protocol (ARP)** is used to resolve **Media Access Control (MAC)** addresses to IP addresses.

(MAC addresses are discussed in [this module](https://github.com/bob-crutchley/courseware/tree/master/topics/networking/modules/mac-address/).)

Its inverse, **Reverse Address Resolution Protocol (RARP)** is used to resolve IP addresses back to MAC addresses.

This is useful for discovering other devices on your private network, amongst other things.

## NIC and MAC
Every networked device contains at least one physical **Network Interface Card (NIC)**, such for Ethernet or wireless connections, providing a physical connection between that device and a network.

NICs can generate a **broadcast domain** between devices if they are all connected to the same system - the numbers in the below diagram signifies a different broadcast domain:

```text
                 1                  2
          ┌────────────[Router]────────────┐
       [Switch]           | 3           [Switch]
    ┌─────┴─────┐       [Node]       ┌─────┴─────┐
  [Node]      [Node]               [Node]      [Node]
```

Each NIC has a unique MAC address burned into it by its manufacturer, which are used by Ethernet and wireless connections to communicate between network devices.

As these NICs only understand MAC addresses, the **Address Resolution Protocol (ARP)** is used to resolve MAC to IP, or vice-versa.

## Usage
ARP broadcasts packets to all computers on the network so as to discover MAC addresses.

Here, **Node 1** and **Node 2** are both present on the same network:

```text
 ┌────────[Node 1]─────────┐						        			┌────────[Node 2]─────────┐
 │ MAC: 12:6e:eb:de:b3:ed  │────────────────────────────────────────────│ MAC: 12:6f:56:c0:c4:c1  │
 │ IP: 10.12.2.73          │											│ IP: 10.12.2.1           │
 └─────────────────────────┘							        		└─────────────────────────┘
```

If **Node 1** tries to find the MAC address associated with the IPv4 address `10.12.2.1`, it will broadcast an **ARP request** along the network until it finds the device it needs:

```text
 ┌────────[Node 1]─────────┐											┌────────[Node 2]─────────┐
 │ MAC: 12:6e:eb:de:b3:ed  │────────────>───────────────────>───────────│ MAC: 12:6f:56:c0:c4:c1  │
 │ IP: 10.12.2.73          │	   Source MAC: 12:6e:eb:de:b3:ed		│ IP: 10.12.2.1           │
 └─────────────────────────┘	   Source IP:  10.12.2.73  	       		└─────────────────────────┘
								   Target MAC: 00:00:00:00:00:00
								   Target IP:  10.12.2.1
```

Once **Node 2** receives this request, it will send an **ARP response** if the Target IP matches its IP address:

```text
 ┌────────[Node 1]─────────┐									  		┌────────[Node 2]─────────┐
 │ MAC: 12:6e:eb:de:b3:ed  │────────────<───────────────────<───────────│ MAC: 12:6f:56:c0:c4:c1  │
 │ IP: 10.12.2.73          │	   Source MAC: 12:6f:56:c0:c4:c1		│ IP: 10.12.2.1           │
 └─────────────────────────┘	   Source IP:  10.12.2.1	   	   		└─────────────────────────┘
								   Target MAC: 12:6e:eb:de:b3:ed
								   Target IP:  10.12.2.73
```

## Tasks
### View the ARP table
#### macOS, Linux, or Windows Subsystem for Linux
Open a terminal, then enter the following command:
```text
admin@ubuntu:~$ cat /proc/net/arp
```
You should see something like this:

```text
IP address		Hw type		Flags	HW address			Mask	Device
192.168.1.73	0x1			0x2		10:fe:ed:11:d4:ec	*		enp0s3
192.169.1.254	0x1			0x2		a0:39:ee:4e:5a:49	*		enp0s3
```
What might these represent?

#### Windows
Open a command prompt/Powershell, then enter the following command:
```text
 C:\WINDOWS\system32>arp -a
```
You should see one or more tables like this:
```text
Interface: 192.168.1.154 --- 0x18
  Internet Address      Physical Address      Type
  192.168.1.133         f4-30-b9-dc-fd-41     dynamic
  192.168.1.228         80-e8-2c-b3-d2-32     dynamic
  192.168.1.254         00-0c-29-3c-38-5f     dynamic
  192.168.1.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
```
What might these represent?

### Use ARP spoofing to launch a MITM attack
<!--SPOOFING TASK NEEDED HERE:

This module would serve as a practical implementation for understanding how the ARP works.

Which targets to select (victim device for target 1 and default gateway for target 2)
How to select which victim device
How to find out the default gateway
What to look for in Wireshark (HTTP requests mainly)
Ettercap can be used to start the MITM attack, then Wireshark can be used to analyse the packets of the targeted devices.
Note that the target device must of course be on the same network.
I also ran into issues when trying this if the target device is on Wifi when the machine I'm using is on Ethernet and vice versa.

-->
