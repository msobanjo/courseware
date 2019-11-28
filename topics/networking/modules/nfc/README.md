# NFC

## Overview
**Near-Field Communication (NFC)** is a type of network designed for very small scenarios.

NFC utilises a small chip - usually embedded within something like a card, a mobile phone or a ring - which responds to a request sent by another chip embedded within a network-enabled device.

The following **Case Study** uses an identity tag to see how this works in practice.

## Tasks
### Case Study: See how NFC works with NFC Tools
*NB: this task will only work on NFC-enabled phones - if you can use contactless with your phone, then you can try this Task.*

Here, we can see an example of NFC in-action using the *NFC Tools* app ([Apple](https://apps.apple.com/us/app/nfc-tools/id1252962749) / [Android](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc&hl=en_US)).

Once it's installed, try holding your identity tag to your phone's NFC reader.

You should see some pretty cool info pop up in the app - your tag's info should be very similar:

![NFCTools tag response](https://i.imgur.com/0G2z7SP.jpg)

When you raise your tag to an NFC reader, like the reader on the door to the academy, it creates a small, but very specific network connection which allows the door to open.

This tag's network protocol is `ISO-14443-3A`, and follows these steps every time it comes into contact with an NFC reader:

![ISO-14443-3A activation](https://www.dummies.com/wp-content/uploads/tag-activation.jpg)

The door reader is a **Proximity Coupling Device (PCD)**, while the tag is a **Proximity Inductive Coupling Card (PICC)**.

1. The door reader sends a radio signal to its immediate proximity, using a 7-bit command called a **Request (REQA)**.
2. The chip embedded within the card is given the tiny amount of energy needed from that Request to send back its own signal - an **Answer to Request (ATQA)** block. Our ATQA block contains a single command: `0x0002`, and the tag's **Unique Identifier (UID)**.
3. A collision - where two or more tags respond to the door reader - may occur if there is more than one card in range. If a collision happens, the door reader will send out a **SELECT** request which includes a portion (**prefix**) of one of the tags' specific UIDs.
4. If collisions still happen, the door reader will send out more and more specific SELECT signals, using longer UID prefixes, until only one tag responds.
5. The selected tag will then respond with a **Select Acknowledgement (SAK)**, which activates the door reader. Our SAK contains the command `0x18`, which in this case will deactivate the electromagnets holding the door closed.
6. The door reader will continue to be activated until it receives a **HALT** command from the tag. In our case, this happens within a second of the SAK being transmitted. 