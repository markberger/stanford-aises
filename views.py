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