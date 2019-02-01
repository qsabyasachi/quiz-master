from flask import jsonify, request
from bson.objectid import ObjectId

from quiz import app
from quiz import db

#creating a new topic
@app.route("/quiz/topics/", methods=["POST"])
def create_topic():
    name = request.form.get("name")
    course_id = request.form.get("courseId")

    course = db.courses.find_one({"_id": ObjectId(course_id)})

    db.topics.insert({"name": name, "course": course })

    return "OK"


#Returning all topics in the DB
@app.route("/quiz/topics/", methods=["GET"])
def get_all_topics():
    result = db.topics.find()

    topics = []
    for item in result:
        if item["_id"]:
            item["_id"] = str(item["_id"])
            item["course"]["_id"] = str(item["course"]["_id"])
        topics.append(item)

    return jsonify(topics)

#Returning all topics by discipline
@app.route("/quiz/courses/<course_id>/topics/", methods=["GET"])
def get_topics_by_course(course_id):

    result = db.topics.find(
             {
                "course._id" : ObjectId(course_id)
             })

    topics = []
    for item in result:
        if item["_id"]:
            item["_id"] = str(item["_id"])
            item["course"]["_id"] = str(item["course"]["_id"])
        topics.append(item)

    return jsonify(topics)
