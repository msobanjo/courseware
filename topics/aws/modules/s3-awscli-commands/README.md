# S3

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [AWSCLI commands with S3](#awscli-commands-with-s3)
	- [Help](#help)
	- [Listing your buckets](#listing-your-buckets)
	- [Creating a bucket](#creating-a-bucket)
	- [Deleting a bucket](#deleting-a-bucket)
	- [Working with Objects](#working-with-objects)
- [Tasks](#tasks)

<!--TOC_END-->


## Overview

We have mainly been looking at working with S3 using the Management Console, however, we can also use the AWS CLI to complete the same tasks, as well as others, in a more programmatic way.
Using the CLI allows us to script and automate what you would normally have to do manually in the management console.

This module will take you through some of the basic commands when working with S3 using the AWS CLI.

### Help
The first command you should always be familiar with is the `help` command and how to access it:


```bash
aws s3 help
```
This will provide you with a list of the commands that you can perform with the CLI.  To get more information about these commands you can call the help command on that particular command as below:
```bash
aws s3 cp help
```
The example above will show more information about the aws `cp` command.

### Listing your buckets
We may need to look at a list of the buckets that we have in a particular account.
To do this we can make use of the `ls` command:

```bash
aws s3 ls
```
This will show a list of all the s3 buckets that you have within your account.

If you read the help for the `ls` command you will see that there are many options that you can pass to the command to get more or different information.

We will likely also want to get some information about the objects within our buckets.
We can use the command below to list the objects that exist within a particular bucket:
```bash
# aws s3 ls s3://<bucket-name>
aws s3 ls s3://my-bucket
```
Technically we do not need to use the `s3://[URI]` schema, as AWS S3 `ls` does not interact with our local file system.  However it is good to help avoid ambiguity with what a command is doing.

If we had a bucket with a large number of objects within it, we may want to list the contents of the bucket, along with a summary of the bucket (number of objects and size) in an easy to read way.

```bash
aws s3 ls s3://<bucket-name> --summarize --human-readable
```

### Creating a bucket

To create an S3 bucket with the CLI is quite straightforward; we use the `mb` (make bucket) command.
We still need to ensure that we are using a globally unique name for our bucket that meets all the required rules.

```bash
# aws s3 mb s3://<bucket-name>
aws s3 mb s3://my-bucket
```

### Deleting a bucket

To delete a bucket using the CLI we should first ensure that the bucket is empty, you could do this using the list command discussed above.

You can then use the `rb` (remove bucket) command:

```bash
# aws s3 rb s3://<bucket-name>
 aws s3 rb s3://my-bucket
```
If however you have a need to, you can delete a bucket without first emptying it by supplying the `--force` option:

```bash
# aws s3 rb s3://<bucket-name> --force
aws s3 rb s3://my-bucket --force
```

### Working with Objects

There are a number of commands that can be used to interact with objects stored in your buckets.
These commands fall in line with some commands you may be familiar with from working with Unix based systems, `cp`, `mv` and `rm` in particular.

```bash
# aws s3 cp <filepath> s3://<bucket-name> --storage-class STANDARD_IA
aws s3 cp ./my-file.txt s3://my-bucket --storage-class STANDARD_IA
```

The above command for example would copy a file from a location on the local machine into the named bucket using the Standard-IA Storage class.

We could use the `mv` command in a similar way, however remember that the Unix `mv` command will delete the file from the first location and place it at the second.

```bash
# aws s3 mv s3://<bucket-name>/<object-key> <local-file-path>
aws s3 mv s3://my-bucket/test.txt test.txt
```
We can also use the `cp` and `mv` commands to transfer a file from S3 into our local file system.

```bash
# aws s3 rm s3://<bucket-name>/<path>/<subdirectory>/<file-to-delete>
aws s3 rm s3://my-bucket/static/images/mini-dachshund.png
```

The command above will delete a specific file from a bucket, you can add the `--recursive` option and specify a folder within an S3 bucket to delete a particular folder and all of its contents.

## Tasks

First we will create a new bucket for the purposes of this task.  
Also for this task create 2 simple text files that will be uploaded to the bucket.

```bash
aws s3 mb s3://<bucket-name>
```
We now want to upload our 2 sample files to the bucket.  Ensure that we use the Standard Storage Class.

```bash
aws s3 cp <filepath> s3://<bucket-name> --storage-class STANDARD
```
Our next task is to delete the files from our local machine, in a future step we want to download the files from the bucket.

We now need to move one of the files from our bucket back into our local file system, to do this we will make use of the 'mv' command.

```bash
aws s3 mv s3://<bucket-name>/<file-to-copy> test.txt
```
The next step will be to remove the the other file from the bucket, to do this we will make use of the 'rm' command.

```bash
aws s3 rm s3://<bucket-name>/<path>/<subdirectory>/<file-to-delete>
```

Our final step now is to completely remove the bucket the our account, to do this will be making use of the 'rb' command.

```bash
aws s3 rb s3://<bucket-name>
```
