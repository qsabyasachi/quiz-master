from quiz import app
from quiz.controllers.quiz import routes, CourseController, QuestionController, TopicController, UserController, TestController, AnswerController, ClassController
# app.run(debug=True)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
