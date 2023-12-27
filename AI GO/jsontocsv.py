import pandas as pd
import json

with open("/Users/jimmywang/Desktop/Jupyter/ML/AI GO/taipei_park.json") as f:
    json_data = json.load(f)

df = pd.read_json(json_data)
df.to_csv("output.csv", index=False)