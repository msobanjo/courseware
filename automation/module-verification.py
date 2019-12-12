#! /usr/bin/env python

import yaml
import re
import os
from functions import get_state

with open('./automation/module.yaml') as module_yaml:
    specs = yaml.load(module_yaml, Loader=yaml.FullLoader)


modules = []
state = get_state()
for topic in state['topics']:
    for module in topic['modules']:
        modules.append(module['gitUri'] + '/README.md')

errors = []
for module in modules:
    print(module)
    with open(module) as readme_file:
        readme_lines = readme_file.readlines()

    for spec in specs:
        print(spec['heading'])
        matched = []
        pattern = re.compile(spec['heading'])
        code_block = False
        for line in readme_lines:
            if line.startswith("```"):
                code_block = not code_block

            match = pattern.search(line)
            if match and not code_block:
                print(line)
                matched.append(match)

        if 'count' in spec:
            count = spec['count']
        else:
            count = 1

        if len(matched) < count:
            errors.append("File: {2}\nDescription: There needs to be at least {0} {1}\n".format(count, spec['description'], module))
        elif len(matched) > count:
            errors.append("File: {2}\nDescription: There can be no more than {0} {1}\n".format(count, spec['description'], module))

if len(errors) > 0:
    rows, columns = os.popen('stty size', 'r').read().split()
    seperator = '\n' + ('=' * int(columns)) + '\n'
    raise Exception(seperator + seperator.join(errors) + '\n\nError count: ' + str(len(errors)))

