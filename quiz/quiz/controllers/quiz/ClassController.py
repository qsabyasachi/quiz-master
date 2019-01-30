from flask import jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from bson.objectid import ObjectId

from quiz.run import app
from quiz import db

#Returning all user classes
@app.route("/quiz/classes/", methods=["GET"])
def get_classes():
    result = db.classes.find( {"creator._id": ObjectId(session["_id"])} )

    classes = []

    for c in result:
        c["_id"] = str(c["_id"])
        c["creator"]["_id"] = str(c["creator"]["_id"])

        classes.append(c)

    return jsonify(classes)
