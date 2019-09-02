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
netstat
```
You should then see an output of the connections to your machine similar to below:
```text
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 work-laptop:46098       ec2-3-9-202-151.e:https ESTABLISHED
tcp        0      0 work-laptop:41682       wl-in-f188.1e100.n:5228 ESTABLISHED
tcp        0      0 work-laptop:49608       server-143-204-18:https ESTABLISHED
tcp        0      0 work-laptop:46246       lb-192-30-253-124:https ESTABLISHED
tcp        0      0 work-laptop:55948       17.47.211.130.bc.:https ESTABLISHED
tcp        0      0 work-laptop:48226       bam-8.nr-data.net:https ESTABLISHED
tcp        0      0 work-laptop:44982       server-143-204-22:https ESTABLISHED
tcp        0      0 work-laptop:46106       ec2-3-9-202-151.e:https ESTABLISHED
tcp        0      0 work-laptop:36322       104.16.70.125:https     ESTABLISHED
tcp        0      0 work-laptop:42932       do-17.lastpass.co:https ESTABLISHED
tcp        0      0 work-laptop:33642       185.199.109.154:https   ESTABLISHED
tcp        0      0 work-laptop:36784       8.255.186.35.bc.g:https ESTABLISHED
tcp        0      0 work-laptop:56196       a2-18-162-235.dep:https ESTABLISHED
tcp        0      0 work-laptop:38962       ec2-3-209-208-129:https ESTABLISHED
tcp        0      0 work-laptop:50210       ec2-54-145-70-92.:https ESTABLISHED
tcp        0      0 work-laptop:37266       47.67.201.35.bc.g:https ESTABLISHED
tcp        0      0 work-laptop:40866       151.101.192.176:https   ESTABLISHED
tcp        0      0 work-laptop:56710       101.59.190.35.bc.:https ESTABLISHED
tcp        0      0 work-laptop:46112       ec2-3-9-202-151.e:https ESTABLISHED
tcp        0      0 work-laptop:44858       ec2-52-215-192-13:https ESTABLISHED
```
