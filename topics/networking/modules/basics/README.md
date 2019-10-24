# Basics

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Network Characteristics](#network-characteristics)
	- [LAN vs WAN](#lan-vs-wan)
	- [Network Spatial Scope](#network-spatial-scope)
- [The Internet](#the-internet)
	- [The World Wide Web](#the-world-wide-web)
	- [Web access](#web-access)
		- [URLs vs URIs](#urls-vs-uris)
		- [URIs](#uris)
		- [A side note on character-encoding](#a-side-note-on-characterencoding)
		- [URLs](#urls)
	- [IP Addresses](#ip-addresses)
		- [IPv4](#ipv4)
		- [IPv6](#ipv6)

<!--TOC_END-->
## Overview
A network is essentially a web of distributed communication between entities. At the lowest level, networks facilitate the sharing of information. The internal and external transfer of information is crucial for this task.

The most well-known network is the **Internet**, which, though well-known, is often poorly-understood. It arose out of a need for institutions to be accessible to, communicate with, and share information with each other.

## Network Characteristics
There are a number of characteristics by which all networks operate in some capacity:
| Characteristic | |
|-|-|
| High capacity | Can the network support significant amounts of data transfer? |
| Fast speeds | How quickly does data move between nodes? |
| Low latency | How long does data take to move between nodes? |
| High availability | How many nodes can supply the same data? |
| Redundancy | How many backup nodes are there in the case of network failure? |
| Security | How safe is the network's data? Is the architecture secure from attack? |

### LAN vs WAN
Networks are broadly classified into two types: **LAN** (**L**ocal **A**rea **N**etwork) and **WAN** (**W**ide **A**rea **N**etworks).

The key characteristics by which we can differentiate between them are as follows:

| Characteristic | LAN | WAN |
|-|-|-|
| Geographic distribution | Small; used for e.g. university campuses | Large; used for e.g. cities |
| Data transmission rate | Fast; gigabits | Slow; megabits |
| Error rate | Lower; due to local connectivity | Higher; as a result of distribution |
| Communication link | 'In-house'; e.g. coaxial cables, fibre-optics, ethernet | External; e.g. phone lines, microwave links, satellite channels |
| Ownership | Single; usually a single organisation or individual | Multiple; essentially several interconnecting LANs |
| Communication cost | Lower; simpler operation allows for reliability | Higher; some aspects of operation may be leased or unreliable |

These differences show the difference in scale between LAN and WAN - while LAN is a small, interconnected collection of nodes usually operated by a single entity across a small area, WAN connects several LAN together to allow for wider, though less reliable, communication across multiple entities.

### Network Spatial Scope
There are a number of other network types, according to specific circumstances.

The hierarchy of networks might look something like this:

<!--big noice diagram here-->

The following table gives brief explanations of each network type in practice:

| Name | Acronym | Function | e.g. |
|-|:-:|-|-|
| Nanoscale | `nano` | Electromagnetic and molecular data transmission | medical nanotechnology |
| Near-Field Communication | `NFC` | Portable dual-device communication | contactless payment |
| Body Sensor Network | `BSN` | Wearable computing devices | smartwatches, implants |
| Personal | `PAN` | Individual workspace connections | Bluetooth, wireless USB |
| Near-me | `NAN` | Proximity-based connections | mobile technology - masts serve multiple carriers |
| (Wireless) Local | `(W)LAN` | Some institution or individual usage | Ethernet, WiFi |
| Metropolitan | `MAN` | Interconnected LANs in a geographical area via endpoint connections | Silicon Valley |
| Wide | `WAN` | Region-spanning network transmitting data between multiple entities | frame relays |
| Cloud | `Cloud` | Massively distributed, using mutliple data centres in multiple geographic regions as a secure connector of endpoints | GCP, AWS, Azure |
| Internet Area | `IAN` | Direct Cloud-based endpoint connection over IP | (conceptual) |
| Interconnected Network | `Internet` | Global system of interconnected networks | TCP/IP, World Wide Web |

## The Internet
As the largest telecommunications network (its name is literally shortened from **inter**connected **net**work), the Internet is the best example of a WAN taken to its logical extreme. It early form was commissioned by the United States as a way of building robust, fault-tolerant communication between networks, and has exponentially expanded ever since.

As the decentralised and distributed global system of interconnected networks, it uses a series of protocols, most notably the Transmission Control Protcol (TCP) and Internet Protocol (IP), to provide end-to-end data communication to every node which connects to it.

### The World Wide Web
The Internet and the World Wide Web are often conflated expressions, though they are vastly different.

While the Internet is a *networking infrastructure* - a network of networks in which any computer can communicate with another computer - the Web is simply an *information-sharing system* which uses the Internet as its base.

Web services mostly use Hypertext Transfer Protocol (HTTP) to transmit data between nodes, which is usually presented in some form of markup, such as HTTP.

Browsers help to facilitate that data transfer, but the Web itself is one of many vehicles which use the Internet as its basis.

### Web access

#### URLs vs URIs
Accessing data through the Web is facilitated by using a (**U**niform **R**esource **I**ndicator). URI is used for all information which flows across the Web: every Web resource must have a specific string of characters which unambiguously define where that particular object is.

For specific Web pages, a Web address, or URL (**U**niform **R**esource **L**ocator) specifies its location on a computer network and mechanism for retrieving it.

Thus, a URL is simply a more specific type of URI.

#### URIs
The URI generic syntax consists of a hierarchical sequence of five components:
```
  URI = scheme:[//authority]path[?query][#fragment]
```
where the authority component divides into three subcomponents:
```
  authority = [userinfo@]host[:port]
```
As each URI begins with a scheme name that refers to a specification for assigning identifiers within that scheme, URIs can take multiple forms:
```
  ldap://[2001:db8::7]/c=GB?objectClass?one
  └┬─┘   └─────┬─────┘└─┬─┘ └──────┬──────┘
  scheme   authority   path      query
```
```
  mailto:John.Doe@example.com
  └─┬──┘ └────┬─────────────┘
  scheme     path
```
```
  news:comp.infosystems.www.servers.unix
  └┬─┘ └─────────────┬─────────────────┘
  scheme            path
```
```
  tel:+1-816-555-1212
  └┬┘ └──────┬──────┘
  scheme    path
```
```
  telnet://192.0.2.16:80/
  └─┬──┘   └─────┬─────┘│
  scheme     authority  path
```
```
  urn:oasis:names:specification:docbook:dtd:xml:4.1.2
  └┬┘ └──────────────────────┬──────────────────────┘
  scheme                    path
```

#### A side note on character-encoding
Of the ASCII character set, the characters `: / ? # [ ] @` are reserved for use as delimiters of the generic URI components.

If you wanted to use any of these in the 'plaintext' areas of a URI, such as by appending an email address to a URI, they would need to be percent-encoded.

For instance `%3F`may appear in certain sections of a URL for a `?`.

Occasionally, `&` may also appear as `&amp` for similar reasons.

#### URLs
On the other hand, a URL is more specific, and usually conforms a much more varied specification:
```
          userinfo       host      port
          ┌──┴───┐ ┌──────┴──────┐ ┌┴┐
  https://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top
  └─┬─┘   └───────────┬──────────────┘└───────┬───────┘ └───────────┬─────────────┘ └┬┘
  scheme          authority                  path                 query           fragment
```

### IP Addresses

#### IPv4

#### IPv6
