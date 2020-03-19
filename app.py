from flask import Flask, render_template

app = Flask(__name__)

STUDENT_NAME = "Chris Pondoc"

@app.route('/')
def return_index():
    return render_template('index.html', title="🏠 Home", description="Home is where the heart is!", student_name = STUDENT_NAME)

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