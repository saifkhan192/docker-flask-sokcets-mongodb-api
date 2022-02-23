import os

from pymongo import MongoClient


def get_mongo(db_name):
    mongo_uri = os.environ.get('MONGO_URI')
    client = MongoClient(mongo_uri)
    db = client[db_name]
    return db

def get_mongo_mem_db():
    return get_mongo("memory_db")

def get_mongo_common_db():
    return get_mongo("common_db")

