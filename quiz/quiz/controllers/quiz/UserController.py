from flask import jsonify, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from quiz.run import app
from quiz import db

#Returning all users in DB
@app.route("/quiz/users/", methods=["GET"])
def get_all_users():
    result = db.users.find()

    users = []
    for item in result:
        if item["_id"]:
            item["_id"] = str(item["_id"])
        users.append(item)

    return jsonify(users)


#Redirecting user to login page
@app.route("/quiz/login/", methods=["GET"])
def redirect_login():
    return render_template("quiz/login/index.html")


#Verifying User Authentication
@app.route("/quiz/login/", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = db.users.find_one(
            {
                "email": email
            })
    if user:
        if check_password_hash(user["password"], password):
            session["email"] = user["email"]
            session["_id"] = str(user["_id"])
            return redirect("/quiz/")

    error = "E-mail or password is incorrect!"
    return render_template("quiz/login/index.html", error=error)


#Redirecting user to signup's page
@app.route("/quiz/signup/", methods=["GET"])
def redirect_signup():
    return render_template("quiz/signup/index.html")


#Registering a new user
@app.route("/quiz/signup/", methods=["POST"])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = generate_password_hash(request.form.get("password"))

    db.users.insert_one(
    {
        "name": name,
        "email": email,
        "password": password
    })

    return redirect("/quiz/")

#System logout
@app.route("/quiz/logout/", methods=["GET"])
def logout():
    session.pop("email", None)
    return redirect("/quiz/login/")
