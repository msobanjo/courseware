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
- [Tasks](#tasks)
	- [View Current Rules](#view-current-rules)
- [Allow for SSH Connections](#allow-for-ssh-connections)
	- [Default Polices](#default-polices)
	- [Saving](#saving)

<!--TOC_END-->
## Overview
Iptables is a command line utility for configuring Linux kernel firewall.
Iptables is used to inspect, modify, forward, redirect, and/or drop IP packets.
The code for filtering IP packets is already built into the kernel and is organized into a collection of tables, each with a specific purpose. 

When using the `iptables` command you will need to be either prefixing commands with `sudo` or be logged in as the `root` user.

## Concepts
### Tables
By default there are three tables in the kernel that contain sets of rules:
- The `filter` table is used for packet filtering; this is the table that you will likely be using the most. Think of this table as the default table.
- The `nat` table is used for address translation.
- The `mangle` table can be used for special-purpose processing of packets.
### Chains
Series of rules in each table are called a chain.
A table can have more than one chain.
#### Filter Table Chains
The `filter` table has 3 chains: `INPUT`, `FORWARD` and `OUTPUT`.
The route table is what decides on which chain incoming packets go to.
Rules can be added to the different chains to `ACCEPT`, `DROP` packets; more on this in the rules section.
```text
                                      Kernal
    ,-----------------------------------------------------------------------,
    |                                                                       |
    |                                                                       |
    |                       ,------> FORWARD -------------------------------->
    |                       |                                               |
------> Incoming Packet --> Route?                                          |
    |                       |                                               |
    |                       `------> INPUT --- Local Process ---> OUTPUT ---->
    |                                                                       |
    |                                                                       |
    `-----------------------------------------------------------------------`
```
### Rules
All of the packet filtering is based on rules.
Rules are conditions which can match packets; all the conditions must be met for the rule to apply.
Some of the things that a rule will usually match are what network interface the packet arrived on (`eth0` for example), what type of packet it is (`ICMP`, `UDP`, `TCP` for example) and the destination port (`80` or `9000` for example).
A `target` must also be specified for when these conditions are met which basically decides what is going to happen to the packet.
#### Targets
A Target (also known as a jump) can be a user-defined chain or one that already exists.
A couple of the built in targets are `ACCEPT`, `DROP`; which are the ones that you will be most likely to use.

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
## Tasks
Here we'll setup a basic chain for using SSH on a machine.
Be very careful when following the instructions; if you are using a remote machine over SSH for this, there is a chance you can block yourself out if the commands below aren't entered correctly.

In the unlikely case you do get locked out of the machine, you can just restart it to gain access again.
### View Current Rules
Try running `sudo iptables -v -L` to view the current chains and rules in place.
You should see that there aren't any rules made; a similar output to this:
```text
Chain INPUT (policy ACCEPT 28 packets, 2550 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 18 packets, 2286 bytes)
 pkts bytes target     prot opt in     out     source               destination 
```
## Allow for SSH Connections
We are going to give access to SSH first before creating the default rules to deny all so that we won't be locked out incase you are working on a remote machine.
The SSH protocol uses TCP port `22`, so we will allow access to this machine on port `22`:
```bash
sudo iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
```
To make sure that the rule has been added you can run `sudo iptables -L -v`; you'll be able to see the new rule under the `INPUT` chain:
```text
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination
   86  7352 ACCEPT     tcp  --  any    any     anywhere             anywhere             tcp dpt:ssh

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 44 packets, 5184 bytes)
 pkts bytes target     prot opt in     out     source               destination
```
### Default Polices
It's best practice to have default rules in place to deny all traffic; we can then create rules with a higher priority to allow certain connections.
```bash
# by default, deny access to all incoming packets
sudo iptables -P INPUT DROP

# don't forward any packets
sudo iptables -P FORWARD DROP

# allow any outgoing packets by default
sudo iptables -P OUTPUT ACCEPT

# allow all connections within the same machine
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
```
When you run `sudo iptables -L -v` again you should now see that the default policies on the chains have changed.
The `INPUT` and `FORWARD` chains will now `DROP` all packets by default:
```text
Chain INPUT (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
  162 13240 ACCEPT     tcp  --  any    any     anywhere             anywhere             tcp dpt:ssh
    0     0 ACCEPT     all  --  lo     any     anywhere             anywhere            

Chain FORWARD (policy DROP 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 34 packets, 5832 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  any    lo      anywhere             anywhere 
```
### Saving
At this point you would typically save the changes we made.
If you don't save then the changes made would be erased on a system reboot (which is good if you locked yourself out).
To save the changes run:
```bash
sudo iptables-save
```
