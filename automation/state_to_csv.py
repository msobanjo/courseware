#! /usr/bin/env python
import pandas as pd
import json

with open("./state.json", "r") as file:
    state = json.load(file)

topics = []
modules = []
all_items = []
all_topics = []
count = 0

for i in state["topics"]:
    all_items.append(i["modules"])

for i in all_items:
    while count < len(i):
        item = (i[count]['resourceName'])
        split_item = item.split("/")
        all_topics.append(split_item[0])
        modules.append(split_item[1])
        count += 1
    count = 0

for topic in all_topics:
    if topic not in topics:
        topics.append(topic)
    else:
        topics.append("-")

df = pd.DataFrame(list(zip(topics, modules)), columns=['topics', 'modules'])
df.to_csv('/tmp/state.csv')
