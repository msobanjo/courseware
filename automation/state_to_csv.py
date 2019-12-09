#! /usr/bin/env python
import pandas as pd
import json
from pandas.io.json import json_normalize

with open("./state.json", "r") as file:
    state = json.load(file)

#df = json_normalize(state)
for i in state:
    print(state[i])
#print(df.head)