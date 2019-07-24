# AWS EC2 Instances
## Overview


## Running an Instance
### Viewing Available AMIs
We need to provide an AMI when running an instance, Amazon has a page with commands for finding the latest image for popular operating systems: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html please note that you will need `jq` installed to run the commands provided.
Here is an example that gets the latest `ubuntu 18.04` image id (AMI):
```bash
aws ec2 describe-images --owners 099720109477 --filters 'Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-????????' 'Name=state,Values=available' --output json | jq -r '.Images | sort_by(.CreationDate) | last(.[]).ImageId'
```

### Running an Instance
Running an instance requires quite a few options:
- Image ID
    This is the base image that the machine will use, Ubuntu is an example.
- Count
    The amount of instances to run from this command
- Instance Type
    The size of the machine, how many CPUs and how much RAM
- Key Name
    The Key Pair to install onto the machine, we need this to be able to securely connect to the instance with SSH.
- Subnet ID
    Which subnet to run the instance in. The instance will be given a private IP address from the subnet that you put it in and and security group rules from the VPC will be applied to the instance.
```bash
# aws ec2 run-instances --image-id [IMAGE_ID] --count [AMOUNT_OF_INSTANCES] --instance-type [MACHINE_SIZE] --key-name [KEY_PAIR_NAME] --subnet-id [SUBNET_ID]
aws ec2 run-instances --image-id ami-0ee246e709782b1be --count 1 --instance-type t2.micro --key-name MyKeyPair --subnet-id subnet-0b601356c0674d00d
```

## View Running Instances
### Basic Usage
To check what existing instances there are, we can use the `describe-instances` command:
```bash
aws ec2 describe-instances
```

## Terminate a Running Instance
### Basic Usage
We can terminate instances by providing their IDs to the `terminate-instances` command.
```bash
# aws ec2 terminate-instances --instance-ids [INSTANCE_IDS]
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

