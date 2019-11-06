# Providers

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Provider](#provider)
	- [Provider plugin architecture](#provider-plugin-architecture)
	- [Custom Providers](#custom-providers)

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

Your configurations can use as many providers as you need. 

Terraform doesn’t ship with any built-in providers. 

Instead it uses a plugin architecture to download the provider plugins required by your configuration.

Each required plugin corresponds to a provider block in your configuration. 

If you try to run plan or apply without having Terraform download the plugins you will get a nasty error message telling you to initialize the plugins.

You initialize Terraform by running the `terraform init` command. 

Terraform will parse your configuration and download the providers specified. 

The plugins are downloaded to a plugins directory inside of the hidden .terraform directory by default. 

As an aside, the init command follows the same process for any modules your configuration specifies as well.

### Custom Providers

Although there are over one hundred public Terraform providers available, if there isn’t a plugin available for what you need, perhaps for an internal private cloud implementation or internal tool you want to integrate, you are able to write your own provider plugins.

Custom providers are written in *Golang*.

HasiCorp provides guides on writing custom providers but this is not a part of this module.
