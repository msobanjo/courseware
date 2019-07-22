# EC2 VPC Subnets
A VPC spans all the Availability Zones in the region.
After creating a VPC, you can add one or more subnets in each Availability Zone.
When you create a subnet, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block.
Each subnet must reside entirely within one Availability Zone and cannot span zones.
Availability Zones are distinct locations that are engineered to be isolated from failures in other Availability Zones.
By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location.
We assign a unique ID to each subnet.

## Creating Subnets
## Basic Usage
After you create a subnet, you can't change its CIDR block.
The size of the subnet's IPv4 CIDR block can be the same as a VPC's IPv4 CIDR block, or a subset of a VPC's IPv4 CIDR block.
If you create more than one subnet in a VPC, the subnets' CIDR blocks must not overlap.
The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses).

When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the subnet.
```bash
# aws ec2 create-subnet --vpc-id [VPC_ID] --cidr-block [CIDR_BLOCK]
aws ec2 create-subnet --vpc-id vpc-081ec835f3EXAMPLE --cidr-block 10.0.1.0/24
```


