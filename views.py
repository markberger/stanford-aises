from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/calendar.html')
def calendar():
	return render_template('calendar.html')

@app.route('/tutoring.html')
def tutoring():
	return render_template('tutoring.html')

@app.route('/projects.html')
def projects():
	return render_template('projects.html')

@app.route('/corporate.html')
def corporate():
	return render_template('corporate.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/regional/index.html')
def regional_conference():
    return render_template('/regional.html')

@app.route('/regional/registration.html')
def conference_registration():
    return render_template('conference-registration.html')

@app.route('/regional/poster-registration.html')
def poster_registration():
    return render_template('poster-registration.html')