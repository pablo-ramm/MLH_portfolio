import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

hobbiesArray = [{
    "name": "Coding",
    "description": "I love coding and learning new things. I am currently learning how to use Flask and how to deploy a website using Heroku."
},{
    "name": "Reading",
    "description": "I love reading books. I am currently reading 'The 7 Habits of Highly Effective People' by Stephen Covey."
},{
    "name": "Playing Video Games",
    "description": "I love playing video games. I am currently playing 'The Legend of Zelda: Breath of the Wild' on the Nintendo Switch."
},{
    "name": "Coding",
    "description": "I love coding and learning new things. I am currently learning how to use Flask and how to deploy a website using Heroku."
},{
    "name": "Reading",
    "description": "I love reading books. I am currently reading 'The 7 Habits of Highly Effective People' by Stephen Covey."
},{
    "name": "Playing Video Games",
    "description": "I love playing video games. I am currently playing 'The Legend of Zelda: Breath of the Wild' on the Nintendo Switch."
}]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def aboutMe():
    return render_template('hobbies.html', hobbies=hobbiesArray)

@app.route('/experience')
def experience():
    return render_template('workExperience.html')

@app.route('/places')
def places():
    return render_template('places.html', title="Places")