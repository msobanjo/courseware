# S3

## Overview

S3 is a Foundation Tool in the AWS Eco-System, it is a Highly Available Object Store that allows 'infinite' storage, you will never run out of space to store your files.

## Bucket Creation

in this module we will be looking at some of the more advanced choices we can make when we are setting up our buckets using the management console.

### Configure Options

In this section of the bucket creation wizard we can configure some high-level options about how our buckets work.

We can enable versioning, which is explained in more detail later, however it simply allows us to maintain multiple versions of one file.

Object Lock is an option we can select that requires versioning to be enabled, simply, it allows objects to be WORM-protected(Write-Once-Read-Many) or immutable, this means that the object cannot be overwritten or deleted. 

We can record requests for access to our bucket, these logs can then be stored in a different bucket so we can keep track of who, when and how a request for access has been made.

We can also allow Object-level logging, this will track access requests and API calls to Objects using CloudTrail, however there is an additional cost for this service.

Tags - We can add bespoke tags to our buckets in order to better keep track of which bucket corresponds to which project.  This is a simple solution that can make working with services in AWS in a complex system so much easier.

### Versioning

By default *versioning* is not enabled on S3 buckets and once you enable it, you cannot switch it off.

Versioning helps protect objects from accidental deletion, when an object is deleted, S3 inserts a *delete marker* instead of removing the object, you can then use this delete marker to restore the object as that particular version.

Versioning also helps to protect against over writing, if you try to overwrite an object, it results in a new object version in the bucket.  You can then decide to restore the object to this previous version.


### Set Permissions

Knowing who has permission to access the data in our buckets is of paramount concern.  There are 2 high-level ways in which we can control access to our buckets, we either use Access Control Lists (ACLs) or bucket policies.  We will be exploring what the means more in a later modules.

On this page we have the option to use checkboxes to modify public access, if we tick the main checkbox we will allow public access to our bucket.

### Review

The final section of the wizard allows us to review the previous selections that we have made and gives us the opportunity to return to those screens to edit any settings.

You should always ensure that you have setup your production-ready buckets correctly by using this review page.

# Tasks

In this task we will be setting up a bucket by using the full wizard.  We will then upload some files to make this bucket serve a static website.

Navigate to the S3 Management Console.

Click the blue **+ Create bucket** button.

Give the bucket a globally unique name, for example:

```
qa-bucket-creation-<unique string of numbers>
```

Set the region.

click the blue **next** button in the bottom right.

Add some tags to your project, for example;

project - website
department - qa

Untick the **Block *all* public access** checkbox.  Ensure that the 4 other checkboxes are also unticked.

Review the options you have selected on the final page of the wizard.

Click the blue **Create bucket** button.

Ensure you have the files found in the website folder of this repository stored locally.

Click the blue **Upload** Button, drag the files (3 files and 3 folders, 6 items in total) onto the indicated area.

Click the blue **Upload** button, you should now see the files being uploaded to your bucket.

Click the checkbox in the top left of the list of files, this will select all the files in the bucket.

Click hte **Actions** drop down menu.

Click the **Make public** option.

Click the **Make public** button.

Click the **Properties** tab across the top of this screen.

Select the Static website hosting box.

Click the first option to use this bucket for hosting a static website.

In the first box type **index.html**.

Make a note of the Endpoint URL deployed at the top of this box, it should look something like:

```
http://qa-bucket-creation-<unique string of numbers>.s3-website-eu-west-1.amazonaws.com
```

Click **Save**

Navigate to the endpoint from a previous step, you should see that you have successfully deployed a static website.
