#! /usr/bin/env python
import subprocess
from subprocess import check_output
import os

print("Tearing Down Lab Environment...")
subprocess.check_output(["terraform","destroy","-auto-approve","lab-setup/infrastructure"])