from flask import Flask 

app = Flask(__name__)

def build():
	from flask_frozen import Freezer
	freezer = Freezer(app)
	freezer.freeze()

if __name__ == '__main__':
	main()