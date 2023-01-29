import jinja2
from flask import Flask, render_template, request
import pymongo as pm
import os
import time
import mongoengine as me

from flask_cors import CORS, cross_origin

from database.models import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template(jinja_env.get_template("Home.html"))

@app.route('/login.html')
def login():
    return render_template(jinja_env.get_template("login.html"))

@app.route('/sign-up.html')
def sign_up():
    return render_template(jinja_env.get_template("sign-up.html"))

@app.route('/upload.html')
def sign_up():
    return render_template(jinja_env.get_template("upload.html"))




@app.route('/api/resume', methods=['POST'])
# @cross_origin(supports_credentials=True)
def upload_file():
    print("uploaded")

    data = request.form
    print("resume data", data)

    resume = Resume(content=data, user=user)
    resume.save()

    print(data)
    return 1


# @app.route('/api/resume', methods=['GET'])
# # @cross_origin(supports_credentials=True)
# def get_test():
#     print("get request")
#
#     return 1




def connect_db(db_name):

    start_time = time.time()
    uri = os.environ.get('MONGODB_URI')
    if uri is None:
        raise RuntimeError("MONGODB_URI not found in environment.")

    me.connect(host=uri, db=db_name)
    client = pm.MongoClient(os.environ.get('MONGODB_URI'))
    db = client[db_name]

    print(f"Connected to database \"{db_name}\" in {time.time() - start_time} seconds.")
    return db

class Database:
    def __init__(self, db_name):
        self.db = connect_db(db_name)

    def run_migrations(self):
        """
        This is run every time the bot starts.
        """

        # find the database version
        try:
            version = DbSettings.objects.get().database_version
        except me.DoesNotExist:
            setting = DbSettings(database_version=1)
            setting.save()
            version = 0

        # run migrations
        if version == 0:
            self.v1()
            version = 1

        if version == 1:
            self.v2()
            version = 2

        print("Ran migrations.")

    def v1(self):
        DbSettings.objects.get().update(database_version=1)

    def v2(self):
        self.db["users"].update_many({}, {"$set": {"name":None}})
        self.db["resumes"].update_many({}, {"$set": {"user":None}})
        DbSettings.objects.get().update(database_version=2)


if __name__ == '__main__':
    db = Database("development")
    db.run_migrations()

    Resume.drop_collection()
    User.drop_collection()

    user = User(name="guy")
    user.save()
    resume = Resume(content="resume", user=user)
    resume.save()

    app.run(debug=True, port=5001)
