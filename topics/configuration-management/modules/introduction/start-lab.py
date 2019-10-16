#! /usr/bin/env python
import subprocess
from subprocess import call
import json

print("Preparing Lab Environment")
# run terraform
call(["terraform","init","lab-setup/infrastructure"])
call(["terraform","apply","-auto-approve","lab-setup/infrastructure"])