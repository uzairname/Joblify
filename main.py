from flask import Flask
import pymongo as pm
import os
import time
import mongoengine as me

from flask_cors import CORS, cross_origin


from database.models import *


app = Flask(__name__)


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





@app.route('/upload-file', methods=['POST'])
@cross_origin(supports_credentials=True)
def hello_world(number):
    print("uploaded")

    resume = Resume(content="resume44", user=user)
    resume.save()

    return 'Hello World!'


if __name__ == '__main__':
    db = Database("development")
    db.run_migrations()

    user = User(name="guy")
    user.save()
    resume = Resume(content="resume", user=user)
    resume.save()

    app.run(debug=True)
