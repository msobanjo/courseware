# `localhost` and Ports

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [`localhost`](#localhost)
- [Ports](#ports)
- [Tasks](#tasks)
	- [See your local loopback mechanism information](#see-your-local-loopback-mechanism-information)
	- [See all the currently running ports](#see-all-the-currently-running-ports)
		- [macos, Linux, or Windows Subsystem for Linux](#macos-linux-or-windows-subsystem-for-linux)
		- [Windows](#windows)
	- [Navigate to a program running through a port on `localhost`](#navigate-to-a-program-running-through-a-port-on-localhost)

<!--TOC_END-->
## Overview
Let's say that we want to access network services that are running on a host device. 

To do this, we have to use the **local loopback mechanism**, a network interface which bypasses the networking hardware of that device entirely.

The cool thing about the local loopback mechanism is that it can run a service that's meant to be on a network - either the local network or the Internet - without having any networking hardware installed on the device at all.

There is a special category of IPv4 addresses reserved so that we can do this: `127.x.x.x`.

They can only be used by internal systems within a host device - in other words, when using these addresses, the host device acts as both the *source* of data and the *receiver* of data. 

## `localhost`
`localhost` is one of these **loopback address** - so any connection it tries to make bypasses its networking devices entirely, and *loops* the connection back to its own internal systems.

`localhost` is hosted at the loopback address `127.0.0.1` (or `::1` in IPv6).

So, when we use the `localhost`, what we're basically asking the device to do is to point any data it sends to *itself*.

As such, the `localhost` is a testing area. 

It looks and feel as though you're hosting something (like a service or a website) on the Internet properly - but all that's really happening is that your device is looping back to itself whenever it tries to connect to the thing you're testing.

This is great for when we're developing applications, because it allows us to test our services without ever exposing them to a) the rest of the network we're on, and b) the Internet.

## Ports
Ports allow us to speak to a specific *service* - a small, self-contained program, which can be used either on its own or in combination with other services.

We 'plug in' the service to the port we want it to use (though for larger programs, this is usually done automaticaly).

The `localhost`, as part of testing, makes exclusive use of these ports.

Because `localhost` uses TCP/IP, any port that it tries to speak to is a **TCP port**.

For instance, if we want run a program which can be hosted on the Internet directly from a computer, such as a Java application, we might find that this program is hosted here:
```text
localhost:8080
```

In this instance, the `:8080` refers to the specific **port** which a program is using to run.

Since the `localhost` is just a name for a specific IP address, our Java application really runs here:
```text
127.0.0.1:8080
```

If we were to host this application outside of our `localhost`, the IP address would change, but the port would remain the same:
```text
34.231.45.89:8080
```

## Tasks

### See your local loopback mechanism information
*This Task will only work when using macOS, Linux, or Windows Subsystem for Linux.*

Open a terminal and enter the following command:
```shell script
$ ifconfig lo
```

You should get an output similar to this:
```bash
nick@DESKTOP-JLGAKSF:/c/WINDOWS/system32$ ifconfig lo
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 1500
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0xfe<compat,link,site,host>
        loop  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

We can see that our `localhost` defaults to `127.0.0.1` or `::1`:
```text
inet 127.0.0.1
inet6 ::1
```

### See all the currently running ports

#### macos, Linux, or Windows Subsystem for Linux
Open a terminal and enter the following:
```text
ss -ar
```

This lists every available port on your system, and which service is using it.

#### Windows
In Windows, the command to do the above is this:
```text
netstat -ab
```

We can also check these ports by using the **Task Manager**.

Press `CTRL + Shift + ESC` to bring up the Task Manager, then navigate to the **Services** tab:

![Control Panel services](https://i.imgur.com/zckHOj1.png)

The `PID` is the current TCP port being used by a particular program.

### Navigate to a program running through a port on `localhost`
For this Task, we will attempt to read an e-book through port 9090 on `localhost`.

First, [download the calibre e-book reader for your system](https://calibre-ebook.com/download).

Open the file, follow the on-screen instructions, then open *calibre* once it has installed.

Once *calibre* is open, click the **Preferences** button (crossed tools) in the top-right:

![calibre preferences](https://i.imgur.com/0fMQdho.png)

Click the **sharing over the net** link, and you should see port settings:

![calibre sharing settings](https://i.imgur.com/Dw4F9w0.png)

Here, we're going to hook up our *calibre* installation to the Web, so that it can be accessed using our `localhost`:
1. Set the port to `9090`
2. Restart the server using the *Stop server* and *Start server* buttons
3. Click **Apply** and close the window

Now, open a browser window and navigate to the following:
```text
http://localhost:9090/
```

You should be greeted with the *calibre* welcome screen:
![calibre on localhost:9090](https://i.imgur.com/pqPQcUX.png)
