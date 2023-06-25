import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies=hobbiesArray)

@app.route('/experience')
def experience():
    return render_template('workExperience.html')

@app.route('/places')
def places():
    return render_template('places.html', title="Places")

@app.route('/education')
def education_page():
    return render_template('education.html', title='Education', education=education)
