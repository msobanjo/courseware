#! /usr/bin/env bash
# download and install the latest version of terraform
latest_version=$(curl -Ls https://releases.hashicorp.com/terraform | grep -E -o 'terraform_[0-9]+.[0-9]+.[0-9]+' | head -1 | cut -d _ -f 2)
zip="terraform_${latest_version}_linux_amd64.zip"
wget "https://releases.hashicorp.com/terraform/${latest_version}/${zip}" -O /tmp/${zip}
mkdir -p ~/.local/bin
unzip /tmp/${zip} -d ~/.local/bin/terraform
