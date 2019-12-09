# IP Routing

*(This module relies on a fundamental understanding of the Internet Protocol and IP addresses. We cover both in [the IP module](https://github.com/bob-crutchley/courseware/tree/master/topics/networking/modules/ip).)*

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Casting](#casting)
- [Network Classes](#network-classes)
	- [Usage](#usage)
- [Subnets](#subnets)
	- [CIDR](#cidr)
- [Tasks](#tasks)
	- [Find your IP address and subnet mask](#find-your-ip-address-and-subnet-mask)
		- [macOS, Linux, or Windows Subsystem for Linux](#macos-linux-or-windows-subsystem-for-linux)
		- [Windows](#windows)
	- [Find network information using a subnet calculator](#find-network-information-using-a-subnet-calculator)

<!--TOC_END-->
## Overview
**IP Routing** refers to the way in which information is *redirected* through a network via the **Internet Protocol**.

When routing information through a network, there are several things to take into consideration:
 - **casting** - which devices are we trying to send data to?
 - **network scope** - how many devices can the network support?
 

## Casting
To move data through a network, we have to display that information on the network in some way, so that it reaches where it needs to go.

We call this **casting**, because we attempt to send out the data to somewhere.

For instance, a radio sends data from a single studio to lots of radio sets by *broad*casting its message - it is *casting* its message to a *broad* area of receivers. 

Generally, when data is moving through a network, it is moving towards a *specific* destination, this process is called *unicast*.

**Unicast** aims to deliver a message to *one and only one device*.

However, there are other types of casting which are worth mentioning:

|Type|Usage|
|-|-|
|**unicast**|sends to a **single** receiver|
|**broadcast**|sends to **all** receivers|
|**multicast**|sends to a **subscribed group** of receivers|
|**anycast**|sends to **one out of a group** of receivers (typically the **nearest**)|

The vast majority of IP routing uses **unicast**.

## Network Classes
Routing information relies on an underlying network structure.

Originally, networks were organised according to **classful** architecture.

Classful network design allowed for a larger number of individual networks.

### Usage
The *first three octets* of an IP address determined its class:
```text
   these!
┌────┴────┐
192.168.100.42
```

A network's class was determined by whether these were able to change (*variable*) or not (*static*).

The octets that do not change are the **network prefix**: all devices on that network will start with the same octets every time.

The octets that did change are the **host identifier**: these would change from device to device connected to the network.

For instance, a network with a **network prefix** of `192.168.100` can contain the following devices:
```text
192.168.100.1
192.168.100.2
...
192.168.100.253
192.168.100.254
```

Each class used more octets for the network prefix, making the host identifier smaller and reducing the number of possible host addresses:

|Class|Network ID|Host ID|Networks|Addresses|
|-|-|-|-|-|
|**A**|`a`|`b.c.d`|128|16,777,216|
|**B**|`a.b`|`c.d`|16,384|65,536|
|**C**|`a.b.c`|`d`|2,097,152|256|

(There was an experimental **D-class**, but it is not covered in these modules.)

This way of splitting networks up is known as **subnetting**.

## Subnets
When the dotcom bubble of the early-90s hit, network classes became mostly obsolete as IPv4 addresses depleted. 

By 1993, they had phased out entirely.

The primary reason for this was that using a traditional class format usually resulted in networks having either a *too-broad* or a *too-narrow* broadcast domain.

A network that might have needed hundreds of IP addresses for its devices (like a Wide-Area Network across a city's municipal offices) could be assigned a class which was too limited, making them run out of addresses very quickly.

Meanwhile, a network that might not have needed more than a few devices connected at any given time (like a LAN in a small office) could be given swathes of IP addresses it didn't need.

Subnetting needed to change to be more manageable, and that signalled a move away from the class system.

To facilitate this, the split in IPv4 addresses between the network prefix and the host identifier are utilised, but an extra section of bits is added for clarity: the **subnet identifier**.

### CIDR
Let's consider the following address:
```text
192.168.100.14/24
```

In this case, how can we know which section of bits is the network prefix, and which section refers to the host?

Classful network architecture was replaced by **Classless Inter-Domain Routing (CIDR)** in 1993.

CIDR allows for the dynamic assignment of several IP addresses to a network through a variety of subnets

Instead of the four classes we looked at earlier, there are now 32 different categories to choose from in order to fine-tune the scope of a particular network's broadcast domain.

The section of bits after the address we looked at earlier - the `/24` - is the **subnet identifier**.

The subnet ID then corresponds with a specific 32-bit **subnet mask**.

The subnet ID lets us know how much of the IP address is the network prefix - here, it's the first `/24` bits, or 3 octets.

If we look at the IP address as binary, we can count these 24 bits:
```text
11000000.10101000.01100100    .00001110     /24
└───────────┬───────────┘     └───┬───┘     └┬┘
        network ID             host ID   subnet ID
```

If we convert from binary to octets, we can count the 3 octets:
```text
192.168.100       .14         /24
└────┬────┘       └┬┘         └┬┘
network prefix   host ID    subnet ID
```
As the subnet ID is `/24`, the network prefix is the first 3 octets; `192.168.100`, and doesn't change - it is *static*.

The host ID - the specific 'door number' of the device we're looking at - is `14`, and can change depending on the device we're looking at - it is *variable*.

Therefore, `192.168.100.14` is one of the 254 nodes within the `192.168.100` subnet.

CIDR uses these things to identify the sub-network, within a domain, that a particular node is on:

```text
┌──────┬─────────────┐ ┌──────┬─────────────┐ ┌──────┬───────────────┐ ┌──────┬─────────────────┐
│  ID  │ Subnet Mask │ │  ID  │ Subnet Mask │ │  ID  │  Subnet Mask  │ │  ID  │   Subnet Mask   │
├──────┼─────────────┤ ├──────┼─────────────┤ ├──────┼───────────────┤ ├──────┼─────────────────┤
│ /1   │  128.0.0.0  │ │ /9   │ 255.128.0.0 │ │ /17  │ 255.255.128.0 │ │ /25  │ 255.255.255.128 │
│ /2   │  192.0.0.0  │ │ /10  │ 255.192.0.0 │ │ /18  │ 255.255.192.0 │ │ /26  │ 255.255.255.192 │
│ /3   │  224.0.0.0  │ │ /11  │ 255.224.0.0 │ │ /19  │ 255.255.224.0 │ │ /27  │ 255.255.255.224 │
│ /4   │  240.0.0.0  │ │ /12  │ 255.240.0.0 │ │ /20  │ 255.255.240.0 │ │ /28  │ 255.255.255.240 │
│ /5   │  248.0.0.0  │ │ /13  │ 255.248.0.0 │ │ /21  │ 255.255.248.0 │ │ /29  │ 255.255.255.248 │
│ /6   │  252.0.0.0  │ │ /14  │ 255.252.0.0 │ │ /22  │ 255.255.252.0 │ │ /30  │ 255.255.255.252 │
│ /7   │  254.0.0.0  │ │ /15  │ 255.254.0.0 │ │ /23  │ 255.255.254.0 │ │ /31  │ 255.255.255.254 │
│ /8   │  255.0.0.0  │ │ /16  │ 255.255.0.0 │ │ /24  │ 255.255.255.0 │ │ /32  │ 255.255.255.255 │
└──────┴─────────────┘ └──────┴─────────────┘ └──────┴───────────────┘ └──────┴─────────────────┘
```
We can see, here, that our subnet mask is `255.255.255.0`.

The subnet mask also contains *static* and *variable* octets, which correspond to the static and variable octets in our IPv4 address.

In this case, since `192.168.100` in our IPv4 is static, so is `255.255.255` in our subnet mask.

And, just like `14` is variable in our IPv4 address, so is `0` in the subnet mask.

Therefore, there must be 254 different addresses within our network domain which a connected device can be assigned to:

```text
IPv4 address:       192.168.100.14
Network prefix:     192.168.100.0
Host ID:            14
Subnet ID:          /24
Subnet mask:        255.255.255.0
Available hosts:    254
```

Our network contains every available address from `192.168.100.1` to `192.168.100.254`.

## Tasks

### Find your IP address and subnet mask

#### macOS, Linux, or Windows Subsystem for Linux
Open a terminal and enter the `ifconfig` command, which shows all your machine's *internal network connections*:

If you are on a WiFi network, you will find your IP address and subnet mask under the `wifi0` block:
```text
wifi0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.25.198  netmask 255.255.255.0  broadcast 172.17.25.255
        inet6 fe80::f94e:7ba5:ca3f:2673  prefixlen 64  scopeid 0xfd<compat,link,site,host>
        ether a0:af:bd:df:79:10  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
A similar set of results will appear if you are using Ethernet, under the `eth0` block.

We're interested in the second line:
```text
inet 172.17.25.198  netmask 255.255.255.0  broadcast 172.17.25.255
```
This gives us your internal IP (`inet`) and the subnet mask (`netmask`).

#### Windows
Open a command window and enter the `ipconfig` command, which shows all your machine's *internal network connections*:

The block we're interested in relies on whether you're using WiFi or Ethernet.

For WiFi, the block starting with `Wireless LAN adapter WiFi:` is the one we want:
```text
   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::f94e:7ba5:ca3f:2673%21
   IPv4 Address. . . . . . . . . . . : 172.17.25.198
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 172.17.25.1
```

For Ethernet, the block we want is the one starting with `Ethernet adapter Ethernet:` instead.

Both clearly show our `IPv4 Address` and `Subnet Mask`.

### Find network information using a subnet calculator
For this task, you will use your machine's IPv4 address and subnet mask which you discovered in the previous task.

This will allow you to discover more about your machine's connection to its local network.

Navigate to [this online subnet calculator](https://www.calculator.net/ip-subnet-calculator.html​).

Leave the network class as 'Any', then enter your machine's subnet mask and IP address into the corresponding fields.

Click calculate - you should receive a similar result to the following:

![Subnet calculator information](https://i.imgur.com/BsedIUN.png)
