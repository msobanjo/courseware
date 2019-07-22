# Overview
Key Pairs in EC2 can be used for securely connecting to EC2 instances in AWS.
Connections are usually over SSH which uses public and private keys.
This handout discusses how to manage these Key Pairs and how to locally store the private keys that are generated on your local system.

## Creating Key Pairs
### Basic Usage
The create-key-pair command can be used to create our key pair, the name of the Key Pair so that it can be easily referenced later on, such as when we want to add a key pair to an EC2 instance.
```bash
# aws ec2 create-key-pair --key-name [KEY_PAIR_NAME]
aws ec2 create-key-pair --key-name MyKeyPair
```
### The Private Key
Once a new Key Pair has been created, the AWS CLI will print out the private key, along with some other information about the Key Pair.
The private key is what we can use on the client side, to authenticate with an EC2 instance.

Here is an example which has been made much shorter:
```
{
    "KeyFingerprint": "7d:67:36:6e:0d:a7:ce:54:d1:41:20:ad:b7:c6:2d:27:e0:05:d8:e1",
    "KeyMaterial": "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAg3tSPNYVmrBVmbIY+/8lRVl/EvIprDpO/pHlODc846AOCZuUC0GXT5Ro95Nkr4zz7zMRrY\n22rHAmH3p6krizoM+fjRorLTSushQ2YQJJRq+O7RCNvtpyaDoRYWKRWqgGfgaZ+ZTXo=\n-----END RSA PRIVATE KEY-----",
    "KeyName": "MyKeyPair"
}
```

### Locally Storing the Private Key
It is important that we save the private key somewhere, because we will not be able to gain access to it again.
To do this we can add a query to our command which gets the KeyMaterial property when the key information is returned, we can then specify that we would like a text output and then redirect the output to a file for the key to be stored in.
```bash
# aws ec2 create-key-pair --key-name [KEY_PAIR_NAME] --query [QUERY] --output [OUTPUT_TYPE]
aws ec2 create-key-pair --key-name MyKeyPair --query ‘KeyMaterial’ --output text > ~/.ssh/MyKeyPair.pem
```

### Private Key Permissions
When storing a private key, it is important that only you as the owner are the one that is able to read it. Make sure you change the file permissions to allow this:
```bash
chmod 400 ~/.ssh/MyKeyPair.pem
```

