from flask import jsonify, request, render_template


from quiz import app
from quiz import db

#creating new discipline
@app.route("/quiz/courses/", methods=["POST"])
def create_course():
    name = request.form.get("name")

    db.courses.insert({"name": name})

    return "OK"


#Returning all courses in DB
@app.route("/quiz/courses/", methods=["GET"])
def get_all_courses():
    result = db.courses.find()

    courses = []
    for item in result:
        if item["_id"]:
            item["_id"] = str(item["_id"])
        courses.append(item)
        # print(courses)
        return jsonify(courses)
