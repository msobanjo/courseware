<!--in-progress, may split out/remove some/all vpn and onion stuff-->

# IP

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Usage](#usage)
- [IP addresses](#ip-addresses)
	- [IP Address Structure](#ip-address-structure)
	- [Binary](#binary)
	- [Reserved IP addresses](#reserved-ip-addresses)
	- [A brief note on IPv6](#a-brief-note-on-ipv6)
- [Tasks](#tasks)
	- [Convert binary IP addresses to decimal](#convert-binary-ip-addresses-to-decimal)
	- [Find your IP address](#find-your-ip-address)
		- [macOS, Linux, or Windows Subsystem for Linux](#macos-linux-or-windows-subsystem-for-linux)
		- [Windows](#windows)
	- [Change your IP address](#change-your-ip-address)
		- [macOS, Linux, or Windows Subsystem for Linux](#macos-linux-or-windows-subsystem-for-linux-1)
		- [Windows](#windows-1)
	- [Look at your network's TCP/IP traffic](#look-at-your-networks-tcpip-traffic)

<!--TOC_END-->
## Overview
Nearly all networks are based on the **Internet Protocol Suite (TCP/IP)**, the set of protocols that allow for a device to gain access to the Internet.

Contained within this suite is the **Transmission Control Protocol (TCP)**, which facilitates connections between nodes within a network, and the **Internet Protocol (IP)**, which has the task of delivering data from a source node to a destination node.

*TCP* is a connection protocol: it is in charge of ensuring that a connection has been made before data is transferred.

*IP* is connectionless: it does not care whether the information it attempts to deliver is received or not.

*IP* also *encapsulates* the data which it transmits, splitting it into several chunks, or **datagrams**, each containing a **header** and a **payload**:

|Type|Information| 
|-|-|
|**Datagram**|basic transfer unit - contains header; payload|
|**Header**|contains source IP address; destination IP address; routing metadata|
|**Payload**|content of data to be transported|

*IP* can then route these *datagrams* from a 'source' node to a 'destination' node.

Essentially, if *TCP* is the postal service, *IP* is the postman.

*TCP* makes sure that the connections are in place for deliveries to take place, but all *IP* does is delivers stuff, and doesn't care if that stuff ever gets where it's supposed to be or not.

## Usage
The *Internet Protocol* requires five specific things in order to work:
1. An **IP address**, assigned to whichever device is attempting to transfer information over the *internet*
2. The **Address Resolution Protocool (ARP)**, a mechanism for mapping a physical *MAC address* to a networked, non-physical *IP address*
3. A local network (the **`localhost`**), with **ports** to plug programs (or **services**) into
4. A **routing** mechanism for moving data around the network
5. A **network gateway**, to route data from the local **internal** network to **external** networks

## IP addresses
In the same way that a postal system uses addresses for posting letters, *IP* makes use of addresses too.

Each networked system must be identified by some kind of unique identifier.

This is because, when information is sent via *IP*, we have to be sure of where we are sending that information.

Even if the information never arrives, we know that the intended destination is correct every time.

Addressing solves this issue by using a unique **IP address** to each device.

Our current standard of *IP address* is **IPv4**.

The **Internet Engineering Task Force (IETF)** regulates the usage of *IP addresses*.

Each *IP address* is **unique** and  can only be assigned to one device at a time.

Allocating unique *IP addresses* is usually done automatically with the **Dyanmic Host Configuration Protocol (DHCP)**.

By ensuring this uniqueness, any device with an *IP address* can now freely send and receive information through the *Internet Protocol*.

### IP Address Structure
An *IP address* is made up of two groups of bits:
 - the **network prefix** - used to identify the specific network a device is on
 - the **host identifier** - used to identify the specific device in a network

The **network prefix** is static and cannot change, while the **host identifier** is variable.

We use this split to help when **routing** information around, which we cover in more depth [here](https://github.com/bob-crutchley/courseware/tree/master/topics/networking/modules/routing).

### Binary 
*IP addresses* are written in **binary**, and split into four 8-bit sections called **octets**, making a 32-bit address:
```text
00001010.00001100.00111000.00010111
```

Binary can only contain two values: **0** or **1**.

When counting in binary, the easiest thing to check is the position of each *1* and *0*.

Let's take the first one of our octets:
```text
┌────────┬─────┬────┬────┬────┬────┬────┬────┬────┐
│  Value | 128 │ 64 | 32 | 16 |  8 |  4 |  2 |  1 | 
├────────┼─────┼────┼────┼────┼────┼────┼────┼────┤
| Binary |   0 |  0 |  0 |  0 |  1 |  0 |  1 |  0 | 
├────────┼─────┼────┼────┼────┼────┼────┼────┼────┼────┐
|  Total |   0 +  0 +  0 +  0 +  8 +  0 +  2 +  0 = 10 |
└────────┴─────┴────┴────┴────┴────┴────┴────┴────┴────┘ 
```
If any of the binary positions equals `1`, then we add together the values of those positions.

Here, we can see this is true for our `8` and `2` positions.

Therefore, the value of the binary number `00001010` in decimal is `10`. 

Our maximum value for an octet, then, is `255`.

Our full *IP address* can now be resolved into decimal, which is much more human-readable:
```text
10.12.56.23
```

### Reserved IP addresses
Some IP addresses are reserved for private purposes:

|Range|
|-|
|`10.0.0.0 - 10.255.255.255`|
|`172.16.0.0 - 172.31.255.255`|
|`192.168.0.0 - 192.168.255.255`|

Usually, these are used for local communication within a private network.

Others are reserved for particular software uses:

|Range|Usage|
|-|-|
|`0.x.x.x`|software use only|
|`127.x.x.x`|`localhost`|
|`224.0.0.0 - 239.255.255.255`|IP multicasting, e.g. for streaming media|
|`240.0.0.0 - 255.255.255.254`|reserved for future usage|
|`255.255.255.255`|local broadcast|

The most important one to note is `localhost`, which we cover in more depth [here](https://github.com/bob-crutchley/courseware/tree/master/topics/networking/modules/localhost).

### A brief note on IPv6
Eventually, we will run out of *IP addresses*.

Given that the *internet* has been in continuous usage for decades, the problem of *IP address* exhaustion has been prevalent since the late-1980s.

*IPv6* was developed, and is currently in deployment, in preparation for the time when *IPv4* addresses deplete entirely.

*IPv6* uses a 128-bit *IP address* instead of *IPv4's* 32-bit system, ensuring that we should not run out of them again for millions of years.

This can be expressed in eight colonned groups of four hexadecimal digits:
```text
2001:0db8:0000:0000:8a2e:0370:7334:0001
```
This is long and contains a lot of zeroes, so we can make this easier to read by omitting them:
```text
2001:db8::8a2e:370:7334:1
```
The `::` refers to one or more blocks of zeroes.

IPv4 addresses can also be expressed in IPv6 format - the IPv4 address `10.12.56.23` becomes:
```text
::ffff:a0c:3817
```

## Tasks

### Convert binary IP addresses to decimal
Without using an online tool, convert the following binary *IP addresses* to decimal:
```text
11000000.10101000.00000001.00000001
```
<details>

<summary><b>Answer</b></summary>

`192.168.1.1`

</details>

```text
01100100.01100101.01100110.11110100
```

<details>

<summary><b>Answer</b></summary>

`100.101.102.244`

</details>

```text
01111111.00000000.00000000.00000001
```

<details>

<summary><b>Answer</b></summary>

`127.0.0.1`

</details>

```text
11111111.11111101.11111110.11111100
```

<details>

<summary><b>Answer</b></summary>

`255.253.254.252`

</details>

```text
01001010.01111101.00101011.01100011
```

<details>

<summary><b>Answer</b></summary>

`74.125.43.99`

</details>

### Find your IP address

#### macOS, Linux, or Windows Subsystem for Linux
Open a terminal and enter the following command (if on an *Ethernet* network):
```text
ifconfig eth0
```

If you're on a *WiFi* network, the command is:

```text
ifconfig wifi0
```

You should get similar results to this:

```text
nick@DESKTOP-JLGAKSF:/c/WINDOWS/system32$ ifconfig eth0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.154  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::e919:8718:19b4:5ae  prefixlen 64  scopeid 0xfd<compat,link,site,host>
        ether f4:30:b9:dc:fc:07  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

```text
nick@DESKTOP-JLGAKSF:/c/WINDOWS/system32$ ifconfig wifi0
wifi0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.25.198  netmask 255.255.255.0  broadcast 172.17.25.255
        inet6 fe80::f94e:7ba5:ca3f:2673  prefixlen 64  scopeid 0xfd<compat,link,site,host>
        ether a0:af:bd:df:79:10  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

#### Windows
Open a command window and enter the following command:
```text
ipconfig
```

This will display all the availble network connections for your device.

We're interested in either the *Ethernet* or *WiFi* information, depending on how you are connected to the Internet:

```text
C:\WINDOWS\system32>ipconfig

Windows IP Configuration

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::e919:8718:19b4:5ae%22
   IPv4 Address. . . . . . . . . . . : 192.168.1.154
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.254

Wireless LAN adapter WiFi:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::f94e:7ba5:ca3f:2673%21
   IPv4 Address. . . . . . . . . . . : 172.17.25.198
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.17.25.1

```

### Change your IP address

#### macOS, Linux, or Windows Subsystem for Linux
**You will need to make a note of your current IP address before attempting this Task.**

Open a command terminal and enter `ipconfig` again, with either your `eth0` or `wifi0` specifier.

Take a note of the second line of the result set, which displays your *IP address*, *subnet mask* and *default gateway*:
```text
        inet 192.168.1.154  netmask 255.255.255.0  broadcast 192.168.1.255
```

We can change our *IP address* directly from the command line in UNIX-based systems.

Let's change the fourth octet of our *IP address* to something else.

Here, we use `ifconfig` again, but then assign it a new *IP address*.

Just to make sure we aren't doing anything else, we will keep the *subnet mask* the same.

If you're using an *Ethernet* connection, enter the following command:
```text
sudo ifconfig eth0 [XXX.XXX.XXX.]254 netmask 255.255.255.0
```

If you're using *WiFi*, enter this instead:
```text
sudo ifconfig wifi0 [XXX.XXX.XXX.]254 netmask 255.255.255.0
```

Make sure you change `[XXX.XXX.XXX.]` to the first three octets of your current *IP address*.

Now, when running `ifconfig` again, we can see that the changes have applied.

For instance, here, we have changed the *IP address* to `192.168.1.254` for an *Ethernet* connection:

```text
nick@DESKTOP-JLGAKSF:/c/WINDOWS/system32$ ifconfig eth0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.254  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::e919:8718:19b4:5ae  prefixlen 64  scopeid 0xfd<compat,link,site,host>
        ether f4:30:b9:dc:fc:07  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
One of two things will happen:
 - **nothing** - you have swapped to a valid *IP address* within your network.
 - **your Internet connection blows up** - you've either swapped to an *IP address* that is already being used by another device, or to one that is not valid for your network.
 
**Cleanup:**
 - use `sudo ifconfig [connection] [previous-IP] netmask 255.255.255.0` to change your *IP address* back to how it was.
 - run `ifconfig [connection]` again to ensure it has changed back.

#### Windows
**You will need to make a note of your current IP address before attempting this Task.**

Open up **Control Panel** and navigate to the **Network and Sharing Centre**:

![Network and Sharing Centre](https://i.imgur.com/tmT5XCw.png)

From there, click the name of the connection type for your network.

This should be either **Ethernet** or **Wifi (your-Wifi-network-ID)**.

You should see your network status:

![Network Status](https://i.imgur.com/YcYpeYD.png)

Open up the **Properties**, then scroll down until you see the highlighted option below:

![Network Properties](https://i.imgur.com/A900h9A.png)

Finally, open up the **Properties** - the panel will either be blank or filled-out, depending on your network configuration:

![IP Properties blank](https://i.imgur.com/4VAJse3.png)
![IP Properties filled-out](https://i.imgur.com/5q6pZX4.png)

Using the results you gained from the previous Task:
- Type your *IP address*, *subnet mask*, and *default gateway* into the corresponding fields.
- Type `8.8.8.8` into the **'Preferred DNS Server'** field.

Change the fourth octet of your *IP address* to something else, then click **OK**.

One of two things will happen:
 - **nothing** - you have swapped to a valid *IP address* within your network.
 - **your Internet connection blows up** - you've either swapped to an *IP address* that is already being used by another device, or to one that is not valid for your network.

**Cleanup:**
- Re-open the **IP Properties** panel.
- Re-select the **'Obtain an IP address automatically'** and **'Obtain DNS server address automatically'** radio buttons.

### Look at your network's TCP/IP traffic
*For this task, you will need* **Wireshark** *installed on your computer - this is covered in our [Wireshark module series](https://github.com/bob-crutchley/courseware/tree/master/topics/wireshark).* 

Open up Wireshark and use the **display filters** to show TCP and IP traffic on your network:
![TCP & IP](https://i.imgur.com/YBqwwlU.png)

Try it now, but just for the traffic that's going to and from your IP address:
![TCP & IP with IP address](https://i.imgur.com/xYm2l2D.png)
