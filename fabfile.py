from fabric.api import local
from fabric.api import put
from fabric.api import task
from fabric.api import execute
from flask_frozen import Freezer
from main import app

HOST = "corn.stanford.edu"

@task
def freeze():
	print("Building static version of app...")
	freezer = Freezer(app)
	freezer.freeze()
	print("Freezing complete.")

def pushToAFS():
        put("build/*", "/afs/ir.stanford.edu/group/aises/WWW")

@task
def deploy(servName="test"):
	if servName == "test":
		print "Deploying to stanford-aises.herokuapp.com"
		local("git push heroku master")
	if servName == "production":
		print "Deploying to Stanford AFS"
		freeze()
		print "Uploading files to AFS"
		user = raw_input("SUNetID: ")
		execute(pushToAFS, hosts=[user+'@'+HOST])

