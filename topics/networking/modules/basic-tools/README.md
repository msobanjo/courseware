# Basic Networking Tools

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [`nslookup`](#nslookup)
	- [`ping`](#ping)
- [Tasks](#tasks)
	- [Use `nslookup` to find the IP of a website](#use-nslookup-to-find-the-ip-of-a-website)
	- [Use `ping` to query a site using its IP address](#use-ping-to-query-a-site-using-its-ip-address)
	- [Disconnect your machine during a `ping` request](#disconnect-your-machine-during-a-ping-request)

<!--TOC_END-->
## Overview 
Two of the most basic tools for seeing networking in action are:
- **nslookup**
- **ping**

Both are lookup tools which check the availability of a host.

### `nslookup`
`nslookup` (**n**ame **s**erver **lookup**) is a network administration tool on the command-line, which directly queries the Domain Name System (DNS) to obtain domain name or IP address mapping.

Here, we can check for the **IP address** of a particular Web site using `nslookup`:

```cmd
  C:\Windows\system32>nslookup example.com
  Server:  dns.google
  Address:  8.8.8.8

  Non-authoritative answer:
  Name:    example.com
  Addresses:  2606:2800:220:1:248:1893:25c8:1946
            93.184.216.34
```

In order to invoke `nslookup`, you need to call it by name (nslookup) in the terminal and pass in a web address (example.com) as an argument to get the information back.

*nslookup* is used in the same way on Windows and Linux operating systems and usually comes pre-installed.

This gives us some useful information about `example.com`:

- The server which `example.com` is hosted on, which is under Google's DNS jurisdiction at `dns.google`
- Its IPv4 address, which is `93.184.216.34`
- Its IPv6 address, which is `2606:2800:220:1:248:1893:25c8:1946`

The `non-authoritative answer` we see just tells us that `nslookup` is querying DNS records kept on external servers, rather than pinging the entire global DNS system directly.

The two IP addresses refer to the Internet Protocol we mentioned earlier, and just shows us the unique location of a resource (in this case, the `example.com` Web site) across the entire Internet.

More information on IP addresses can be found in the [IP Module](../ip/README.md).
<!--issue-415-->

### `ping`
`ping` is a networking utility which is used to test the reachability of a host on the Internet.

It works as a 'there and back again' tool, by measuring the amount of time it takes for a short message to be sent from the source host to a destination host and echoed back again.

`ping` works by sending an **echo request** packet through the **Internet Control Message Protocol (ICMP)** to the destination host, and waiting for a reply.

We can use `ping` to query an IP address so as to check its availability:

```cmd
  C:\Windows\system32>ping 93.184.216.34
```

We could also indirectly ping the URL `example.com`:

```cmd
  C:\Windows\system32>ping example.com
```

We receive two outputs.

The first output is a response to each ping we send to `example.com` (a standard `ping` request pings the server 4 times) in the form of a small **packet** of data:

```cmd
  Pinging 93.184.216.34 with 32 bytes of data:
  Reply from 93.184.216.34: bytes=32 time=81ms TTL=51
  Reply from 93.184.216.34: bytes=32 time=79ms TTL=51
  Reply from 93.184.216.34: bytes=32 time=78ms TTL=51
  Reply from 93.184.216.34: bytes=32 time=78ms TTL=51
```

The second output counts the packets successfully sent and received, and counts any that might be lost.

The output of a successful `ping` request typically looks like this:
```cmd
  Ping statistics for 93.184.216.34:
      Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
  Approximate round trip times in milli-seconds:
      Minimum = 78ms, Maximum = 81ms, Average = 79ms
```

Occasionally, due to network failures or other connectivity issues, requests may simply fail to be sent from a node or received by a server.

A failed `ping` request typically looks like this:
```cmd
  C:\Windows\system32>ping en.wikipedia.org

  Pinging dyna.wikimedia.org [91.198.174.192] with 32 bytes of data:
  Request timed out.
  Request timed out.
  Request timed out.
  Request timed out.

  Ping statistics for 91.198.174.192:
      Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
```

This is an excellent way to check whether a server is 'up' or 'down', as well as average connection speeds between your machine and the server.

## Tasks

### Use `nslookup` to find the IP of a website
*This task requires the use of `nslookup` inside your machine's command line interface (CLI).*

Use this to find the IP addresses for Amazon, Google, Facebook and Outlook.

### Use `ping` to query a site using its IP address
*This task requires the use of `ping` inside your machine's CLI.*

Use the IP addresses you gained from the previous task to find the DNS which each of the four sites are using. What do you notice? 

### Disconnect your machine during a `ping` request
*This task requires the use of `ping` inside your machine's CLI.*

Try to `ping` any of the IP addresses from the previous tasks, but either click `CTRL + C`, remove your Ethernet cable or deactivate your WiFi during the process. What happens?
