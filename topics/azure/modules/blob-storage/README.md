# Blob Storage

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Unstructured Data](#unstructured-data)
- [Blob storage design](#blob-storage-design)
- [Blob Storage Access](#blob-storage-access)
- [Task](#task)

<!--TOC_END-->
## Overview

Blob storage is Microsoft's **object storage** solution for the cloud.

It is optimised for storing **massive** amounts of **unstructured** data.

## Unstructured Data

Unstructured data is data that doesn't conform to a particular data model or definition.

Examples of this are text data and binary data.

## Blob storage design

Blob storage is designed for:

* **Serving images** or documents directly to the browser
* Storing **large files**
* Streaming **video** and **audio**
* Writing to **log files**
* Storing data for **backup**, **disaster recovery** and **archiving**
* Storing data for **analysis** by another service (either on-premises or Azure-hosted)

## Blob Storage Access

Access to objects in blob storage can be achieved using **HTTP/HTTPS** from anywhere in the world.

You can give customers/client applications access to the objects for a specified length of time, via a _Shared-Access Signature_ (effectively a URI with a specified time limit for access).

As well as this, with the right permissions, objects can be accessed using the Azure Portal, Azure Powershell or Azure CLI.

## Task

To learn more about Azure Blob Storage, take some time to watch this [video from Microsoft Azure](https://www.youtube.com/watch?v=UJG6viKU_A8).
