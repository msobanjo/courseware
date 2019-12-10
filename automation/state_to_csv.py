#! /usr/bin/env python
import pandas as pd
import json

with open("./state.json", "r") as file:
    state = json.load(file)

all_module_items = []
for i in state["topics"]:
    all_module_items.append(i["modules"])

def topics_list(item_list):
    count = 0
    topics = []
    for i in item_list:
        while count < len(i):
            item = (i[count]['resourceName'])
            split_item = item.split("/")
            topics.append(split_item[0])
            count += 1
        count = 0
    return topics

def modules_list(item_list):
    count = 0
    modules = []
    for i in item_list:
        while count < len(i):
            item = (i[count]['resourceName'])
            split_item = item.split("/")
            modules.append(split_item[1])
            count += 1
        count = 0
    return modules
    
def refactor_topics(topics_list):
    refactored_topics = []
    for topic in topics_list:
        if topic not in refactored_topics:
            refactored_topics.append(topic)
        else:
            refactored_topics.append("-")
    return refactored_topics


df = pd.DataFrame(list(zip(refactor_topics(topics_list(all_module_items)), modules_list(all_module_items))), columns=['topics', 'modules'])
df.to_csv('/tmp/state.csv')
