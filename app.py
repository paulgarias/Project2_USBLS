from flask import Flask, render_template, jsonify, redirect
from flask_restful import Resource, Api

from sqlalchemy import Column, Float, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
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

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("contact.html")

@app.route('/us-states')
def us_states():
    data = session.query(myJson.json).filter(myJson.jsonid==2).all()
    return jsonify(json.loads(data[0][0]))

@app.route('/usa-jobs')
def usa_jobs():
    data = session.query(myJson.json).filter(myJson.jsonid==1).all()
    return jsonify(json.loads(data[0][0]))

if __name__ == "__main__":
    app.run(debug=True)
