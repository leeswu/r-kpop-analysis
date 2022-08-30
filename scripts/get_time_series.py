import pandas as pd
import numpy as np
import json

def get_time_resample(times, freq):
    df = pd.DataFrame({'Timestamp': times, 'Count': 1})
    df = df.set_index(['Timestamp'])
    df.index = pd.to_datetime(df.index, unit='s')

    df = df.resample(freq).sum()

    time_series = df.reset_index().values.tolist()

    for stamp in time_series:
        stamp[0] = stamp[0].strftime('%Y-%m-%d %X')

    return time_series


with open("./processed_data/group_data_complete.json") as f:
    data = json.load(f)

for group in data.values():
    times = group["Created"]
    times.sort()

    time_series = get_time_resample(times, 'W')

    group["Time Series"] = time_series

with open('./processed_data/group_data_time.json', 'w') as f:
    json.dump(data, f, indent=2)