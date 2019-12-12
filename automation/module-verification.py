#! /usr/bin/env python

import yaml
import re
import os
from functions import get_state

with open('./automation/module.yaml') as module_yaml:
    specs = yaml.load(module_yaml, Loader=yaml.FullLoader)


def get_modules():
    # TODO REMOVE
    return ["/tmp/module.md"]
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

def get_non_code_block_lines(lines):
    non_code_block_lines = []
    code_block = False
    for line in lines:
        if line.startswith("```"):
            code_block = not code_block
        if not code_block:
            non_code_block_lines.append(line)
    return non_code_block_lines

def match_spec(line, specs):
    for index, spec in enumerate(specs):
        pattern = re.compile(spec['heading'])
        match = pattern.search(line)
        if match:
            return True, index;
    return False, 0;

def wrong_order_error(order, module, specs):
    print("File: {0}\nDescription: The headings are in the wrong order.".format(module))
    for index, spec in enumerate(specs):
        if index != order[index]:
            if index > order[index]:
                if len(
                print("Heading {0} should be after the {1} and before the {2}".format(spec[index]['name'], spec[index-1]['name'],spec[index+1]['name'] ))


def get_errors():
    errors = []
    for module in get_modules():
        with open(module) as readme_file:
            readme_lines = readme_file.readlines()
        lines = get_non_code_block_lines(readme_lines)

        order = []

        for line in lines:
            matched, spec_index = match_spec(line, specs)
            if matched:
                order.append(spec_index)

        if sorted(order) != order:
            wrong_order_error(order, module, specs)

        for index, spec in enumerate(specs):
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

