#! /usr/bin/env python
# helper function library
from pathlib import Path
import os
import re
import json

def get_overview(contents):
    overview_list = re.findall(r"(?<=## Overview\n).*", contents)
    overview = ""
    if len(overview_list) > 0:
        overview = overview_list[0]
    return overview

def get_title(contents):
    title_list = re.findall(r"(?<=# ).*", contents)
    title = ""
    if len(title_list) > 0:
        title = title_list[0]
    else:
        print("no title in given contents")
        exit(1)
    return title

def get_module_props(module):
    module_readme = open(module + "/README.md", "r")
    contents = module_readme.read()
    props_list = re.findall(r"(?<=<!--PROPS\n)((.*\n)*)(?=-->)", contents)
    props_string = "{}"
    if len(props_list) > 0:
        props_string = props_list[0][0].strip()
    module_readme.close()
    props = json.loads(props_string)
    props["path"] = module
    props["overview"] = get_overview(contents)
    props["name"] = get_title(contents)
    return props

def get_all_modules_for_topic(topic):
    items = Path(topic).glob("modules/*")
    module_paths = filter(lambda item: os.path.isdir(item), items)
    module_paths = map(lambda module: str(module), module_paths)
    modules = []
    for module in module_paths:
        modules.append(get_module_props(module))
    return modules

def get_all_topics():
    items = list(Path("./topics").glob("*"))
    topics = filter(lambda item: os.path.isdir(item), items)
    return map(lambda topic: "./" + str(topic), topics)

def get_state():
    state = {
        "topics": []
    }
    for topic in get_all_topics():
        state["topics"].append({
            "path": topic,
            "modules": list(get_all_modules_for_topic(topic))
        })
    return state

