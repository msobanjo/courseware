#! /usr/bin/env bash
# install the gcloud sdk using apt
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt install -y apt-transport-https ca-certificates
sudo apt-get update && sudo apt-get install -y google-cloud-sdk
