from pymongo import MongoClient

from constants import CONSTANTS


def get_db():
    client = MongoClient(CONSTANTS['DB_URL'])
    db = client[CONSTANTS['DB_NAME']]
    return db


DB = get_db()
