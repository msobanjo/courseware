#! /usr/bin/env python
import yaml
import os
import re
from pathlib import Path
import glob

with open('./automation/structure.yaml') as file:
    yaml_file = yaml.load(file, Loader=yaml.FullLoader)

def get_property(item, prop):
    if prop not in item:
        raise Exception('yaml item does not have "{0}" field set: {1}'.format(prop,str(item)))
    else:
        return item[prop]


def check():    
    good_list = []
    broken_list= []
    for item in yaml_file:
        globbed_list = []
        all_files = Path(".").glob(get_property(item, 'path'))
        for f in all_files:
            globbed_list.append(str(f))
        
        for globbed_item in globbed_list:
            
            split_item = globbed_item.split("/")[-1]

            for i in get_property(item, 'spec'):
                match = re.compile(i['match'])
                if match.search(split_item) != None:
                    good_list.append(globbed_item)

            if globbed_item not in good_list:
                broken_list.append(globbed_item)
    
    return broken_list

            
broken = check()
for i in broken:
    print (i)
