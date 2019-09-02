<!--PROPS
{
    "estTime": 5,
    "questions": [
        {
            "value": "What is the Netstat command used for?",
            "answer": "Displaying network connections for Transmission Control Protocol, routing tables, and a number of network interface and network protocol statistics",
            "choices": [
                "Provide information about the currently running processes, including their process identification numbers (PIDs)",
                "Allowing you to run programs with the security privileges of another user"
            ]
        }
    ]
}
-->
# Netstat Introduction
<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Use Cases](#use-cases)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
In computing, netstat is a command-line network utility that displays network connections for Transmission Control Protocol, routing tables, and a number of network interface and network protocol statistics.

Netstat is usually installed on most operating systems including Windows, Mac and many popular Linux distributions.
One thing to take into consideration when using netstat is that the options are different depending on which operating system you are using.

## Use Cases
The netstat tool can be used for the following:
- Finding issues in a network
- Find what application is using a certain port
- Measure network performance
- Show current connections to the machine

## Tasks
Check that netstat is working correctly by opening a command prompt on Windows or a terminal on Linux and run the following command:
```bash
netstat --version
```
