from flask import Flask
from pymongo import MongoClient
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "secret key"

toolbar = DebugToolbarExtension(app)

client = MongoClient("mongodb://127.0.0.1:27017/classroomdb")
db = client.classroomdb
