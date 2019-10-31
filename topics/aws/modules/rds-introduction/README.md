# Relational Database Service (RDS)


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