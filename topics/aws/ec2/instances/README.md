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
```bash
aws ec2 run-instances --image-id ami-1a2b3c4d --count 1 --instance-type c3.large --key-name MyKeyPair --security-groups MySecurityGroup
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

