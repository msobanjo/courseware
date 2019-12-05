# Network Gateways

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Default Gateway](#default-gateway)
- [NAT](#nat)
- [DNS](#dns)
- [Changing external IP address](#changing-external-ip-address)
	- [VPNs and remote access](#vpns-and-remote-access)
- [Tasks](#tasks)
	- [Find your network's default gateway](#find-your-networks-default-gateway)
		- [macOS, Linux, or Windows Subsystem for Linux](#macos-linux-or-windows-subsystem-for-linux)
		- [Windows](#windows)
	- [Use DNS to convert IP addresses into Web addresses](#use-dns-to-convert-ip-addresses-into-web-addresses)
	- [Find your external IP address](#find-your-external-ip-address)
		- [macOS, Linux, or Windows Subsystem for Linux](#macos-linux-or-windows-subsystem-for-linux-1)
		- [Windows](#windows-1)

<!--TOC_END-->
## Overview
A **network gateway** is a way for a private network to access public networks.

When connecting to the Internet, the packets of information we wish to send outside of our network are sent to the network gateway.

By using this gateway, we can clearly see which data is being sent *externally*.

This is a key component of the **Internet Protocol (IP)**, as without it there would be no way to send information between networks.

## Default Gateway

Let's say we want to send data outside of a private network.

The private network's **network identifier** is this:
```text
192.168.100
```

(This allows for `254` devices to connect to that network with their own unique IP address.)

When any data is addressed to an IP address outside of `192.168.100.X`, it is sent to the network's **default gateway**.

Usually, the address of a default gateway for a network ends in `.1`

Therefore, the default gateway for this network is `192.168.100.1`

## NAT
The default gateway allows for several devices on a private network to connect to a public network at the same time.

**Network Address Translation (NAT)** allows for information to pass between a private network and a public one, such as the Internet, by pointing all devices within that network to pass their data *through* the default gateway.

Let's say we have three devices (**nodes**), all in the same network, looking to access the Internet:

```text
                  Local Network                                    
			Private IPv4: 192.168.100.X                                  Internet
┌───────────────────────┴────────────────────────────┐│┌─────────────────────┴────────────────────┐
                                                      │
 ┌─────[Node]────┐                                    │
 │ 192.168.100.3 ├──┐                                 │
 └───────────────┘  │                                 │
 ┌─────[Node]────┐  │                ┌────────────[Router]────────────┐
 │ 192.168.100.4 ├──┼────────────────┤ Default gateway: 192.168.100.1 ├───────────────────────────>
 └───────────────┘  │                │ External IP:     145.12.131.7  │
 ┌─────[Node]────┐  │                └────────────────────────────────┘
 │ 192.168.100.5 ├──┘                                 │
 └───────────────┘                                    │
                                                      │
```

The nodes are all contained within a local network with a network identifier of `192.168.100`

Each of them have a **internal IP address** within this network of `192.168.100.X`

The router redirects data from all nodes in the network to its **default gateway** of `192.168.1.1`

NAT translates the information to an **external IP address** through the default gateway, allowing the data to access any external IP address.

## DNS
Once a device is connected to the Internet, the user will, most likely, type in some URL to visit:
```text
https://example.com/
```

For the purposes of this tutorial, this is the website's **host name**.

The **Domain Name System (DNS)** is used to convert a device's host name into an IP address which another device can understand.

For example, if a device needs to communicate with `example.com`, it will need the IP address for `example.com`. (It doesn't matter whether it's IPv4 or IPv6 in this case.)

It is the job of DNS to convert the host name to the IP address of the web server.

DNS is, essentially, a massive directory of web addresses - it converts a website's name that people know to a number that the Internet actually uses.

The command `ping` allows us to see DNS in action:
```text
C:\WINDOWS\system32>ping example.com

Pinging example.com [93.184.216.34] with 32 bytes of data:
Reply from 93.184.216.34: bytes=32 time=76ms TTL=51
Reply from 93.184.216.34: bytes=32 time=79ms TTL=51
Reply from 93.184.216.34: bytes=32 time=76ms TTL=51
Reply from 93.184.216.34: bytes=32 time=80ms TTL=51

Ping statistics for 93.184.216.34:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 76ms, Maximum = 80ms, Average = 77ms
```

We can see the IP address (IPv4 in this case) for `example.com` is `93.184.216.34`

## Changing external IP address
**IP-based geolocation** is the mapping of an issued IP address to the location in which the server that a particular node is connected to. 

While this is sometimes useful - such as for querying the location of a central web server which a particular node is connected to, or for **Global Positioning System (GPS)** location on mobile devices - there are cases in which changing a node's perceived location can be beneficial.

### VPNs and remote access
A **Virtual Private Network (VPN)** is used to extend a private network across a public network.

This allows for devices to send and receive data on a public network *as though they were directly connected to a private network*.

VPNs were developed as a way to allow **remote access** to users.

Remote access eliminates the need for a user to use a machine that is directly connected to an network.

For instance, people working for large organisations could use a VPN to access corporate applications and resources.

In terms of security, the connection to a private network is established through an encrypted layered **tunneling protocol**; the VPN user then authenticates themselves so as to gain access to the network.

In recent times, most individuals with a VPN use them for a number of reasons:
 - **Privacy** - it is commonly believed that **Internet Service Providers (ISPs)** are able to view the history of every website that was visited by each of its users; using a VPN arguably obfuscates this information.
 - **Security** - as a VPN extends a private network across a public system through an encrypted tunnel, they act as an extra measure when accessing sensitive information; some VPNs may themselves be encrypted.
 - **Anonymity** - a VPN can be used as a **proxy server**, which acts as an intermediary layer between a user's client and the servers they access. 
 - **Geo-spoofing/anti-censorship** - VPN companies usually host their servers in locations which have more lax Internet restrictions, such as for video- and music-streaming, than the countries they market their service to; these users connect to the VPN in order to spoof their location so as to appear as though they are accessing Web services from the location of these servers.

VPNs are less powerful than most of the general public believe, for a number of reasons. [This video explores some of the more common misconceptions surrounding VPNs.](https://www.youtube.com/watch?v=WVDQEoe6ZWY)

## Tasks

### Find your network's default gateway

#### macOS, Linux, or Windows Subsystem for Linux
In UNIX-based systems, using `ip route` will list every network on our system.

We can pipe the default information to a `grep` to find what we need.

Open a terminal and enter the following command:
```shell script
ip route | grep default
```

You should see the *IP routing table*, where you'll find the gateway that your device is connected to:

```shell script
nick@DESKTOP-JLGAKSF:/c/WINDOWS/system32$ ip route | grep default
none default via 192.168.1.254 dev eth0 proto unspec metric 256
none default via 172.17.25.1 dev wifi0 proto unspec metric 0
```

Here we can see the two gateways a device has for WiFi (`wifi0`) and Ethernet (`eth0`).

#### Windows
In Windows, using `ipconfig` will list out every network on our system.

We can pipe the result set to a `findstr` to find the network gateway.

Open a command terminal and enter the following command:

```text
ipconfig | findstr "Gateway"
```

This should give the current gateway for our system:

```text
C:\WINDOWS\system32> ipconfig | findstr "Gateway"
   Default Gateway . . . . . . . . . : 172.17.25.1
```

### Use DNS to convert IP addresses into Web addresses
Using the *Domain Name Service (DNS)*, convert these external IP addresses into their Web equivalents:

```text
104.199.64.136
```
```text
151.101.0.67
```
```text
78.129.229.95
```
```text
194.61.183.124
```

### Find your external IP address
We can use a DNS request to find our public external IP address.

#### macOS, Linux, or Windows Subsystem for Linux
In UNIX systems this can be done with the `dig` command.

Open a terminal and enter the following command:

```shell script
dig +short myip.opendns.com @resolver1.opendns.com
```

This uses the DNS server at `resolver1.opendns.com` to resolve the myip.opendns.com host name to our external IP address.

#### Windows
We can use a DNS request in Windows too with a slightly different command: 

```text
nslookup myip.opendns.com. resolver1.opendns.com
```

This should return the DNS server's IP address as well as our own:
```text
C:\WINDOWS\system32>nslookup myip.opendns.com. resolver1.opendns.com
Server:  resolver1.opendns.com
Address:  208.67.222.222

Non-authoritative answer:
Name:    myip.opendns.com
Address:  164.39.75.108
```
