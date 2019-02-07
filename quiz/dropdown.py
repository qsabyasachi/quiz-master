from flask import render_template, Flask
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "secret key"


@app.route('/')
@app.route('/index')
def index():
    # user = {'name': 'Bob'}

    # client = MongoClient('mongodb://localhost:27017/')
    # db = client['test-database']
    #
    # collection = db.test_collection
    # posts = db.posts
    # name_list = [p['name'] for p in posts.find({'type': "server"})]

    return render_template('drop_down.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
