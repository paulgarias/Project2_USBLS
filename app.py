from flask import Flask, render_template, jsonify, redirect
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/us-states')
def us_states():
	f = open("us-states.json",'r')
	us_state_json = json.loads(f.read())
	f.close()
	return jsonify(us_state_json)

@app.route('/usa-jobs')
def usa_jobs():
	f = open("usaJobs.json",'r')
	usa_jobs_json = json.loads(f.read())
	f.close()
	return jsonify(usa_jobs_json)

if __name__ == "__main__":
    app.run(debug=True)
