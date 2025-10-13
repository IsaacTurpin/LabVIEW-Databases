from pymongo import MongoClient
import json

CLIENT = MongoClient("mongodb://localhost:27017/")
DB = CLIENT["SensorsMDB"]

def insert_device(json_data: str) -> str:
    data = json.loads(json_data)
    collection = DB["Devices"]
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_doc_by_id(collection_name: str, document_id: str) -> str:
    collection = DB[collection_name]
    try:
        document = collection.find_one({"_id": document_id})
    except Exception:
        return ""

    if document is None:
        return ""

    return json.dumps(document, default=str)


