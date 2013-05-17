from flask import Flask 
from flask import render_template

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/calendar.html')
def calendar():
	return render_template('calendar.html')

@app.route('/projects.html')
def projects():
	return render_template('projects.html')

@app.route('/corporate.html')
def corporate():
	return render_template('corporate.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

def main():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

def build():
	from flask_frozen import Freezer
	freezer = Freezer(app)
	freezer.freeze()

if __name__ == '__main__':
	main()