import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime
import requests

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv('MYSQL_DATABASE'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        host=os.getenv('MYSQL_HOST'),
        port=3306
    )


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb

mydb.connect()
print(mydb)
mydb.create_tables([TimelinePost])

hobbiesArray = [{
    "name": "Coding",
    "description": "I like coding and learning new things. I am currently learning how to use Flask and about deploying microservices.",
    "image": "static/img/coding.jpeg"
},{
    "name": "Reading",
    "description": "I love reading books. I am currently reading 'The 7 Habits of Highly Effective People' by Stephen Covey.",
    "image": "static/img/reading.webp"
},{
    "name": "Movies",
    "description": "I watch a lot of movies with my family. My favorite movies are the Indiana Jones series.",
    "image": "static/img/movies.jpeg"
},{
    "name": "Running",
    "description": "I Like going for a run, makes me feel relax. I am planning to run a marathon.",
    "image": "static/img/running.jpeg"
}]

education = [
    {
        "school_name": "Monterrey Institute of Technology and Higher Education",
        "degree": "High School",
        "field_of_study": "",
        "start_year": "2017",
        "end_year": "2020",
        "grade": "90",
        "description": "Completed with honors."
    },
    {
        "school_name": "Monterrey Institute of Technology and Higher Education",
        "degree": "Bachelor's Degree",
        "field_of_study": "Computer Science",
        "start_year": "2020",
        "end_year": "2025",
        "grade": "92",
        "description": "Especializing in Software Engineering."
    }
]
work_experience = [
    {
        "job_title": "Jr Software Engineer",
        "company_name": "Greenapsis",
        "start_date": "March 2023",
        "end_date": "Present",
        "location": "Monterrey, NL",
        "description": "Working on internal tools"
    },
    {
        "job_title": "Intern QA developer",
        "company_name": "Epicor",
        "start_date": "June 2022",
        "end_date": "March 2023",
        "location": "Monterrey, NL",
        "description": "Worked on development for test scripts"
    }
]

@app.route('/')
def index():
    return render_template('about.html', title='name')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies=hobbiesArray)

@app.route('/places')
def places():
    return render_template('places.html', title="Places")

@app.route('/education')
def education_page():
    return render_template('education.html', title='Education', education=education)

@app.route('/experience')
def experience_page():
    return render_template('experience.html', title='Work Experience', work_experience=work_experience)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline", name = "Pablo")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')

    # Validate name
    if not name:
        return {"error": "Invalid name"}, 400

    # Validate content
    if not content:
        return {"error": "Invalid content"}, 400

    # Validate email
    import re
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    sanitization_regex = r'<[^>]*>|[&<>"\']'

    sanitized_name = re.sub(sanitization_regex, '', name)
    sanitized_content = re.sub(sanitization_regex, '', content)

    if not re.fullmatch(email_regex, email):
        return {"error": "Invalid email"}, 400

    timeline_post = TimelinePost.create(name=sanitized_name, email=email, content=sanitized_content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }