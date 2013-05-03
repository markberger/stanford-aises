from flask import Flask 
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calendar')
def calendar():
	return render_template('calendar.html')

def main():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	main()