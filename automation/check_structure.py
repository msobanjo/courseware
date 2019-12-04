#! /usr/bin/env python
import yaml

with open('./automation/structure.yaml') as file:
    test = yaml.load(file, Loader=yaml.FullLoader)

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

iterate(test)

