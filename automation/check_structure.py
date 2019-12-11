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

def get_files(item):
    files = []
    all_files = Path(".").glob(get_property(item, 'path'))
    for f in all_files:
        files.append(str(f))
    return files       

def regex_check(item, path):
    good_list = []
    split_item = path.split("/")[-1]
    for i in get_property(item, 'spec'):
        match = re.compile(i['match'])
        if match.search(split_item) != None:
            good_list.append(path)
    return good_list

def validate():    
    broken = []
    for item in yaml_file:
        file_list = get_files(item)
        for file_path in file_list:
            correct_format = regex_check(item, file_path)
            if file_path not in correct_format:
                broken.append({'source':file_path, 'error':get_property(item, 'desc')})
    return broken

            
def errormsg(broken_items):
    msg = ""
    for item in broken_items:
        msg += "\n" + "source: " + item['source'] + "\n" + "error: " + item['error'] + "\n" + "---------------------------------------------------------------" + "\n"
    if msg:
        raise Exception(msg)

errormsg(validate())

