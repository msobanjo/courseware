# Network Architecture

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Network Components](#network-components)
- [Network Diagrams](#network-diagrams)
- [Network Topology](#network-topology)
	- [Bus](#bus)
	- [Ring](#ring)
	- [Star](#star)
	- [Mesh](#mesh)
	- [Tree](#tree)
	- [Hybrid P2P (Peer-to-Peer)](#hybrid-p2p-peertopeer)
- [Tasks](#tasks)
	- [Office Network Topology](#office-network-topology)
	- [Good Network Architecture](#good-network-architecture)

<!--TOC_END-->
## Overview
Since networks are designed as a way for multiple devices to communicate with each other, they need to be organised in some way:
 - what kinds of devices does the network contain?
 - how are the network connections laid out?
 
To answer both of these questions, we map out the **topology** of the network.

When devices are communicating across a network, they are always sharing data.

In larger networks, data is constantly flying around between devices.

Much like letters in a postal system, data is *encapsulated*, or stored, in small chunks called **packets**.

Data that is constantly being moved throughout the network is called **traffic**.

## Network Components
Networks not only contain computers, but several different **components** as well.

Some of these components are visible or usable by an end user, while some simply facilitate the flow of information.

Components in networking terminology are usually referred to as **nodes** - they would typically be devices like: 
- computers
- phones
- tablets

The three fundmaental network components are:

| Component | Role | Function | 
|-|-|-|
| **Router** | Distributor | Forwarding and directing network traffic |
| **Switch** | Middleman | Receiving and processing packets from a router to send to a device |
| **Node** | User | Sending packets to a switch; receiving and processing packets from a switch |

Depending on the network, other components can be encountered, all of which have their own uses:

| Component | Function |
|-|-|
| **Cable** | Direct connectivity between any network components |
| **Signal** |  Wireless connectivity between any network components |
| **Network Interface Controller (NIC)** | Physically receives data from a network |
| **Host adapter** | Connects a host system to other network/storage devices |
| **Gateway** | Allows for data transfer between networks |
| **Network bridge** | Aggregates mutliple networks together |
| **Hub** | Connects multiple devices together onto a single network |

(There are others besides this, but they won't be covered in this module.)

## Network Diagrams
Let's look at an example of the architecture and topology involved within a typical network:

```text
          ┌────────[Router]────────┐
      [Switch A]               [Switch B]
    ┌─────┴─────┐            ┌─────┴─────┐
 [Node 1]    [Node 2]     [Node 3]    [Node 4]────[Node 5]
```

Here, we can see:

- the **Router** is in charge of sending and receiving information from the two **Switches**
- the **Switches** send and receive information sent to them from the **Nodes**
- the **Nodes** both send information to, and receive information from, the **Switches**

Let's say that **[Node 4]** is the device that you're using to read this module.

Your device needs to send information to **[Node 1]**.

To do this, there's a lot that would need to happen:
1. First, your device at **[Node 4]** sends a *data packet* up the network to **[Switch B]**
2. **[Switch B]** receives the packet, then *forwards* it to the **[Router]**
3. The **[Router]** receives the packet and works out that you want to send it to **[Node 1]**
4. The **[Router]** sees that **[Switch A]** is in charge of **[Node 1]**, so it *forwards* the data to it
5. **[Switch A]** receives the packet, then *forwards* it down to **[Node 1]**

There is a lot of room for errors during this process, despite its simplicity.

Let's now say that your device at **[Node 4]** needs to send information to **[Node 3]**.

Since both your device and **[Node 3]** are both connected to **[Switch B]**, it would take less time to transfer the information over.

Finally, let's say that your device at **[Node 4]** needs to send information to **[Node 5]**.

Since your device and **[Node 5]** are directly connected, the information transfer would be even quicker!

## Network Topology
Network **topology** typically refers to the *physical* and *logical* ways in which a network is laid out.

**Physical topology** refers to the actual hardware - wires, computers, routers - of a network, such as those linking computers together in an office builidng.

**Logical topology**, on the other hand, describes how networks without an obvious physical topology - such as in wireless systems like Bluetooth and contactless - link devices together, such as the WiFi in your home. 

Physical network topologies are:
- bus
- ring
- star
- mesh
- tree
- hybrid P2P (Peer-to-Peer)

Due to hardware limitations, most wired networks stuck to one of these physical topologies.

### Bus
```text
      ┌────────┬────────┐
  [Node 1]  [Node 2]  [Node 3]
```
Data passing along a network which uses Bus topology would be received quicker by nodes which are close to the node sending that information.

For instance, if **[Node 1]** sends data intended for **[Node 3]**, it will take a while for that data to pass through all the wires connecting every node together.

As **[Node 2]** is in the 'middle' of the network, it would receive data faster, on average, than the other nodes. 

### Ring
```text
  ┌[Node 1]───[Node 2]┐
  |                   |
  |                   |
  |                   |
  └[Node 3]───[Node 4]┘
```
Ring topology allows for data to circulate through a network in a more even spread than by using a Bus-based system, as each node is connected to two other nodes in the setup.

### Star
```text
  [Node 1] [Node 2]
        \   /
        [Hub]
        /   \
  [Node 3] [Node 4]
```
Star topology makes use of a 'middle' **Hub**, which serves to re-transmit information sent from one node to another which is intended to receive that information.

As information is only sent between each node and the *Hub*, this theoretically stops information from spreading through the network 'in search' of the node it needs to get to.

Instead, the Hub takes control of where information is headed, which allows for greater network speed.

### Mesh
```text
  ┌[Node 1]───[Node 2]┐
  |     \      /      |
  |       ─────       |
  |     /      \      |
  └[Node 3]───[Node 4]┘
```
Mesh topology connects every node, where possible, to every other node in the network, without using a Hub to redirect information.

By connecting every node together, a *Hub* becomes unnecessary, as data will be received just as quickly at any node irrespective of which node it is sent from.

However, larger wired networks of this type may suffer due to the greater number of wires required to connect every node to every other node - for instance, if one wire stops working, it may take a significant amount of time to diagnose which wire it is. 

### Tree 
```text
          ┌────────[Router]────────┐
      [Switch A]               [Switch B]
    ┌─────┴─────┐            ┌─────┴─────┐
 [Node 1]    [Node 2]     [Node 3]    [Node 4]
```
You might recognise this setup!

Tree topology essentially organises several *Star* topologies into a hierarchy.

By doing this, the peripheral 'leaves' (nodes) of the Tree are only required to send and receive information to the switch directly above it.

As a result, rather than have a single *Hub* node, there are muiltiple switches which share responsibility for re-transmitting data, and a single router to facilitate.

### Hybrid P2P (Peer-to-Peer)
As networks have expanded (and become more wireless) over time, most network architectures employ a **Hybrid** system, most commonly based on Tree architecure.

Wireless technology is Hybrid by design: most Internet-enabled devices are so interconnected that both physical and logical network topology has become less relevant.

When we talk about topology today, we only really refer to it when describing two things:
1. **Smaller, wired, or home/office network architecture**
2. **Larger, integrated, wired networks from the pre-wireless age**

Generally, wireless networks are interconnected, or **peer-to-peer (P2P)** networks.

Every node can both send and receive data from every other node.

This eliminates the need for specific routers, hubs, or switches.

## Tutorial
Try to complete the following tasks:

### Office Network Topology
What types of network architecture are where you currently are?

We have spoken about a few different network topologies in this module.

Think about the ways in which devices where you are might link into a network.

You will need to consider the following:
 - Which of each of the network components where you are are connected to a wired network(s);
 - Which of the wireless devices around you are connected to a wireless network;
 - What the topology of each of the networks around you might look like.

### Good Network Architecture
Based on network topology, draw a diagram of what you think a good network architecture might look like.

For this task, you'll need to map out what you think a 'good' network is:
 - You can define 'good' according to your own specification - should it be e.g. more fast, reliable, accurate?
 - You need to specify whether this network is wired or wireless, and why you chose that setup!
