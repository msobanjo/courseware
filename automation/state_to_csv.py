#! /usr/bin/env python
import pandas as pd
import json

with open("./state.json", "r") as file:
    state = json.load(file)

all_module_items = []
for i in state["topics"]:
    all_module_items.append(i["modules"])

def topics_modules_lists(item_list):
    count = 0
    topics = []
    modules = []
    for i in item_list:
        while count < len(i):
            item = (i[count]['resourceName'])
            split_item = item.split("/")
            topics.append(split_item[0])
            modules.append(split_item[1])
            count += 1
        count = 0
    return topics, modules

def refactor_topics(topics_list):
    refactored_topics = []
    for topic in topics_list:
        if topic not in refactored_topics:
            refactored_topics.append(topic)
        else:
            refactored_topics.append("-")
    return refactored_topics

df = pd.DataFrame(list(zip(refactor_topics(topics_modules_lists(all_module_items)[0]), topics_modules_lists(all_module_items)[1])), columns=['topics', 'modules'])