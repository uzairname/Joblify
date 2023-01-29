import jinja2
from flask import Flask, render_template, request
import os

from database.models import Database
import database.models as models

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
def upload():
    return render_template(jinja_env.get_template("upload.html"))




@app.route('/api/resume', methods=['POST'])
# @cross_origin(supports_credentials=True)
def upload_file():
    print("uploaded")

    data = request.form
    print("resume data", data)

    resume = models.Resume(content=data, user=user)
    resume.save()

    print(data)
    return 1



@app.route('/api/job-posting', methods=['POST'])
# @cross_origin(supports_credentials=True)
def upload_file():
    print("uploaded")

    data = request.form
    print("job data", data)

    job_posting = models.JobPosting(description=data, user=user)
    job_posting.save()

    print(data)
    return 1


@app.route('/api/matches', methods=['GET'])
# @cross_origin(supports_credentials=True)
def get_matches():
    print("getting matches")

    job_posting = models.JobPosting.objects.get(id=job_posting_id)
    job_posting = models.JobPosting.objects.get(id=job_posting_id)

    matches = models.Resume.objects(user=job_posting.user)
    return matches



# @app.route('/api/resume', methods=['GET'])
# # @cross_origin(supports_credentials=True)
# def get_test():
#     print("get request")
#
#     return 1


if __name__ == '__main__':
    db = Database("development")
    db.run_migrations()

    models.Resume.drop_collection()
    models.User.drop_collection()

    user = models.User(name="guy")
    user.save()
    resume = models.Resume(content="resume", user=user)
    resume.save()

    app.run(debug=True, port=5001)
