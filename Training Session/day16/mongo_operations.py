import os

import pandas as pd
from mongodb import MongoClient
from dotenv import load_dotenv

load_dotenv()
connection_string = os.getenv("MONGODB_URI")

try:
    client = MongoClient(connection_string)
    print("Connected to MongoDB.")

    # Reading from db
    database = client["sample_mflix"]
    collection = database["movies"]

    print(pd.DataFrame(collection.find().limit(5)))

    # Write to db
    database = client["ust_live_quiz"]
    collection = database["basic_collection_test"]

    data_to_insert = {
        "username": "Priyanka",
        "age": 25,
        "completed_series": ["Lost", "Friends", "Stranger Things"],
        "location": "TVM"
    }

    collection.insert_one(data_to_insert)
    print("Data inserted.")

except Exception as e:
    print(e)
