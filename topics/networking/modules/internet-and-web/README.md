# The Internet & The Web

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [The Interconnected Network](#the-interconnected-network)
	- [The World Wide Web](#the-world-wide-web)
	- [Web access](#web-access)
		- [URI](#uri)
		- [URL](#url)
		- [Encoding](#encoding)
- [Tasks](#tasks)
	- [Categorise each section of a long URL](#categorise-each-section-of-a-long-url)
	- [Explain why URL identifiers might change](#explain-why-url-identifiers-might-change)
	- [Try sending a text to an email address](#try-sending-a-text-to-an-email-address)

<!--TOC_END-->
## Overview
A **network** is essentially a web of distributed communication between entities.

At the lowest level, networks facilitate the sharing of information.

So far, previous modules covered **internal** transfer of information across a *single network*.

However, information can be exchanged between entirely separate networks.

There is a requirement for the networks to be connected with each other, before they can share the information.

Therefore, the **external** transfer of information is just as crucial for allowing communication between entities.

## The Interconnected Network
The most well-known *network* is the **Internet**, which, though well-known, is often poorly-understood.

As the largest telecommunications network *internet* (name is an abbreviation of **inter**connected **net**work), the *internet* is the best example of a WAN taken to its logical extreme.

It arose out of a need for institutions to be accessible to, communicate with, and share information with each other.

Its early form was commissioned by the United States as a way of building robust, fault-tolerant communication between networks, and has exponentially expanded ever since.

As the decentralised and distributed global system of interconnected networks, it uses a series of protocols to function, most notably:
 - **T**ransmission **C**ontrol **P**rotocol **(TCP)** 
 - **I**nternet **P**rotocol **(IP)**
 
 The combination of these results in **TCP/IP**, which serves to provide end-to-end data communication to every device that uses it.

### The World Wide Web
Contrary to popular belief, the Internet and the **World Wide Web** are not the same thing:
 - The **internet** is a *networking infrastructure* - a 'network of networks' in which any computer can communicate with another computer.
 - The **WWW web** is an *information-sharing system* which uses the *internet* as its base.

Web services mostly use **H**yper**T**ext **T**ransfer **P**rotocol **(HTTP)** to transmit data.

**Web Browsers** help to facilitate that data transfer, by displaying **Web pages**.

Web pages are nearly always written in **H**yper**T**ext **M**arkup **L**anguage **(HTML)**.

However, the Web itself is only one of many vehicles which use the *internet* as its basis.

### Web access
Everything on the *Web* has its own unique address. 

In order to access that data, you will need that address to do it.

Every *web address* adheres to the same standard: **U**niform **R**esource **I**ndicators **(URI)**.

Just like postal addresses, every *Web* resource must have a specific string of characters which unambiguously define where that particular object is.

#### URI
*URI* syntax consists of a hierarchical sequence of five components:
```text
  scheme :// [authority] path ? [query] # [fragment]
```
Where the authority component divides into three sub-components:
```text
  [userinfo] @ host : [port]
```
Each *URI* begins with a **scheme**, and is followed by any **identifiers** which can be within that scheme.

Depending on the **scheme**, a URI can take multiple forms:
```text
  mailto:John.Doe@example.com
  └─┬──┘ └────┬─────────────┘
  scheme     path
```
```text
  tel:+1-816-555-1212
  └┬┘ └──────┬──────┘
  scheme    path
```
```text
              host    port
           ┌────┴───┐ ┌┴┐
  telnet://192.0.2.16:800/example-1
  └─┬──┘   └─────┬──────┘ └───┬───┘
  scheme     authority      path
```

#### URL
URLs are used when referring to specific **Web pages**, and act like page numbers might in a book.

Because of the sheer number of Web pages that exist, URLs conform to a more varied specification than URIs:
```text
          userinfo       host      port
          ┌──┴───┐ ┌──────┴──────┐ ┌┴┐
  https://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top
  └─┬─┘   └───────────┬──────────────┘└───────┬───────┘ └───────────┬─────────────┘ └┬┘
  scheme          authority                  path                 query           fragment
```

#### Encoding
Of the ASCII character set, the characters `: / ? # [ ] @` are reserved for use as **delimiters**.

These allow for URL identifiers to give more information about the page being accessed.

However, if you needed to use any of these characters in **plaintext** ('as-is'), they would need to be percent-encoded:

```text
https://en.wikipedia.org/wiki/Port_%28computer_networking%29
```

```text
https://en.wikipedia.org/wiki/Romeo_%2B_Juliet
```

## Tasks

### Categorise each section of a long URL
For this task, navigate to [this](https://www.smile.amazon.co.uk/gp/product/B07HRHM8F3/ref=ox_sc_saved_title_1?smid=A3P5ROKL5A1OLE&psc=1) Amazon item listing.

### Explain why URL identifiers might change 
The URL in the previous exercise looks like this:
```text
https://www.smile.amazon.co.uk/gp/product/B07HRHM8F3/ref=ox_sc_saved_title_1?smid=A3P5ROKL5A1OLE&psc=1
```
When you open this link in your browser, some of it will change. Why do you think this is?

Categorise the URL you are directed to into its constituent parts. What is each section of the URL doing? 

### Try sending a text to an email address
*For this task, you will need a functioning device capable of using the* **M**ultimedia **M**essage **S**ervice **(MMS)** *to send texts.*

It is possible, thanks to the way URI works, to send a text to an email address.

Usually, your mobile service provider will convert your text to an email and send it for you.

You'll need to set the contact to send a message to as some email, such as your personal email address.

Navigate to your personal email (it may take a couple of minutes) and you should have received your message.
![MMS to email new](https://i.imgur.com/B14sMMj.png)

Take a look at the sender field. What is happening here?
![MMS to email open](https://i.imgur.com/035MlFw.png)
