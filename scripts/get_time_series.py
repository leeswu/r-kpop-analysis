import pandas as pd
import numpy as np
import json

def get_time_resample(times, freq):
    time_series = []

    df = pd.DataFrame({'Timestamp': times, 'Count': 1})
    df = df.set_index(['Timestamp'])
    df.index = pd.to_datetime(df.index, unit='s')

    df = df.resample(freq).sum()

    resample = df.reset_index().values.tolist()

    for stamp in resample:
        time_series.append({"Week": stamp[0].strftime('%Y-%m-%d'), "Count": stamp[1]})

    return time_series


with open("./processed_data/group_data_complete.json") as f:
    data = json.load(f)

for group in data.values():
    times = group["Created"]
    times.sort()

    time_series = get_time_resample(times, 'W')

    group["Time Series"] = time_series

with open('./processed_data/group_data_cleaned.json', 'w') as f:
    json.dump(data, f, indent=2)