from flask import Flask, render_template, jsonify, redirect
from flask_restful import Resource, Api

from sqlalchemy import Column, Float, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import json

Base = declarative_base()

class myJson(Base):
    __tablename__ = "myjson"
    jsonid = Column(Integer, primary_key=True)
    json = Column(Text)

engine = create_engine("sqlite:///myjson.sqlite")
Base.metadata.create_all(engine)

session = Session(bind=engine)


engine_hist = create_engine("sqlite:///histJobDB.sqlite")
Base_hist = automap_base()
Base_hist.prepare(engine_hist, reflect=True)
jobsDB = Base_hist.classes.jobsDB
session_hist = Session(engine_hist)

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/us-states')
def us_states():
    data = session.query(myJson.json).filter(myJson.jsonid==2).all()
    return jsonify(json.loads(data[0][0]))

@app.route('/usa-jobs')
def usa_jobs():
    data = session.query(myJson.json).filter(myJson.jsonid==1).all()
    return jsonify(json.loads(data[0][0]))

@app.route('/alabama')
def state_jobs():
    data = session_hist.query(jobsDB.year,jobsDB.tot_emp,jobsDB.state).filter(jobsDB.state=="Texas",jobsDB.occ_title=="Aerospace Engineering and Operations Technicians").all()
    jsonitem = [{"year": item[0], "value":item[1]} for item in data]
    return jsonify(jsonitem)

if __name__ == "__main__":
    app.run(debug=True)
