from flask import render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask

app = Flask(__name__);

app.config["SECRET_KEY"] = "secret key"

app = Flask(__name__);
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
    return render_template("quiz/dashboard/index.html")


app.run(debug=True)
# if __name__ == '__main__':
#     app.run(host='127.255.255.254', port=5000)