#! /usr/bin/env python
import yaml
import os
import re
from pathlib import Path
import glob

root_dir = "./topics"
broken = []

with open('./automation/structure.yaml') as file:
    yaml_file = yaml.load(file, Loader=yaml.FullLoader)

def get_property(item, prop):
    if prop not in item:
        raise Exception('yaml item does not have "{0}" field set: {1}'.format(prop,str(item)))
    else:
        return item[prop]


for item in yaml_file:
    globbed_list = (glob.glob(get_property(item, 'path')))
    for globbed_item in globbed_list:
            
            split_item = globbed_item.split("/")[-1]
            
            
            folder_match = re.compile(get_property(item, 'spec')[1]['match'])
            file_match = get_property(item, 'spec')[0]['match']
            
            if folder_match.search(split_item) is not None or file_match == split_item:
                continue
            else:
                broken.append(globbed_item)

    
    for i in broken:
        print(i)

            
 
