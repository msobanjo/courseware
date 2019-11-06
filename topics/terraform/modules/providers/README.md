# Providers

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Provider](#provider)
	- [Provider plugin architecture](#provider-plugin-architecture)
	- [Custom Providers](#custom-providers)
	- [Provider versioning](#provider-versioning)
	- [Provider aliases](#provider-aliases)

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

HashiCorp provides guides on writing custom providers but this is not a part of this module.

### Provider versioning

Providers are released on their own schedule and have their own versions separate from Terraform.

Within a provider block, you can omit a version and have the latest version downloaded automatically. 

Here is an example of omitting provider plugin version:

<details>
<summary>AWS example</summary>

```hcl
provider "aws" {
  region = "eu-west-2"
}
``` 

</details>

However, this can become problematic. For example, if the same configuration is applied on separate machines before and after a new provider version is released, potentially resulting in different behaviors. 

To avoid these issues, it is a best practice to constrain the provider version in your configurations. 

The string you assign to the **version** key constrains the version of the provider Terraform will use. 
You can either specify a specific version or a range. 

When you specify a range, you can use the less than, less than or equal to, greater than, or greater than or equal to operators. 
If you specify a lower and an upper bound, you separate the constraints using a comma.

You also use the tilde arrow or pessimistic operator as a short hand for certain ranges. The version number you specify acts as a lower bound of the version and the upper bound is set as the second last version digit specified.

If you have previously downloaded provider plugins satisfying the version constraints, running the init command again won’t result in newer versions being downloaded, even if there are newer versions satisfying the constraints. 
To upgrade to the latest provider plugin versions that satisfy your version constraints, you use the **init -upgrade** option of the init command.

You can check the current provider versions by executing the following command:

`terraform providers`

Here's an example of specifying a specific version for the provider plugin:

<details>
<summary>AWS example</summary>

```hcl
provider "aws" {
  region  = "eu-west-2"
  version = 2.8
}
```

If your current version of the *aws* plugin is lesser than 2.8 then run the following command to download the plugin version 2.8:
`terraform init -upgrade`

</details>

Here's an example of specifying the version by using the greater than operator, this example will tell Terraform to use the provider plugin of higher version than the set value:

<details>
<summary>AWS example</summary>

```hcl
provider "aws" {
region  = "eu-west-2"
version = "> 2.8"
}
```

If your current version of the *aws* plugin is lesser than 2.8 then run the following command to download the plugin version 2.8:
`terraform init -upgrade`

</details>

Here's an example of using the `~>`, the number provided on the right of the arrow acts as the lower boundary when selecting the version number to download:

<details>
<summary>AWS example</summary>

```hcl
provider "aws" {
region  = "eu-west-2"
version = "~> 2.8"
}
```

In this example the version specified translates that the provider plugin version to be used should be no lower than `2.8.0` but not greater than `3.0.0`. 
In the declaration the zero is omitted as it would be inferred by terraform. 
The first digit `2` means that only major releases of `2` should be used.  

If your current version of the *aws* plugin is lesser than 2.8 then run the following command to download the plugin version 2.8:
`terraform init -upgrade`

</details>

### Provider aliases

You can declare multiple blocks for the same provider in your configuration. 
One scenario where you may want or need to do this is when you have resources with the same cloud provider but in multiple regions. 
You can configure one provider for each region to accommodate this scenario.

To identify multiple instances of a single provider, you must add an alias. 
The alias is used by resources to indicate which instance of the provider to use.

One default provider is allowed. 
The default instance doesn’t specify an alias and is used by default when resources don’t specify a specific provider.

To refer to a specific instance inside of a resource block, you add a provider key. 
The value of the provider is a string beginning with the provider type followed by dot and the assigned alias.

Here is an example of giving provider an alias:

<details>
<summary>AWS example</summary>

```hcl
provider "aws" {
region  = "eu-west-2"
alias   = "aws-uk"
}

resource "aws_instance" "example" {
  provider = "aws.aws-uk"
  ami           = var.ami
  instance_type = var.type
}

```

In this example you can see a provider declaration where an alias is used. 
Additionally the resource will now be using this specific provider through the alias. 
As this example is about aws provider in order to refere to the alias you would need to do it through `aws.` notation.

</details>
