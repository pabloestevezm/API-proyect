
from src.app import app
from src.config import DBURL
from flask import Flask
from pymongo import MongoClient

client = MongoClient(DBURL)
print(f"connected to db {DBURL}")
db = client.get_database()

@app.route("/user/<username>")
def create_user(username):
    """
    This function creates new users, in case that username exists, returns APIerror.
    """
    if db.users.find_one({"username":username}) == None:
        db.users.insert({"username":username})
        return str(db.users.find_one({"username":username},{"username":0})["_id"])