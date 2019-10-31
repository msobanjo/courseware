# S3

## Overview

S3 is a Foundation Tool in the AWS Eco-System, it is a Highly Available Object Store that allows 'infinite' storage, you will never run out of space to store your files.

## Lifecycle Policies

S3 can be automated to move your objects based upon their age, this is different from Intelligent Tiering as you would use this with data where you can better plan in advance the access pattern to your data.

For instance you may want to keep sales data from the last quarter in Standard Access as it is going to be most relevant in sales estimates.  However when you move into the next quarter you may want to move this data into a longer term storage solution as the data becomes less relevant.

This reduces your overall cost, because you are paying less for data as it becomes less important with time.  You can set these rules to apply to a bucket ot the individual objects in the bucket.

## Tasks

For this task we will be modifying the lifecycle policies on an existing bucket.

Using the Management Console select an existing bucket or create a new one.  

Click the **Management** tab across the top.

Click the **Lifecycle** button at the top.

You will see that there is no lifecycle rule applied to this bucket.  To create one you need to click the **+ Add lifecycle rule** in the top left.

Create a name for your rule, for example:

```
qa-s3-bucket-lifecycle-rule
```

At this point you can limit the Lifecycle to specific objects using tags.  This is important because we decide the storage class for objects per object at the object level, not at a bucket level.  Therefore we will likely want to setup transitioning from one storage class to another at an object level as well.

The next screen asks whether you want to set the lifecycle rules for just the current version of your files or for any previous versions as well.  This is only relevant if you have enabled versioning in your bucket.

We will be setting lifecycle rules for just the current version of our files, so select this checkbox.

Some text will appear, click the blue **+ Add transition** label.

This is where we can select the Transitioning rules that apply, for instance we can declare that an object should be moved into Standard-IA storage 90 days after it has been created.

A use case for this could be the static image resources used on a blog, the blog posts from 90 days ago are likely to be less popular and receive less hits.  Therefore the images attributed to these posts could be moved into Standard IA to decrease the overall cost of storing the image.

Click the blue **Next** button.

On the next screen we can decide if the objects should be deleted instead of moving into archival storage, in certain cases you may not need to retain the data at all, therefore deleting the object is perfectly plausible.  However if you need to retain the data, for instance Financial records for Audit purposes then ensure that you move these files into Archival Storage.

Click the blue **Next** button.

The final screen allows you to review the rule you are creating and make any edits to it, if you are happy with the rule use the blue **Save** button to save the rule.
