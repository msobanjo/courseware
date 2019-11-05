# SQS Introduction

## Overview

Amazon Simple Queue Service (Amazon SQS) offers fast, reliable and scalable queues for storing messages. By using Amazon SQS, you can move data between distributed components of your applications that perform different tasks without losing messages or requiring each component to be always available.

## Coupling

If you have never come across the concept of Coupling before, you need to be fully aware of it before we move on.

```
We need a module here that describes coupling.
```

Simply put when we are creating a diverse system using a MicroServices Architecture, we aim for each of these services to be reliant on as small a number of other services as possible, this limits the impact to the overall system if a single service fails.

## Queues

A queue is a temporary repository for messages that are awaiting processing. The queue acts as a buffer between the service producing the data and the service consuming (or using) the data. This means the queue resolves issues that arise if the producer is producing work faster than the consumer can process it, or if the producer or consumer are only intermittently connected to the network. 

A single queue can be used simultaneously by many distributed services, with no need for those services to coordinate with each other to share the queue, hence we have achieved low coupling.

## Tasks

For this task we will be creating a simple SQS Queue, we will be pushing messages to the queue, reading them from the queue, and finally deleting messages from the queue.

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

We can give each Attribute a Name, a Type and a Value.  For this Task please create a numerical attribute with the name 'Price' and give it a value of 100.

Click the blue **Send Message** button, you will then see that the queue you have created on the dashboard will have 1 message available.

With the queue still highlighted, click the **Queue Actions** drop down menu, then click the **View/Delete Messages**.

Here we have a screen where we will be able to interact with the messages that are on the queue, click the blue **Start Polling for Messages** button.

The process should return the message that appears on your queue, however because SQS is a distributed managed service, one poll may not find all of your messages on the queue.

If you click the **message details** button you will be able to see the body of the message and the attributes that we have set for it.

You can delete your message by selecting the tick box on the left of the message.  Then by using the red **Delete x Message** button.
