#! /usr/bin/env python

import yaml
import re


with open('./automation/module.yaml') as module_yaml:
    specs = yaml.load(module_yaml, Loader=yaml.FullLoader)

file = '/tmp/module.md'

with open(file) as readme_file:
    readme_lines = readme_file.readlines()


for spec in specs:
    print("spec: {0}".format(spec))
    matched = []
    pattern = re.compile(spec['heading'])
    for line in readme_lines:
        match = pattern.search(line)
        if match:
            matched.append(match)
    if len(matched) == 0:
        raise Exception("There needs to be at least one {0} in the file: {1}".format(spec['description'], file))
    else if len(matched > 1):
        raise Exception("There needs to be at least one {0} in the file: {1}".format(spec['description'], file))

