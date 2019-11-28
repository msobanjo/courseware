# PAN & Bluetooth
## Overview
A **Personal Area Network (PAN)** is a network type based on a relatively short-wave, low-power radio frequency.

It reaches slightly further than its more contemporary counterpart, [Near-Field Communication (NFC)](https://github.com/bob-crutchley/courseware/tree/master/topics/networking/modules/nfc/), but far less than a **Wireless Local Area Network (WLAN)**.

## Bluetooth
Bluetooth is the most well-known form of PAN - it was developed as a way of bringing together multiple wireless technologies under a single communication protocol. [This video explains how Bluetooth got its name.](https://www.youtube.com/watch?v=VdmQp9M9jUo)

Bluetooth transmits its signals along the **ISM** frequency band set aside for **i**ndustrial, **s**cientific and **m**edical devices, which operates between 2.402 and 2.480 GHz.

When two Blueooth devices connect, they share a fraction of the ISM band to communicate on.

The request and response forms a small network between the two devices.

The network is so specific that both devices will **blacklist** everything for incoming connections *except* for incoming connections from the other device.

The following **Case Study** will use your device's Bluetooth capabilities to show how it works.

## Tasks
### Case Study: See how PAN works with Bluetooth tethering
*NB: this task will only work with Bluetooth-enabled phones and desktops.*

For this Case Study, turn on Bluetooth discovery on your device, and see how many devices in your local vicinity it picks up.

Connect to another device which is capable of displaying visual information, such as a laptop or a tablet.

Try to send [this image](https://yt3.ggpht.com/a/AGF-l79R65oC-kUKQQii1-zvefpjRvrSYbITqYgD-w=s900-mo-c-c0xffffffff-rj-k-no) across.

(Depending on your device, there may be a specific option to send files via Bluetooth on your phone).

Even if you were to do this in the middle of a crowded street, you would not experience any interference at all.

Bluetooth devices avoid interfering with any other devices by using **spread-spectrum frequency hopping**.

Each device will randomly select 79 different frequencies from a designated range within the ISM band, swapping around which one it uses 1600 times per second.

When you turn on your device's Bluetooth, it will send radio signals asking for a response from any units with an address in a particular range.

Since other devices around have addresses in the range, it responds, and a PAN is formed.

Even if one of these devices should receive a signal from another system, it will ignore it since it's not from within the network.

Combining this method with an extremely weak transmission signal allows for multiple Bluetooth devices to operate in tandem without major interference.

Any two devices which happen to attempt using the same frequency to communicate would only experience issues for a fraction of a second.

Since each PAN hops randomly through the available frequencies, all of the PANs we create within this room are completely separated from one another.

However, if a multitude of Bluetooth devices are operating at the same time in a packed space, the interferences become more obvious when they do arise.

This is why on a packed train, everybody's Bluetooth earbuds will crackle more than usual - though the PANs are prevented from accepting incoming connections from outside the network, the ISM band itself is full of devices with overlapping `frequency ranges.