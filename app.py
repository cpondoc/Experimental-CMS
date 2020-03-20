from flask import Flask, render_template, send_from_directory
from classes.fetch_data import set_up
import classes.post

app = Flask(__name__)

ASSET_FOLDER = 'assets/'
STUDENT_NAME = "Chris Pondoc"

app.config['ASSET_FOLDER'] = ASSET_FOLDER

@app.route('/posts/<poster>/<subject>')
def view_post(poster, subject):
    list_of = {}
    list_of = set_up()
    for post in list_of:
        if post.poster == poster and post.subject == subject:
            return render_template('view_post.html', title="🔍 View Post", description="Take a closer look.", student_name = STUDENT_NAME, post=post)

@app.route('/assets/<filename>')
def asset_file(filename):
    return send_from_directory(app.config['ASSET_FOLDER'], filename)

@app.route('/')
def return_index():
    list_of = {}
    list_of = set_up()
    return render_template('index.html', title="🏠 Home", description="Home is where the heart is!", student_name = STUDENT_NAME, posts=list_of)

@app.route('/hours')
def return_hours():
    return render_template('hours.html', title="⏱ Hours", description="Staying on top of your time!", student_name = STUDENT_NAME)

@app.route('/activities')
def return_activities():
    return render_template('activities.html', title="🙋‍♂️ Activities", description="Browse from all of the opportunities to serve your community!", student_name = STUDENT_NAME)

@app.route('/resources')
def return_resources():
    return render_template('resources.html', title="📚 Resources", description="Everything at your disposal!", student_name = STUDENT_NAME)

@app.route('/settings')
def return_settings():
    return render_template('settings.html', title="⚙️ Settings", description="Settings to manage your experience!", student_name = STUDENT_NAME)