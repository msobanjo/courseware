# S3

## Overview

S3 is a Foundation Tool in the AWS Eco-System, it is a Highly Available Object Store that allows 'infinite' storage, you will never run out of space to store your files.

## Storage Options

### Storage Options
When you store Data in S3 you need to decide which storage class you will be using to store the data, the main driver behind the decision is how often you will need to access the data.  The list below represents some of the most commonly used storage options, we will be analysing these in turn.

- S3 Standard
- Intelligent-Tiering
- S3 Standard IA
- S3 One Zone IA
- Glacier

### Standard
Used when data will be often accessed - uses cross region replication for redundancy.  As you would expect this is the default storage class for when an object is first uploaded to S3.

### IA - Infrequently Accessed

Standard IA is used when you will not be accessing the data as often, it is cheaper to store data, however more expensive to access.
- Lower cost per GB stored
- High cost per HTTP Request made to the data.
- 30-day minimum storage.

### IA - One Zone
Cheaper than IA - however data is stored in a single Availability Zone, not to be used for critical application data.  One Zone IA is cheaper, but less reliable.

### Intelligent Tiering

Optimises storage costs by moving an object between 2 different storage classes automatically based upon the access patterns on that data.

Intelligent Tiering is ideal when you have data you need to store but you don't know what the access patterns for the data may be, for example with a new application or website when you are not yet sure how popular the data will be.

## Tasks



Click the blue **Upload** button.

Select a suitable file.

Click the blue **next** button.

Here we can set the permissions for our object as we are uploading it, if your bucket does not allow public access then we will not be able to manage public permissions.

Click the blue **next** button.

Here we can set some properties for our object, the first options you will notice are the Storage Classes available for object, notice some of the different restrictions that are placed on the different storage options.

If you scroll to the bottom of the screen you will see you have the option to change the metadata of the object as you are uploading it, as well as adding Tag to the object to make it easier to track.

Click the blue **next** button.

On this final screen we have the option to review the settings that we have applied to this/these files before we upload them to the bucket.
