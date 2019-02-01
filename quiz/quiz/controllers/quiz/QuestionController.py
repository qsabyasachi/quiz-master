import math

from flask import render_template, jsonify, request
from bson.objectid import ObjectId

from quiz import app
from quiz import db

@app.route("/quiz/questions/<question_id>/", methods=["PUT"])
def update_question(question_id):
    title = request.form.get("title")
    correctAnswer = request.form.get("correctAnswer")
    choices = request.form.getlist("choices[]")

    db.questions.update({"_id": ObjectId(question_id)},
    {"$set": {
        "title": title,
        "correctAnswer": correctAnswer,
        "choices": choices
    }})

    return "OK"


#Returning a question by ID
@app.route("/quiz/questions/<question_id>/", methods=["GET"])
def get_question(question_id):
    result = db.questions.find_one( {"_id": ObjectId(question_id)} )

    if result["type"] == "multipleChoice":
        question = {
            "_id": str(result["_id"]),
            "title": result["title"],
            "type": result["type"],
            "correctAnswer": result["correctAnswer"],
            "choices": result["choices"]
        }
    else:
        question = {
            "_id": str(result["_id"]),
            "title": result["title"],
            "type": result["type"],
            "correctAnswer": result["correctAnswer"]
        }

    return jsonify(question)


#registering a new question
@app.route("/quiz/questions/", methods=["POST"])
def create_questions():
    title = request.form.get("title")
    type = request.form.get("type")
    level = request.form.get("level")
    correct_answer = request.form.get("correctAnswer")
    topic_id = request.form.get("topic")
    answers = request.form.getlist("answers[]")

    topic = db.topics.find_one({"_id": ObjectId(topic_id)})

    questions = db.questions
    id = questions.insert_one({
        "title": title,
        "type": type,
        "level": level,
        "correctAnswer": correct_answer,
        "choices": answers,
        "topic": topic
    }).inserted_id

    question = db.questions.find_one({"_id": ObjectId(id)})
    if question["_id"]:
        question["_id"] = str(question["_id"])
        question["topic"]["_id"] = str(question["topic"]["_id"])
        question["topic"]["course"]["_id"] = str(question["topic"]["course"]["_id"])

    return jsonify(question)
