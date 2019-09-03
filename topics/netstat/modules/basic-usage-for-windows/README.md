# Basic Usage for Windows
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Options on Windows](#options-on-windows)

<!--TOC_END-->
## Overview
Netstat on Windows displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols).
## Options on Windows
Used without parameters, netstat displays active TCP connections.
Typically on Windows CLI tools options are prefixed with `/`.
For instance to use the `a` option you would put `/a`.
This is not the case with netstat; you can use `-`.
An example of using the `a` option would be `-a`.
Here are some of the other available options to use with netstat on Windows:

| Option | Description |
|--------|-------------|
| `-a`      | Displays all active TCP connections and the TCP and UDP ports on which the computer is listening |
| `-e`      | 	Displays Ethernet statistics, such as the number of bytes and packets sent and received. This parameter can be combined with `-s.` |
| `-h`      | Show available options |
| `-n`      | Displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names. |
| `-o`      | Displays active TCP connections and includes the process ID (PID) for each connection. You can find the application based on the PID on the Processes tab in Windows Task Manager. This parameter can be combined with `-a`, `-n`, and `-p`. |
| `-p` | Shows connections for the protocol specified by Protocol. In this case, the Protocol can be tcp, udp, tcpv6, or udpv6. If this parameter is used with `-s` to display statistics by protocol, Protocol can be tcp, udp, icmp, ip, tcpv6, udpv6, icmpv6, or ipv6. |
| `-s` | Displays statistics by protocol. By default, statistics are shown for the TCP, UDP, ICMP, and IP protocols. If the IPv6 protocol is installed, statistics are shown for the TCP over IPv6, UDP over IPv6, ICMPv6, and IPv6 protocols. The -p parameter can be used to specify a set of protocols. |
| `-r` | Displays the contents of the IP routing table. This is equivalent to the `route print` command. |
