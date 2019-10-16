#! /usr/bin/env bash

# path setup
if ! grep 'PATH=~/.local/bin;$PATH' ~/.bashrc > /dev/null; then 
    echo 'PATH=~/.local/bin;$PATH' >> ~/.bashrc
fi
prerequisites=( "apt_packages" "pip" "ansible" "aws_cli" "gcloud_sdk" "terraform" )
for prerequisite in "${prerequisites[@]}"; do
    echo installing ${prerequisite}
    ./installers/${prerequisite}.sh > /tmp/${prerequisite}-$(date +%s).log
    if [[ $? != 0 ]]; then
        exit
    fi
done

cp ./installers/lab-* ~/.local/bin
