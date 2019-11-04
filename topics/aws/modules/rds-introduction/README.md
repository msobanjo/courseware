# Relational Database Service (RDS)

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [SQL vs NoSQL](#sql-vs-nosql)
- [Managed vs Unmanaged](#managed-vs-unmanaged)
- [RDS Use Cases](#rds-use-cases)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
Amazon Relational Database Service (Amazon RDS) is a fully managed relational database service, it can be used to provision new database instances in a matter of minutes that can easily be vertically scaled.

## SQL vs NoSQL
We should be comfortable with the differences between these 2 kinds of databases, the 2 options are available in AWS for your architecture.

RDS is focused around the SQL or relational Databases, where the data within them has some sort of structure or schema that must be adhered to.

Comparatively you might decide to use a NoSQL option when you need have data that is relatively unstructured or does not conform to traditional schemas.  You may also require a solution that can be horizontally scaled as opposed to just vertically scaled.

Comparison of different solutions

| Attribute        | SQL           | NoSQL  |
| -------------:|:-------------:|:-----:|
| Data Storage      | Rows and Columns | Key-Value stores and documents |
| Schema      | Fixed      |   Dynamic |
| Querying | SQL based querying      |    Collections of Documents |
| Scalability | Vertical      |    Horizontal |

## Managed vs Unmanaged

When we discuss this argument it is worth remembering the 'aaS' concept, we can give up flexibility of a service in exchange for less responsibility.

With an unmanaged database hosted on-prem, we are responsible for maintaining all aspects of the database, from its power and cooling requirements through to managing concepts such as how it scales, and everything in between.

With an unmanaged database in the cloud we are not responsible for maintaining the hardware that the database uses, however we are still responsible for installing, patching and backing up the database.

With a fully managed database we are responsible only responsible for optimising the app that uses our database, that is ensuring that the database works as well as possible for our application.  We do not need to deal with any of the hardware issues, maintaining the software that the database uses, scaling the database or ensuring high availability.

So as previously stated, with a managed system we give up our ability to change the system in exchange for less responsibility.

## RDS Use Cases

A Relational database solution such as RDS works well for applications that have complex, structured data that conforms to a particular schema.  It is also a great solution for when you need to perform complex joins and queries on this data.

RDS as a managed solution works well as a solution when you do not want to handle the tasks of provisioning and maintaining the database that your application requires.

## Tasks
<<<<<<< HEAD

For this task we will be creating a simple managed database using the management console.

Using the Services drop-down from the top of the Management Console navigate to RDS.

A small window at the top of the screen will state some information about a service called Amazon Aurora, we will be exploring that in more detail in a later module, however for now we should click the orange **Create database** button.

The first option we get is to choose a database creation method, as this is an introductory module to RDS we will be using the **Easy Create** option, select this now.

For the Engine Type we will be using **MySQL**.

For the DB instance size please select the **Free tier** option.

Create a suitable identifier for your DB instance, it needs to conform to some rules set out below the input field as well as being unique to your account.

Set a master username for your Database, do not use 'admin', for the purpose of this Task I will be using:

```
QARDSIntroUser
```

Set a Password for your DB instance, for the purpose of this task I will be using:

```
TheSkillsToSucceed
```

Click the orange **Create database** at the bottom right.

After a few moments you database will be ready to use!

To access your navigate, ensure you are using the RDS console and click the Databases link in the left pane.

=======
>>>>>>> ea4a5acc7464527c2675527869698db358e43836
