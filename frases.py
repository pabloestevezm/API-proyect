from app import app_
from pymongo import MongoClient
from src.config import DBURL
from flask import request
import re
from src.helpers.error_helper import errorHelper, APIError, Error404, checkValidParams
from src.helpers.js_answ import data
import json

client = MongoClient(DBURL)
print(f"connected to db {DBURL}")
frases_api = client.get_default_database()["frases"]

@app_.route("/company/")
@errorHelper()
def ljkahlsd():
    raise Error404("Please provide a name")

# app.route("/company/")(errorHelper()
#                        (lambda: (_ for _ in ()).throw(Error404("Please provide a name"))))

"""
@app_.route("/company/<name>")
@errorHelper(["detailed"])
def getCompany(name):
    # name = request.args.get("name") # this is from query params ?...
    print(f"Requesting info for company {name}")

    namereg = re.compile(f"^{name}", re.IGNORECASE)

    # if the query param detailed is present, show all company info
    info = {"_id": 0, "name": 1, "home_url": 1,
            "email_address": 1, "founded_year": 1}

    # checkValidParams(["detailed"])

    if request.args.get("detailed") == "1":
        print("DETAILED INFO")
        info = {"_id": 0}
    else:
        print("BASIC INFO")

    company = companies.find_one({"name": namereg}, info)

    if not company:
        raise Error404("This company is not found on database")

    return data(company)

"""