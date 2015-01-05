from bart_api import BartApi
from lxml import etree
import datetime
import time
from caltrain import getNextTrains

API_KEY = "ZVLK-UNSI-IYPQ-DT35"
bart = BartApi(API_KEY)

#56 mins from Berkeley to Millbrae

#Relevant stations for southbound from Berkeley to Stanford
R2M = "RICH-MLBR"
P2M = "PITT-SFIA"

#relevant station abbreviations
Berkeley = "DBRK"
Millbrea = "MLBR"

def getBartTimes():
	nextTimes = getBartMins()
	finalTimes = []
	curr = datetime.datetime.now()
	for t in nextTimes:
		if(t == "Leaving"):
			t = 0
		mn = int(t) * 60
		delt = curr + datetime.timedelta(0,mn)
		finalTimes += [delt.strftime("%H:%M")]
	
	lastTimes = []
	for t in finalTimes:
		d = datetime.datetime.strptime(t,"%H:%M")
		n = datetime.datetime.strftime(d,"%I:%M")
		lastTimes += [n]
	return lastTimes


def getBartMins():
	dep1 = bart.etd(station=Berkeley,direction="s")
	nextTimes = []
	for item in dep1:
		dest = item.find("destination").text
		if dest == "Millbrae":
			for thing in item:
				if(thing.tag == "estimate"):
					mins = thing.find("minutes").text
					nextTimes += [mins]
	return nextTimes

def calTrain():
	leavingMins = getBartMins()
	current = datetime.datetime.now()

	nextDates = []
	for mins in leavingMins:
		if(mins == "Leaving"):
			mins = 0
		seconds = 60 * int(mins)
		timeToMillBrae = 60 * 56
		nxt = current + datetime.timedelta(0,seconds + timeToMillBrae)
		nextDates += [nxt]

	#calculate the next 3 times arriving from Millbrae
	nextTimes = []
	for val in nextDates:
		t = str(val).split(" ")[1]
		nTime = t.split(":")

		hr = nTime[0]
		mn = nTime[1]

		finalTime = hr + ":" + mn
		nextTimes += [finalTime]

	trains = getNextTrains(nextTimes)
	finalTimes = []
	for train in trains:
		newtime = train.strftime("%H:%M")
		finalTimes += [newtime]

	lastTimes = []
	for t in finalTimes:
		d = datetime.datetime.strptime(t,"%H:%M")
		n = datetime.datetime.strftime(d,"%I:%M")
		lastTimes += [n]
	return lastTimes
