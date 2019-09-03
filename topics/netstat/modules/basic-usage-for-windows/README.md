# Basic Usage for Windows
<!--TOC_START-->
### Contents
- [Overview](#overview)

<!--TOC_END-->
## Overview
Netstat on Windows displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols).
## Options on Windows
Used without parameters, netstat displays active TCP connections.
Here are some of the other available options to use with netstat on Windows:
| Option | Description |
|--------|-------------|
| -a      | Displays all active TCP connections and the TCP and UDP ports on which the computer is listening |
| -e      | 	Displays Ethernet statistics, such as the number of bytes and packets sent and received. This parameter can be combined with `-s.` |
| -n      | Displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names. |
