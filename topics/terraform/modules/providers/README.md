# Providers

<!--TOC_START-->
## Contents
- [Overview](#overview)

<!--TOC_END-->
# Overview

Providers must be configured to manage any infrastructure in Terraform, this module will cover them and how to set it up.

### Provider

The provider wraps the create, read, update and delete API calls needed to manage resources. 

It’s easy to tell what provider a resource uses because the type of a resource always begins with the name of its provider. 

For example, aws_instance uses the AWS as the provider provider.

Here's an example of a provider:

<details>

<summary>AWS provider example</summary>

```hcl
provider "aws" {
  region = "eu-west-2"
}
```

</details>

### Provider plugin architecture

