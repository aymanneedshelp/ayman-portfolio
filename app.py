# app.py
from flask import Flask, render_template
import json

app = Flask(__name__)

def load_data():
    with open('static/data/projects.json', 'r') as f:
        projects = json.load(f)
    with open('static/data/experience.json', 'r') as f:
        experience = json.load(f)
    return projects['projects'], experience['experiences']

@app.route('/')
def home():
    projects, experiences = load_data()
    return render_template('index.html', projects=projects, experiences=experiences)

if __name__ == '__main__':
    app.run(debug=True)