#! /usr/bin/env python

import yaml
import re


with open('./automation/module.yaml') as module_yaml:
    specs = yaml.load(module_yaml, Loader=yaml.FullLoader)

file = '/tmp/module.md'

with open(file) as readme_file:
    readme_lines = readme_file.readlines()


errors = ""

for spec in specs:
    print("spec: {0}".format(spec))
    matched = []
    pattern = re.compile(spec['heading'])
    for line in readme_lines:
        match = pattern.search(line)
        if match:
            matched.append(match)

    if 'count' in spec:
        count = spec['count']
    else:
        count = 1

    if len(matched) < count:
        errors = errors + "There needs to be at least {0} {1} in the file: {2}\n".format(count, spec['description'], file)
    elif len(matched) > count:
        errors = errors + "There can be no more than {0} {1} in the file: {2}".format(count, spec['description'], file)

if errors:
    raise Exception(errors)
