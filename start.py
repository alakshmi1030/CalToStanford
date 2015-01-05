from flask import Flask
from flask import render_template
from flask import request
from backend import getBartTimes
from backend import calTrain

app = Flask("start")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/getroutes")
def getroutes():
	nextTimes = getBartTimes()
	nextTrains = calTrain()
	return render_template("results.html",next=nextTimes,trains=nextTrains)

app.run()