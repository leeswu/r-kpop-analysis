"""
Writes the processed dataset into MongoDB Cloud atlas for API usage
"""

import pymongo
import json
import certifi
from pymongo import MongoClient, InsertOne
import config as cfg

CONNECTION_STRING = cfg.MONGO_SECRET

client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
db = client.kpopDB
collection = db.groupData
requesting = []


with open(r"./processed_data/group_data_time.json") as f:
    data = json.load(f);


for key, value in data.items():
    requesting.append(InsertOne(value))


result = collection.bulk_write(requesting)
client.close()
