import routes, CourseController, QuestionController, TopicController, UserController, TestController, AnswerController, \
    ClassController
from flask import render_template, request, redirect, session, jsonify

from quiz import app
from quiz import db

#Redirecting to the application index
@app.route("/quiz/", methods=["GET"])
def index():
    if "email" in session:
        created_tests = db.tests.find(
                        {
                            "creator.email" : session["email"]
                        })
        tests = db.tests.find(
                {
                    "people" : session["email"]
                })

        return render_template("quiz/index.html", created_tests=created_tests, tests=tests)

    return redirect("/quiz/login/")

#Redirecting to dashboard
@app.route("/quiz/dashboard/", methods=["GET"])
def dashboard():
    co_urse = CourseController.get_all_courses()
    return render_template("quiz/dashboard/index.html", co_urse=co_urse)
