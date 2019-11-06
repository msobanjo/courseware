# S3 File Upload

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [File Upload](#file-upload)
	- [Moving Data](#moving-data)
	- [Multipart Upload](#multipart-upload)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview



## Moving Data
Although S3 allows you to store as much data as you want, individual objects cannot be larger than 5 TB.
However there are restrictions in place when you are uploading files using the GUI, if you upload a file using the Amazon S3 console then the maximum file size is 160 GB.
You need to use the AWS CLI or API directly to upload larger files.

## Multipart Upload
Multipart Uploads are the concept that enables us to upload files of up to 5 TB, Multipart Uploads also have other benefits:

- Parallel uploads to improve throughput.
- Minimising the impact of restarting a download due to a network failure.
- Pausing and restarting object uploads - you have more flexibility over how an upload ends.
- An upload can start before the object has been completely created.

## Tasks

For this task we will be using the AWS CLI to upload a file to a bucket you have created.

The first step is to list the buckets that we have on our account, to do this with the CLI you need to run the command below.

```bash
aws s3 ls
```

You should see that some information about the buckets in your account is displayed.

At this point it might be useful to list the objects in the bucket to ensure that we are using the correct bucket, to do this run the following command.

```bash
aws s3 ls s3://<name-of-bucket>
```

This will show information about the objects in the bucket, including when it was created, its size in bytes and the name of the object.

Our final step is to upload a file via the CLI, ensure you have a  suitable file to upload and then run the command below.

```bash
aws s3 cp <path to file> s3://<name-of-bucket>
```

You should see a single line returned stating that the file has been uploaded, use one of the commands you have learnt above to ensure that the object does indeed now exist in your bucket.
