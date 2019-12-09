import pandas as pd
from pandas.io.json import json_normalize

state = "./state.json"
df = json_normalize(state)

print(df.head)