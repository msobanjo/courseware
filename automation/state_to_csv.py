#! /usr/bin/env python
import pandas as pd
import json

with open("./state.json", "r") as file:
    state = json.load(file)

topics = []
modules = []
all_items = []
count = 0

for i in state["topics"]:
    all_items.append(i["modules"])

for i in all_items:
    while count < len(i):
        item = (i[count]['resourceName'])
        split_item = item.split("/")
        topics.append(split_item[0])
        modules.append(split_item[1])
        count += 1
    count = 0


df = pd.DataFrame(list(zip(topics, modules)), columns=['topics', 'modules'])
df.to_csv('/tmp/state.csv')