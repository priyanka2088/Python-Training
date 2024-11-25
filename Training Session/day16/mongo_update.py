import os

import pandas as pd
from mongodb import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()
connection_string = os.getenv("MONGODB_URI")

try:
    client = MongoClient(connection_string)
    print("Connected to MongoDB.")

    database = client["ust_live_quiz"]
    collection = database["basic_collection_test"]
    document_id = ObjectId("67383929ff9b6251fcbab5f7")

    # Print based on id
    print(pd.DataFrame(collection.find_one({"_id": document_id})))

    new_data = {"name": "Priyanka", "age": 25, "city": "TVM"}

    # Update db
    result = collection.update_one(
        {"_id": document_id},
        {"$set": new_data}
    )

    if result.matched_count > 0:
        print("Updated successfully.")
        # Print based on id
        print(pd.DataFrame(collection.find_one({"_id": document_id})))
except Exception as e:
    print(e)
