# S3

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [S3](#s3)
	- [What is it?](#what-is-it)
	- [Comparison of Block and Object Storage](#comparison-of-block-and-object-storage)
	- [Buckets](#buckets)
	- [Redundancy](#redundancy)
	- [Events](#events)
	- [S3 Use Cases 1](#s3-use-cases-1)
	- [S3 Use Cases 2](#s3-use-cases-2)
	- [S3 Use Cases 3](#s3-use-cases-3)
	- [Good uses cases](#good-uses-cases)
	- [Bad use cases](#bad-use-cases)
	- [S3 Costing](#s3-costing)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview

S3 is a Foundation Tool in the AWS Eco-System, it is a Highly Available Object Store that allows 'infinite' storage, you will never run out of space to store your files.

## S3

### What is it?

Amazon S3 is storage for the internet, it is designed to be used as a means to store and retrieve any amount of data, at any time, from anywhere on the web

It is a highly scalable, reliable, secure, fast and inexpensive infrastructure that is used by Amazon itself.

### Comparison of Block and Object Storage

S3 is an Object-Level Store, this means that the files we upload to S3 are stored as Objects.  If we want to update the contents of one of these files we cannot do so in situ, we need to download the file, make the change, and then re upload the file.

The file has been wrapped in meta-data, data that S3 uses to provide information about the object.  This object is then stored in an S3 'Bucket'. 

Block storage is older, in block storage data is stored in equal sized 'blocks' the data is not stored with any associated metadata.

An application will make SCSI calls to find the address for the data it needs in these blocks, because of this block storage leads to faster performance when the application and the storage is close.

This is why we use Block Storage as boot devices for our EC2 instances (EBS), S3 is an Object store, and cannot be used as a boot device.

### Buckets
When we work with S3, the first thing we need to do is create a bucket.  These buckets are where the files that we upload to S3 reside as objects.  Each S3 bucket must have a **globally** unique name that adheres to certain rules.

### Redundancy
By default, data in S3 is stored redundantly across multiple facilities and multiple devices in each facility, this is a Managed service meaning that AWS handles this entirely for the user.  When using S3 to store files, you will lose approximately 1 file from every 10 million files you store every 10,000 years or so.  This equates to 99.999999999% reliability (11 9's).

### Events
S3 includes event notifications that allow you to set up automatic notifications when certain events occur, such as an object being uploaded to or deleted from a specific bucket. Those notifications can be sent to you, or they can be used to trigger other processes, such as AWS Lambda scripts.

### S3 Use Cases 1
A popular use of S3 is to store and distribute static web content or media. These files can then be delivered directly from Amazon S3.

This works because each S3 bucket has a globally unique name, each object can therefore be associated with a unique HTTP URL. S3 can also be used as an origin for a content delivery network (such as Amazon CloudFront). Amazon S3 works well for fast-growing websites that require strong elasticity. This might include workloads with large amounts of user generated content, such as video or photo sharing.

```
https://aws-intro-bucket.s3-eu-west-1.amazonaws.com/001.mp3
```

### S3 Use Cases 2
A popular use of S3 is to host **entire** static websites. The files that you upload to the Bucket will include the html, css and js files you need to serve static web content, as well as any images or videos you may need for your site.  These files can then be delivered directly from Amazon S3.

### S3 Use Cases 3
Due to its high durability and scalability, S3 is a great tool for making backups and archiving.  You will learn more about a flavour of S3 called Glacier, which is designed to store rarely accessed files for long periods of time.

### Good uses cases
- WORM - Write Once, Read Many
- Spiked Data Access
- Large number of users and diverse amounts of content
- Rapidly growing data sets.

### Bad use cases
- S3 cannot be used for Block Storage, you cannot reformat the drive.
- The data you need to store changes often.

### S3 Costing
- Pay for the amount of Storage you use, rounded up to the nearest GB.
- Transfer of data out of the bucket into other regions or the Internet
- HTTP Requests on your data.

# Tasks

We will be creating our first bucket and uploading a simple file too it, please ensure you have a simple .txt file to upload to this bucket.

Log into your S3 Console and click the Services tab at the top of the screen.

Navigate too, or search for, S3.  Open the S3 management console.

Click the blue 	**+ Create Bucket** button.

Enter a globally unique name for your bucket, ensuring that you abide by the validation rules, for example; 

```
qa-my-first-bucket-<unique string of numbers>
```

Select a Region for your bucket, for now we should aim to set all our services in the same region so they are easier to track.

Press the **Create** button at the bottom left of this screen.

You should see that a new bucket has been created on the dashboard, select this bucket.

Click the blue **Upload** button in the top left of the screen.

Click the blue **Add files** button and navigate to your .txt file.

At this point you could have also dragged the file as indicated and dropped it onto the console.

Click the blue **Upload** button at the bottom left of this screen.

You should see that your bucket now contains the file that you uploaded.  Select it now.

Scroll to the bottom the the files details and you should see an Object URL, click the link.

We have tried to navigate directly to the file to download it via the internet, however you will find that you do not have the right permissions to access this file.  In later steps we will be looking at how we can control access to the Objects stored in our buckets.
