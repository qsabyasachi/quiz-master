from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from pymongo import MongoClient



app = Flask(__name__);

app.config["SECRET_KEY"] = "secret key"
DEBUG_TB_PROFILER_ENABLED = True
toolbar = DebugToolbarExtension(app)

# client = MongoClient("mongodb://eduardo:secretPassword@127.0.0.1/classroomdb")
# client = MongoClient("mongodb://127.0.0.1:27017/classroomdb")

client = MongoClient("mongodb://127.0.0.1:27017/classroomdb")
db = client.classroomdb

# cars = [ {'name': 'Audi', 'price': 52642},
#     {'name': 'Mercedes', 'price': 57127},
#     {'name': 'Skoda', 'price': 9000},
#     {'name': 'Volvo', 'price': 29000},
#     {'name': 'Bentley', 'price': 350000},
#     {'name': 'Citroen', 'price': 21000},
#     {'name': 'Hummer', 'price': 41400},
#     {'name': 'Volkswagen', 'price': 21600} ]
#
# with client:
#
#     db = client.testdb
#     db.cars.insert_many(cars)

# with client:
#
#     db = client.classroomdb
#
#     users = db.users.find()
#
#     for user in users:
#         print(user)


from quiz.quiz.controllers.quiz import routes, CourseController, QuestionController, TopicController, UserController, TestController, AnswerController, ClassController
