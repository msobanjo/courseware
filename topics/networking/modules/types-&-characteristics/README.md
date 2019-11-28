# Network Types and Characteristics

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Network Types](#network-types)
	- [Network Characteristics](#network-characteristics)
	- [LAN vs WAN](#lan-vs-wan)
- [Tasks](#tasks)
	- [How can a network exhibit good characteristics?](#how-can-a-network-exhibit-good-characteristics)
	- [How might a network be inefficient?](#how-might-a-network-be-inefficient)
	- [Think about LAN and WAN use cases](#think-about-lan-and-wan-use-cases)

<!--TOC_END-->
## Overview
Networks come in many forms, depending on the situation in which you'd want to use them.

Usually, the network type to use is determined by how big it needs to be:
 - **physically** - how many devices are going to be connected together at once?
 - **logically** - how much data is going to be moving around the network at once?
 - **geographically** - how far does data need to be transmitted?

Some networks might also require the usage of specific hardware or transmission standards.

## Network Types
The **type** of a network usually relies on how much physical space it covers.

This makes it easy to explore the differences between the networks we use on a regular basis.

The smallest networks area may only extend for a few nanometres, while the largest networks stretch over the entire planet.

From smallest to largest, the following table gives brief descriptions and examples for some common network types:

| Name | Acronym | Function | e.g. |
|-|:-:|-|-|
| **Nanoscale** | `nano` | Electromagnetic and molecular data transmission | medical nanotechnology |
| **Near-Field Communication** | `NFC` | Portable dual-device communication | contactless payment |
| **Body Sensor Network** | `BSN` | Wearable computing devices | smartwatches, implants |
| **Personal** | `PAN` | Individual workspace connections | Bluetooth, wireless USB |
| **(Wireless) Local** | `(W)LAN` | Some institution or individual usage | Ethernet, WiFi |
| **Wide** | `WAN` | Region-spanning network transmitting data between multiple entities | "the Cloud", frame relays |
| **Interconnected Network** | `Internet` | Global system of interconnected networks | TCP/IP, World Wide Web |
| **Global Positioning System** | `GPS` | Global orbital geolocation through satellites | SatNav, Google Maps |

(There are several other network types, but they are not covered in these modules.)

### Network Characteristics
Networks always operate on the basis of providing seamless interconnectivity between devices.

The efficiency of a network can be measured through the following six characteristics:

| Characteristic | |
|-|-|
| **High capacity** | Can the network support significant amounts of data transfer? |
| **Fast speeds** | How quickly does data move between nodes? |
| **Low latency** | How long does data take to move between nodes? |
| **High availability** | How many nodes can supply the same data? |
| **Redundancy** | How many backup nodes are there in the case of network failure? |
| **Security** | How safe is the network's data? Is the architecture secure from attack? |

### LAN vs WAN
We can see how efficient a network is by checking it against these characteristics.

By doing this, we can determine which type of network should be used in particular situations.

Given the size differences between networks, we can generalise networks into two types:
 - small-scale - a **L**ocal **A**rea **N**etwork **(LAN)**
 - large-scale - a **W**ide **A**rea **N**etwork **(WAN)**

If we apply the characteristics from earlier, we can check how well these network types perform in different use cases:

| Characteristic | Use Case | LAN | WAN |
|-|-|-|-|
| **High Capacity** | **Geographic distribution** | Small; used for e.g. university campuses | Large; used for e.g. cities |
| **Fast Speeds** | **Data transmission rate** | Fast; gigabits | Slow; megabits |
| **Low Latency** | **Error rate** | Lower; due to local connectivity | Higher; as a result of distribution |
| **High Availability** | **Communication link** | 'In-house'; e.g. coaxial cables, fibre-optics, ethernet | External; e.g. phone lines, microwave links, satellite channels |
| **Redundancy** | **Communication cost** | Lower; simpler operation allows for reliability | Higher; some aspects of operation may be leased or unreliable |
| **Security** | **Ownership** | Single; usually a single organisation or individual | Multiple; essentially several interconnecting LANs |

These differences help to explain the difference in scale between *LAN* and *WAN*:
 - *LAN* is a small, interconnected collection of nodes, usually operated by a single entity, across a small area
 - *WAN* connects several *LAN* together to allow for wider, though less reliable, communication across multiple entities

## Tasks

### How can a network exhibit good characteristics?
Think about the six characteristics which a network should be able to exemplify.

What do you think each characteristic would look like within a network which used *good practice*?

In other words, how can a network be very good at displaying each characteristic?

### How might a network be inefficient?
How can a network fail to exemplify each characteristic?

What makes a network difficult to use for an end user, and how is this *bad practice*?

### Think about LAN and WAN use cases
Think of a few cases where it would be better to use LAN and WAN.

When choosing between the tweo network types, you will need to consider:
 - the *characteristics* of each network
 - the *physical* size of the network
 - the *logical* size of the network
 - the *geographical* area the network will cover

### Find your machine's GPS location
Navigate to [this IP geolocation finder](https://www.iplocation.net/find-ip-address).

Which address, for which node, is this service using to locate your machine?
