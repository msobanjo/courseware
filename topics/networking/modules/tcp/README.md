# TCP
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [TCP Header Format](#tcp-header-format)
- [TCP Operations](#tcp-operations)
	- [Connection Establishment](#connection-establishment)
	- [Data Transfer](#data-transfer)
	- [Connection Termination (Graceful Close)](#connection-termination-graceful-close)
- [Tasks](#tasks)
	- [Viewing TCP Packets with Wireshark](#viewing-tcp-packets-with-wireshark)

<!--TOC_END-->
## Overview
Transmission Control Protocol (TCP) is connection-orientated.
This means that there is a handshake to ensure that the data has been delivered correctly.
A logical connection must be established before any transferring of data can begin. TCP uses a 3 way handshake when establishing and terminating a connection, and there is more on this in the TCP operation section.
The reliable nature of TCP means that it is used in application level protocols, such as SSH, FTP and almost anything where all of the data must be transferred.

## TCP Header Format
Every TCP header has 10 required fields and an optional 11th field.
This many fields are needed in a TCP header, because TCP has quite a few capabilities compared to a protocol such as UDP.

1. Source Port – The port from which the packet was sent from
2. Destination Port – The port of the receiving device
3. Sequence Number – The device sending the packets will use sequence numbers to order groups of messages. For instance, an image file that is being transported over multiple messages will need to be reconstructed at the other end in the correct order.
4. Acknowledgement Number – Both the senders and receivers of the messages will use the acknowledgement numbers field to communicate the sequence numbers of the messages that have either been recently received or expected to be sent.
5. Data Offset – Stores the total size of the header
6. Reserved – These are 3 bits for the reserved field. They are unused and are always set to 0.
7. Control Flags – There are six standard and three extended control flags that are used for managing the data flow - more on this in the TCP operation section.
8. Window Size – A way of regulating how much data can be sent, before requiring an acknowledgement to confirm that the data has been received successfully.
9. Checksum – Generated by the sender. A mathematical technique for the receiver to assure the integrity of the data, and to make sure that it has not been corrupted or tampered with.
10. Urgent Pointer – This value is typically set to zero and ignored; however, it can be used in conjunction with one of the control flags, to require priority in processing.
11. Optional Data – Optional data for TCP allows more features, such as support for special types of acknowledgement and window scaling algorithms

![TCP Header](https://lh3.googleusercontent.com/o9ex3p3QMp5ONvsl-rZFnJ7g6K0wdI-CdxgT5qj1Zs-H56gPK3x26p4ijnaxaPn0OcLmBl9MUZkgHzsHNCgtW0YxZ8zB8Pn9APiyNnsfB61HlQq8W3Xicx5pOiXzxRAcHBiXFD0YFa56pr9dJAsyWrgV3otXqjtgomSGOt0gmkGAC7eVnAPmX1cH1WyW3p6nn-lY-UR_WMdkMxyRXaRvr3wBRd5VDnTdSHYU48xHZuAAOmeiIc84zccP2r8axDjPuNIvJ56ge5tOIh3gASN1v5_A9c-N5UAAyjPBuBeFe0obju3hbC0U5tTNNrMBQmgt_brDZzOh2yF3RGYH-9K8Bd0nuJi2ufyv9Unb_bF9MdM-hRTNYPIbSOceSziLGOBwGSyrd1nVtnzDVrlIADcYSg9Lvv4EJePZITkUmrXR3QxKLXU_r69UAj_S3nEBpAKi3KddFxDsuDLN-UCbg0mN5LmhRvnx2nCbIeUkYOvyeQbPE36b4b07xcdY3XQaeVqw-BlTEtV3Ix0wQW3HXUyOfFhhBY-JnaHlmOaU0DLjuPf4n1qidj4zY3ZFgyXuYm1zdWRY2QkYUABa4cQow9yLEv3LU__zmbFTA2D_JUoaoeNlR5OSgcDfcDWLlGZ5Xq4msVvNL_knd5FwM1itrZCKc33eIUhBmOgDofoh4PPz-kdTDG1QFvo4__NOCBJGKLBlO4V5ikqg8d1tNVgNSe94nlmtkp_qkJknOVdTAt7n2ZmAO20n=w1084-h628-no)

## TCP Operations
### Connection Establishment
There is a **three-way handshake** when establishing a new connection with TCP. The control flags are used to communicate which stage the connection establishment is at, and there are two control flags used for establishing a new connection:
- `SYN` – The Synchronisation flag is used in the first request to the remote device. This flag is only ever used in the first packet from the sender and the receiver.
- `ACK` – The Acknowledgement flag is used for acknowledging when a packet has been received successfully.
`SYN-ACK` are used together on the **connection accepted** response from the remote machine, to inform the initial sender that the first packet has been received.
The three-way handshake for a TCP connection establishment is as follows:
1. The client, or local machine, sends a data packet to the remote server with the `SYN` control flag
2. If the packet reaches the remote server (with routing and firewalls correctly configured) then the server will respond with a confirmation receipt with the control flags `SYN`/`ACK`.
3. When the client machine receives the confirmation receipt from the server, it will then respond with an `ACK` packet. Upon the server receiving this, a connection is created and the two machines can now communicate.

![TCP Connection Establishment](https://lh3.googleusercontent.com/6SDc57fgBkSq3s_pbKu-bVXXwDzvGLFxsHObJqr84rlwHvtN3aBEWFeQF3cc3ew3-j2YLICS46THZ1_n8nSYvdSLhDchCt52gGYf4lPEDk5aAeEqMAKLZQrDvpEoOUMthJSfpJupMykh2gC_PES_2vUN2f372qzKOADLDULE3i5kx82Vnc34IbxtpzeBwwtVi1s-cU9KZoqjfhRHgClN78wMVufIUHbeS0KssDOVHJWTgtIM2acrlKkSpSBm3Km5C47c71zwkenaNzPALUA1b48lz1sxQ58iYtLb0bpjkFs5arT1_xz0UDgY0vAtpgs1oE_vHykyHJqKLW3SgBLpYXN6aFlfL24-bdHL7vqg8gwSnWcjDnGEs5ro1gXOQwGpeAhs2UfCzDhwUz4ao5e9yDGc4PhZCW4QQSaiYe3sMKrwAIEGA1gLWL_5zQuHLdca6PPNu0MT5NG2CXo0wBHHjG_LnBJP9DYfP_WaxG_jc2AM1r9e1Nq6ls-rxAnF6Mo2YSN9PQsIuf7mBHeCqmY9KllaIwNtHnfnDo6d0tDLdUp4qQROk2p8Efr3eaXnjl7j7TaCLy42gqKIEca2J7r_P6QvCONDHazKxnv54HGKFudlFpgwaFtvszkm44oPs-eVnQqSeDQQr9UfG1g60BNRWBaFMkQoX9726U40RAMdRQlHDMz5rnjuS_YskTwnMBwIdDos4bhWeIZ1jAlMYz3Un-4aECzMWOzqfwdavYTWn1-IX0Gn=w835-h685-no)

### Data Transfer
Once a TCP connection has been established, data can then be transferred in sequences.
The three main parts to take into consideration with TCP data transfers is the *sequence number*, *acknowledgment number* and the *window size*.
The sequence and acknowledgement numbers are essential for both devices on the connection, to be able to transfer the data in order and reliably.
The window size is important for increasing the overall transfer speed of the data. The server will increase the window size as the connection continues, so that it does not have to reply with acknowledgements as often.
1. The client and server first connect using the 3-way handshake, as shown above.
2. The client sends a packet to the server containing the first sequence of data, and this is data block one of the PNG image. The client now awaits a response from the server.
3. The server responds with an acknowledgement to say that the data for sequence 1 was received correctly. It also gives a window value, to let the client know that they will send another acknowledgement once one more sequence has been received.
4. The acknowledgement is received by the client, and 1 more data sequence is then sent in a packet to the server, including a reference to the acknowledgement that asked for it.
5. Sequence 2 is received by the server and an acknowledgement response is created, with an increased window value this time. The server will now not reply until it has received sequences 3 & 4.
6. The response from the server asking for sequences 3 & 4 fails and does not reach the client. After the timeout period, the client sends the sequence 2 packet again.
7. The server receives the packet for sequence 2 again and then, once again, asks for sequences 3 & 4.
8. This time, the acknowledgement packet from the server reaches the client and the client sends two packets, one for sequence 3 and one for sequence 4.
9. This pattern of sending, acknowledging and increasing the window size continues until there is a connection termination.

![TCP Data Transfer](https://lh3.googleusercontent.com/Oz074lzAMSFv68esdoexOJ4eABpFhUSiR3fqn-Scvv1atC3wrQbY_vey6KAnP4z5wImNwhJlX6jQY_PNHD6fpYvPd7RDt-GCVe28JcalbgUFXHcLs_snA6pzDU6s1dkyNtqRjY9ZEGt7hY552o4LITQVd6bTT5jjh7PJ0I_K8021XQPgMoKuX7s7yqCgZ06fnsiiL6iWtVO40bDeQwKpxuZHaX0x6_4jnclo80X-XMOhniiiUctKieP_gNmBCU4i-APcE-uRK7Zy-6POzMUNiFa1dqZ-pXrEsOCGjb4i0_SkU3G6P76_chDtmgU6GTbdR1_nxvgV0F-tB9GtZXdb8Xld7tUjGyZBlUceEo_FKLlFyxqv28DBUjUezjLDndR0_ZbGAtAjlFDWTIYtJmK-MFgwaoU_gtPQ595U_MkAsUQl_FANeuCt_3pEFEYkXBUWFNtT6tI6R9ykgQ-VsS4GfThe9fCrjkCLJtcf2NxlKrv10spQ3XT89Tvhchvy8WWIhiPinkfkyfgeWCvslRHbXkBQm9CkEXDsOQ8vIrO--4YeYtiKMl0rFSz5cvDHvSB1o7jJENQ3hpCG4pA9PKzRt_eOx2YSrkBWvLMeIbLFWaBRkBR9ACaWS20xKkK-H9sEfrHXCl-HLAwzg5yFiKeP5pF3awq-aAuCEIJmfAP5JZDGM06GE1uB7tT4e3fM5PhKZnDZ0un1hdZXnPO_wHiGu8-WVIljd-h31O-vaN9l4sbFdYLu=w911-h1060-no)

### Connection Termination (Graceful Close)
Here is the process for terminating a TCP connection:
1. The client, or local machine, sends a data packet to the remote server with the `FIN` control flag
2. Once the server recieves the packet, the connection is terminated and a `FIN-ACK` packet is sent back to the client
3. The client server now *acknowledges* the connection termination, by sending an `ACK` packet back to the sever

![TCP Connection Termination](https://lh3.googleusercontent.com/wxM7JkZo60NgRtrhwDXIsG0d96F-yEa1xwh4GxqxgISBipDc6zPSghRhDE4GHyHzgxGi5usW-GUFLFJsgiTZ3wuK-Yh4yeeZeN4IUmgFAriuLawjkbcTbJ9y0q6BFOFINDQYS3UbyzkA549Yh-SOHBC6ctd70sPJ9IzxQNW0RmdMV-81I1Len-DKE_bDGfEKZoMimHzcRI6xNqX76Xz44AwaITc92QAmWYkWB1kszZ9x8tNTs6ehofCZGxijAdk4PmTBppf1UHkfdHp9EU-778_X79bkQ388adIbE2HMz6DEkFmTALPLtNUPg0VXRXZD60GSKkI-toN_lhn-6iEnEyvaqa376hHqPyPUCdJyYbSQnf6tBfzFDxq0ZAb4GpNbfQw4MItn8sWa5Oxzx9vCNmQKtNA_R7G27T-jvlwMjeXhcTe8mEsfw5_L0FCeLeQ-ZxfdgG79hmtkXdmTqWZ6FTPxBOqaOTnVoWRzVPNt3k-jyXlFGJlugJoSNZ0weQmXAAQJr1_UeLQrORK7vEiLhvlU3qy0JwbFAuMs765QU6widCv-bRhQhJtmJX88ccFLCnXZVXJ0ykUWbgw-WxCwDtIuF1Z9jy6Ow8xPZNqg7auJeGj9daID0UTS1qLFRyNMZt_KlxcPdujPUv4Tracblb3jnVeYI2q2W0L1NMUFErEATBhQ9TrvUBr45a4iIgZqqRbzlB3VKaxUEBITMvHYtxZk4As2auk7DrQmUyfpyBcHI91v=w884-h685-no)

## Tasks
For the task below you will need Wireshark installed.
If you are unsure what Wireshark is, or how to use or install it, please have a look at the Wireshark [Introduction Module](/topics/wireshark/modules/introduction)

### Viewing TCP Packets with Wireshark
- We can start by running a brief scan, until some packets come in.
- Once there are some packets there, you can stop the scan and click on one of the packets that has TCP as the protocol.
- On the middle window frame, select the `Transmission Control Protocol` drop down

You should now be able to see information about the TCP packets. See how many of the properties shown in TCP Header diagram you can find here:

![TCP Header](https://lh3.googleusercontent.com/no-MmNGJTMlWVjNTEIyLmBatitBWBXCki0IZaqfJT_gl0NnCJwVByUc5YIPJ6BIPt-HDNQb2cbi5OfNdijVBQkHdQ0FqWrUSRvneMl3bHfi7cq7oVyPTHaTfz_Dz5q65RhFQRESPT0LA6WYLMnpMWErNgtWfLzWzIXSssal6fmCOmwf30dNTCTrs1PKiDkuZT4fxgl2cHIp5vwUAV3WsCRpuiMZ-uB-o1v9UArp2Gpt6W9i0rviT4WDZxopN2kiJu1crn7Ha6dFkQr0E0vgfP4xSiX1naMwPkC6fFr8Ck58Dr3zwvMz6NPl6F3vRfFR04jDGatILzDOO6Z56ExTLKf5eUjNx-FvZUIAqnP3Jo5GSypMz1gqq9p_5r14wYC-ATIlZSOJNrXErkH_cAo1oZYq5E02ah-kZu6wg_XBGmt8zM49YRYrQRkOo37oNrD8fx3Egk41qWyQcx639ebPfA8Yn-r_0R8GlCAGdu_JwWajO1KCn8UwFjy0DZ39vWbJ4LbIG3jTNi1_MorC_BspWYPBejjRjBpD3StOpQkNFbNN_6lbeFELN8T8_q_nzikoBPDUJRyb-8jtcffzPo0SEG2CqhytSURS7eH3iV9ucASKscJdAi7afadAVmf0kFRxxSe6MMRTc4USDhS1kaz1lD5Oe8bHntJJeJ3LJQsTdRuP1XBbCQWm-WAiBXXZlXIxLVMsNnR1XqKdHrwQhjyQD1RwLDZDEzEcTE7MUPZ7DIdW1A4bn=w1179-h1287-no)