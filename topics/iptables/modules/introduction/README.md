# Introduction
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Concepts](#concepts)
	- [Tables](#tables)
	- [Chains](#chains)
	- [Rules](#rules)
		- [Targets](#targets)
- [Installation](#installation)
	- [Ubuntu/Debian](#ubuntudebian)
	- [CentOS/RHEL](#centosrhel)

<!--TOC_END-->
## Overview
Iptables is a command line utility for configuring Linux kernel firewall.
Iptables is used to inspect, modify, forward, redirect, and/or drop IP packets.
The code for filtering IP packets is already built into the kernel and is organized into a collection of tables, each with a specific purpose. 
## Concepts
Here are three main concepts about iptables:
### Tables
By default there are three tables in the kernel that contain sets of rules:
- The `filter` table is used for packet filtering.
- The `nat` table is used for address translation.
- The `mangle` table can be used for special-purpose processing of packets.
### Chains
Series of rules in each table are called a chain.
A table can have more than one chain.
### Rules
All of the packet filtering is based on rules.
Rules are conditions which can match packets; all the conditions must be met for the rule to apply.
Some of the things that a rule will usually match are what network interface the packet arrived on (`eth0` for example), what type of packet it is (`ICMP`, `UDP`, `TCP` for example) and the destination port (`80` or `9000` for example).
A `target` must also be specified for when these conditions are met which basically decides what is going to happen to the packet.
#### Targets
Targets can be a user-defined chain or one that already exists.
Some of the built in targets are `ACCEPT`, `DROP`, `QUEUE` and `RETURN`; which are the ones that you will be most likely to use.
## Installation
Iptables actually comes preinstalled on many popular Linux distributions.
If iptables isn't installed then you can use the following to install it for your operating system:
### Ubuntu/Debian
```bash
sudo apt install -y iptables
``` 
### CentOS/RHEL
```bash
sudo yum install -y iptables
```
