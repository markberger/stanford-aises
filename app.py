from flask import Flask 
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/calendar')
def calendar():
	return render_template('calendar.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/corporate')
def corporate():
	return render_template('corporate.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

def main():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	main()