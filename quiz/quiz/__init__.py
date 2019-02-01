from flask import Flask
from pymongo import MongoClient



app = Flask(__name__);
app.debug = True
app.config["SECRET_KEY"] = "secret key"
client = MongoClient("mongodb://127.0.0.1:27017/classroomdb")
db = client.classroomdb
