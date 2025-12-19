from db_init import get_database
import models

db = get_database()

def get_characters_collection():
    collection = db["characters_db"]
    return [models.character(name=char["name"], pv=char["PV"], atk=char["ATK"], defce=char["DEF"]) for char in collection.find()]    


def get_monsters_collection():
    collection = db["monster_db"]
    return [models.monster(name=m["name"], pv=m["PV"], atk=m["ATK"], defce=m["DEF"]) for m in collection.find()]

def save_score(username, waves):
    score = db["scores_db"]
    score.insert_one({"username": username, "waves": waves})

def get_top_score(limit = 3):
    score = db["scores_db"]
    return list(score.find().sort("waves", -1).limit(limit))
