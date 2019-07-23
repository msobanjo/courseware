# VPC Introduction
## Overview
Amazon Virtual Private Cloud (Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.
You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.
You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications.

You can easily customize the network configuration for your Amazon VPC.
For example, you can create a public-facing subnet for your web servers that has access to the Internet, and place your backend systems such as databases or application servers in a private-facing subnet with no Internet access.
You can leverage multiple layers of security, including security groups and network access control lists, to help control access to Amazon EC2 instances in each subnet.

## Use Cases
### Host a Simple, Public-Facing Website
You can host a basic web application, such as a blog or simple website in a VPC, and gain the additional layers of privacy and security afforded by Amazon VPC.
You can help secure the website by creating security group rules which allow the webserver to respond to inbound HTTP and SSL requests from the Internet while simultaneously prohibiting the webserver from initiating outbound connections to the Internet.
You can create a VPC that supports this use case by selecting "VPC with a Single Public Subnet Only" from the Amazon VPC console wizard.

### Host Multi-Tier Web Applications
You can use Amazon VPC to host multi-tier web applications and strictly enforce access and security restrictions between your webservers, application servers, and databases.
You can launch webservers in a publicly accessible subnet and application servers and databases in non-publically accessible subnets.
The application servers and databases can’t be directly accessed from the Internet, but they can still access the Internet via a NAT gateway to download patches, for example.
You can control access between the servers and subnets using inbound and outbound packet filtering provided by network access control lists and security groups.
To create a VPC that supports this use case, you can select "VPC with Public and Private Subnets" in the Amazon VPC console wizard.

## Creating a VPC
### Basic Usage
VPCs can be create very easily, you only should have to provide the CIDR block which defines the address range for you subnet.
```bash
# aws ec2 create-vpc --cidr-block [CIDR_DEFINITION]
aws ec2 create-vpc --cidr-block 10.0.0.0/16
```

### Create a Default VPC
If you created your AWS account after 2013-12-04, it supports only EC2-VPC. In this case, you have a default VPC in each AWS Region. A default VPC is ready for you to use so that you don't have to create and configure your own VPC. You can immediately start launching Amazon EC2 instances into your default VPC. You can also use services such as Elastic Load Balancing, Amazon RDS, and Amazon EMR in your default VPC.

A default VPC is suitable for getting started quickly, and for launching public instances such as a blog or simple website. You can modify the components of your default VPC as needed. 

If for whatever reason you have deleted your default VPC, its easy to create another one:
```bash
aws ec2 create-default-vpc
```

### CIDR Blocks & Limitations
The CIDR block is what defines how large or small your subnet is.
The smallest CIDR block you can have is /28, with 16 hosts or /16, which can have up to 65,536 hosts.

## View Existing VPCs
### Basic Usage
You may want to view the existing VPCs to view the properties of them:
```bash
aws ec2 describe-vpcs
```
### Getting the ID Property Using Queries
To manage a VPC, such as when you want to delete it, then you will need to be able to reference that VPC by its ID.
If you have several VPCs then the output can be a little overwhelming, considering that you just want to see the IDs.
We can use a query like belown and change the output to just be text to make a list of VPC IDs.
```bash
aws ec2 describe-vpcs --output text --query "Vpcs[].VpcId"
```

## Delete VPCs
### Basic Usage
The VPC ID must be provided when deleting a VPC:
```bash
# aws ec2 delete-vpc --vpc-id [VPC_ID]
aws ec2 deletecreate-vpc --vpc-id vpc-061635ad5414cf433
```

## Tasks
Try to complete the following tasks using the commands you learned above:
- Create a new VPC with a CIDR block of 10.0.0.0/16
- List the VPCs you have, showing only the IDs of them
- Delete the VPC that you created by it's ID
- Learn about [Internet Gateways](./internet-gateways)

