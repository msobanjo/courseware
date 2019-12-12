#! /usr/bin/env python

import yaml
import re
import os
from functions import get_state

with open('./automation/module.yaml') as module_yaml:
    specs = yaml.load(module_yaml, Loader=yaml.FullLoader)


def get_modules():
    modules = []
    state = get_state()
    for topic in state['topics']:
        for module in topic['modules']:
            modules.append(module['gitUri'] + '/README.md')
    return modules

def get_count_for_spec(spec):
    if 'count' in spec:
        return spec['count']
    else:
        return 1


def get_matches(lines, spec):
    matched = []
    pattern = re.compile(spec['heading'])
    code_block = False
    for line in lines:
        if line.startswith("```"):
            code_block = not code_block

        match = pattern.search(line)
        if match and not code_block:
            matched.append(match)
    return matched

def get_errors():
    errors = []
    for module in get_modules():
        with open(module) as readme_file:
            readme_lines = readme_file.readlines()

        for spec in specs:
            matched = get_matches(readme_lines, spec)
            count = get_count_for_spec(spec)

            if len(matched) < count:
                errors.append("File: {2}\nDescription: There needs to be at least {0} {1}\n".format(count, spec['description'], module))
            elif len(matched) > count:
                errors.append("File: {2}\nDescription: There can be no more than {0} {1}\n".format(count, spec['description'], module))
    return errors

errors = get_errors()

if len(errors) > 0:
    rows, columns = os.popen('stty size', 'r').read().split()
    seperator = '\n' + ('=' * int(columns)) + '\n'
    raise Exception(seperator + seperator.join(errors) + '\n\nError count: ' + str(len(errors)))

