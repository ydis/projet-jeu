import sys
from pymongo import MongoClient


def get_database():

    client = MongoClient("mongo://localhost:27017")
    db = client["game_db"]
    characters = db["characters_db"]
    return db