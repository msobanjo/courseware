# SQS Introduction

## Overview

Amazon Simple Queue Service (Amazon SQS) offers fast, reliable and scalable queues for storing messages. By using Amazon SQS, you can move data between distributed components of your applications that perform different tasks without losing messages or requiring each component to be always available.

## Coupling

If you have never come across the concept of Coupling before, you need to be fully aware of it before we move on.

```
We need a module here that describes coupling.
```

Simply 

## Queues

A queue is a temporary repository for messages that are awaiting processing. The queue acts as a buffer between the component producing and saving data, and the component receiving the data for processing. This means the queue resolves issues that arise if the producer is producing work faster than the consumer can process it, or if the producer or consumer are only intermittently connected to the network. SQS ensures delivery of each message at least once, and supports multiple readers and writers interacting with the same queue. A single queue can be used simultaneously by many distributed application components, with no need for those components to coordinate with each other to share the queue.

## Tasks

Navigate to the **SQS Dashboard** to the using the Service drop down menu.

If this is your first time here you will see a splash screen with a blue **Get Started Now** button, click this button.

Enter a name for your queue, for example;

```
example-queue
```

We will be using a Standard Queue for this Task.

Click the blue **Quick-Create Queue** button at the bottom right of the page.

You will be returned to the SQS Dashboard.

When the Queue is highlighted we can select some Queue Actions, toggle this dropdown menu and we select **Send a Message**.

Here we can add some text to the message that we need to send, add some sample text here.

If you click the **Message Attributes** tab at the top of the screen you will see that you can add some attributes to the message.

We can give each Attribute a Name, a Type and a Value.  For this Task please create a numerical attribute with the name 'Price'.









