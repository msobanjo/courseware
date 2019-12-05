#! /usr/bin/env python
import yaml
import os
import re
from pathlib import Path

with open('./automation/structure.yaml') as file:
    yaml_file = yaml.load(file, Loader=yaml.FullLoader)

def get_property(item, prop):
    if 'type' not in item:
        raise Exception('child does not have "{0}" field set: {1}'.format(prop,str(item)))
    else:
        return item[prop]

def iterate(children, depth=0):
    for child in children:
        print(get_property(child, 'type'))
        if 'children' in child:
            iterate(child['children'], depth + 1)



root_dir = "./topics"
folder_pattern = re.compile("^[a-z0-9_\-]+$")
file_pattern = "README.md"

def iterate(directory, depth=0):
    broken = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            if folder_pattern.search(name) ==  None:
                broken.append(root + name)
        for name in files:
            if name != file_pattern:
                broken.append(root + name)
    for item in broken:
        print(item)

iterate(root_dir)


