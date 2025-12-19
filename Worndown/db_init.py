import sys
from pymongo import MongoClient


def get_database():
    client = MongoClient("mongodb://localhost:27017")
    db = client["game_db"]
    return db