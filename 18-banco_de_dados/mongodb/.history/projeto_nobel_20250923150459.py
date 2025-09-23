import requests
from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

for collection_name in ["prizes", "laureates"]:
    response = requests.get(
        f"https://api.nobelprize.org/v1/{collection_name[:-1]}.json"
    )
    
    documents = response.json()[collection_name]
    db[collection_name].insert_many(documents)
    
