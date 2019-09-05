# Frames
## Overiew
Devices on a network send and receive Packetized Data in discrete chunks called frames.
Frames can hold a maximum of 1500 bytes, or 12000 bits, while it won’t be necessary to remember this number exactly, it is important to understand that frames cannot hold a lot of data.
For instance if a MP3 file is 4MB, that is 4,194,304 bytes so many frames will need to be transmitted to transfer the entire file.

## Incoming and Outgoing Frames
Data comes down from applications such as a Web browser and into the Network Interface Card (NIC).
The NIC then creates a frame using this data and sends it into the network to reach the destination device.
Incoming frames from the network are first checked to see if they are intended for the card.
The data is then processed for the application running on the system and sent to it.
All used and unwanted frames are discarded.

![Incoming and Outgoing Frames](https://lh3.googleusercontent.com/NpIQqDTiCzRZSeTXQ3j8N5832ewq2DKz559cwyYNfxU0WWo7UN1groARYNZwgaj-y-G1MTZcE13HzNQPQ4cyeRFUdOqgpFukLzsdYT8YtK4Zh07hojC_pS7ncQCiUhnDr5vCc_dSbC1kFfTcON5HJZcLePtZDzXS9SBoywxPUBHpIuIjAN19X2Fk3dk01MAOoxqwo_WhM2QLntbl97PuuAnRTxeBOUU6ENgks5D8nXPDMs4yxSb1IcJs4rx1fA_yUMvKW_LyOaAVGadM6gELWpQ95rhlVw94Y2qnMY5uVAEFZsXRG6H9z8XT_boip_pFJfmfcZWAQ1IBu-uC-7dQ7OWL3fhzGc_xQFJc8mTlK7lFZTzGwXgQJoG_sXoEwIomj6n9u-rBt9dfcFC26lY3Q-sHwrytCofzuhFAwUuVkLoxXb-QvCxJs1wVHLJTKjxOIuvWFxN5p0tdWdI79hOTZ6oKJnLm67cJTzaHnOgIdLXUkTirfSV7s-IMtjCz2E9ZFsKJgSTsLOC5IohYeFcFPfGE4_C8Nm1rhs9DSrQIVT8p0YYuXCxtT7s89__PZoal880KPnNgEKmp1dBJ6JRXUrcI97gSahP_wPIEJ0PRQlsputAhH5C15O2gV25BGTYiuyQkl5QI43JBa3ogiuYmVbH3OLiIgNiPumnVG7MjXAA8xi1xv5pGD6Z4ZuPCYQbyJWLv0-olmu8EgMQO2XLzzQ7OKwTK6zzeL4Y4D-loIxiLLspD=w716-h484-no)

## Frames Traversing the Network
With a hub, outgoing frames PCA are relayed to all devices on the network included in the frame is the physical address of the sender and the target.
All devices will check the frame to see if the physical address matches their own.
If the target address matches, the frame is processed, otherwise it is discarded.

## Cyclic Redundancy Check (CRC)
CRC is used as way to verify the integrity of the data being sent in the Frame and ensure that it hasn’t been corrupted.
CRCs are a part of the Frame Check Sequences (FCS), all frames that are traversing over a network are in danger of being corrupted or damaged by interferences on a network.
FCS can use CRCs to validate the data that has been transmitted, CRCs work in a similar way to checksums; an algorithm generates a number or string of text from a piece of data, this algorithm can then be calculated in calculated again when the frame is received to confirm its integrity.

![Cyclic Redundancy Check](https://lh3.googleusercontent.com/UaSVzouzhqyIat8pqoGfH_3mHy1-MBV3Fu0Y6xzC1y4yM8yWMgD8FvFgd2952s3ce1D7nGN-jIEuKms1XjwCB8fVQJRLblrZ2V5vdamEFQzU_SRzS90_ObvigD3QpLlFlGJ0kOTMVyb8ZNMpgzdyF5IUKdqaScshibwT8B8Uu2sT_jNiMcS3HhKUq6M0KUZKim4Dk0vtcmASNzP7DtT4zau4X4tk1mZ9CvxTDqQ9x2qsiCFIoMQtlYsCkxNi_qWXQru0de1y4yeeVmK7obeDYm04kKCTJcznPRk3l0gdn9_xWx6FnrRH7Tkss42Vvit98cB_2kPCPY0G6a1DQaDyGcFEyggbw6K7foxdMNFerr5Rfh_YzYCTmjeAr6xmHClWt5f_U2KXgYaBLU2lrApBrGNU57Wm4_5I0bITzkA-dRCOx4bTG9d1kY5hKT6T8UL0ThMXW9YQL3LdwyDv5hAAOCXUhflEqxytwEM0fp6qOEp5xvZL_JdlNe2P8DjuICTLXBZ3RXCIIrqzUKLAAGHfgb_VaGyYy_GviC0534GQdAIdHTZS-QOy252Gpbn8PxSMDWLCxx6ADpldW7--g8_QtunlerwNV4ILXM9tqyXXPVVla5OKGBd-jLEg1Z3JFkK2gts7OegiM-I1uKKxGdR8A3mvgpZZfL0jxPz1azt6sPj1nBpjBvbfZPSFE_2hqjohLm0zL07OipEOpptUxZSyMdlou-kaAS2ERLkLmGBnfCpgGDvd=w1278-h411-no)

