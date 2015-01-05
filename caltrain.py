#!/usr/bin/env python2.5
import time
import datetime
#37 mins from Millbrae to Palo Alto

wkdaySouthAMlst = ["5:19","5:49", 
"6:29", "6:48", "7:01", "7:15", "7:32", "7:48", "8:01", "8:15", "8:32" , "8:48", "9:01",
"9:15", "9:31", "9:55", "10:31", "11:31"]

wkdaySouthPMlst = ["12:31", "13:31" ,"14:31" ,"14:55", "15:31", "15:55", "16:25", "16:56", "16:49", 
"17:14", "17:30", "17:49", "18:14", "18:30", "18:56", "18:49", "19:14",  
"19:54", "21:04", "22:04", "23:04", "00:25"]

wkendSouthAMlst = ["8:39", "9:39" ,"10:39", "11:39"]

wkendSouthPMlst = ["12:15","12:39","1:39" ,"2:39" ,"3:39" ,"4:39" ,"5:39" ,"6:39" ,"7:15" ,"7:39"  
"8:39" ,"9:39"]

weekdaySouthbound = { "am" : wkdaySouthAMlst, "pm" : wkdaySouthPMlst }

weekendSouthbound = { "am" : wkendSouthAMlst, "pm": wkendSouthPMlst }

#data coming in list of times ARRIVING at millbrae
def getNextTrains(times):
  trainTimes = []
  for item in times:
    hr = int(item.split(":")[0])
    mn = int(item.split(":")[1])
    #use wkdaySouthPM for now, modify later
    timeTrain = ''
    for t in wkdaySouthPMlst:
       hour = int(t.split(":")[0])
       minute = int(t.split(":")[1])
       millbraeDepartureTime = datetime.time(hour,minute)
       millbraeArrivalTime = datetime.time(hr,mn)
       if(millbraeArrivalTime < millbraeDepartureTime):
          timeTrain = millbraeDepartureTime
          break
    trainTimes += [timeTrain]

  return trainTimes
       