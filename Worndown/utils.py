from db_init import get_database
import models
db = get_database()

def get_characters_collection():
    collection = db["characters_db"]
    return [char for char in collection]

def get_monsters_collection():
    collection = db["monster_db"]
    return [mons for mons in collection]

def converter_char_into_object(character):
    models.character(name = character["name"], pv = character["pv"], atk = character["atk"], defce = character["defce"])

def converter_mons_into_object(monster):
    models.monster(name = monster["name"], pv = monster["pv"], atk = monster["atk"], defce = monster["defce"])
