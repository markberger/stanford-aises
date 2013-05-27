from fabric.api import local, env, run, put
from flask_frozen import Freezer
from main import app
from fab_settings import *

env.user = USER
env.hosts = HOSTS

def freeze():
	print("Building static version of app...")
	freezer = Freezer(app)
	freezer.freeze()
	print("Freezing complete.")

def deploy(servName="test"):
	if servName == "test":
		print "Deploying to stanford-aises.herokuapp.com"
		local("git push heroku master")
	if servName == "production":
		print "Deploying to Stanford AFS"
		freeze()
		print "Uploading files to AFS"
		put("build/*", "~/aises/WWW")

