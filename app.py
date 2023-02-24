from flask import Flask
from flask import request
from pymongo import MongoClient
import json
import bcrypt
import pymongo
import datetime

app = Flask(__name__)


@app.route("/api/v1/signup", methods=['POST'])
def signup():
    content = request.json
    email=content.get('email')
    password=content.get('password')
    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)
    # printing the salt
    print("Salt :")
    print(salt)
 
    # printing the hashed
    print("Hashed")
    print(hashed)
    print content
    print email
    print password
    myclient = pymongo.MongoClient("mongodb://appuser:appuser1@ac-1k7xrfw-shard-00-00.qu56bir.mongodb.net:27017,ac-1k7xrfw-shard-00-01.qu56bir.mongodb.net:27017,ac-1k7xrfw-shard-00-02.qu56bir.mongodb.net:27017/?ssl=true&replicaSet=atlas-ifammd-shard-0&authSource=admin&retryWrites=true&w=majority");
    mydb = myclient['HealthData']
    mycol = mydb["Users"]

    mydict = {}
    mydict["email"] = email
    mydict["password"] = password
    mydict["created_at"] = datetime.datetime.now()
    mydict["updated_at"] = datetime.datetime.now()

    x = mycol.insert_one(mydict)

    print(x)

    return "<p>signup, coming soon!</p>"

@app.route("/api/v1/login")
def login():
    return "<p>login, coming soon!</p>"

@app.route("/api/v1/profile")
def profile():
    return "<p>profile, coming soon!</p>"