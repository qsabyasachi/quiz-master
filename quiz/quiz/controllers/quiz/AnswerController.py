from flask import render_template, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from bson.objectid import ObjectId

from quiz.run import app
from quiz import db

#seeing the details of the answer
@app.route("/quiz/answers/<answer_id>/", methods=["GET"])
def see_answer(answer_id):

    answer = db.answers.find_one(
             {
                "_id" : ObjectId(answer_id)
             })
    print(answer)

    return render_template("quiz/answers/see.html", answer=answer)


#updating quiz note
@app.route("/quiz/answers/<answer_id>/", methods=["PUT"])
def update_grade(answer_id):
    grade = int(request.form.get("grade"))
    answer = db.answers.find_one(
             {
                "_id" : ObjectId(answer_id)
             })

    answer["grade"] = grade

    db.answers.update(
    {
        "_id" : ObjectId(answer_id)},
        answer
    )

    return "Ok"
