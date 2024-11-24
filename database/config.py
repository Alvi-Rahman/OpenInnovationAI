"""
File for database configurations
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from pymongo import MongoClient
import _constants as C


def get_mongo_client():
    """
    Sets up a MongoClient and returns the object
    """
    client = MongoClient(C.MONGODB_URI)
    db_connection = client[C.MONGODB_DATABASE]
    return db_connection


def get_collection(db: MongoClient, collection_name: str):
    """
    Gets specified collection and returns it
    """
    collection = db[collection_name]
    return collection
