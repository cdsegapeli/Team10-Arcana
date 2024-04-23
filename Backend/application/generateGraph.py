from bson import ObjectId
from application import mongo
from datetime import datetime
import application.databaseInterface as dbi

db = dbi.DatabaseInterface()

def sortByTime(events):
    normalizeTime(events)
    sorted_date = sorted(events, key=lambda x: datetime.strptime(x['date']+" "+x['time'], '%m/%d/%Y %H:%M:%S'))
    return sorted_date

def groupByVectorId(events):
    vectorGroups = {}
    for event in events:
        if event['vectorID'] in vectorGroups.keys():
            vectorGroups[event['vectorID']].append(event)
        else:
            vectorGroups[event['vectorID']] = [event]
    return vectorGroups

def normalizeTime(events):
    for event in events:
        month, day, year = event['date'].split('/')
        if len(month) < 2:
            month = '0' + month
        if len(day) < 2:
            day = '0' + day
        event['date'] = month + '/' + day + '/' + year
        if len(event['time']) < 7:
            event['time'] = event['time'] + ':00'

def sortEvents(id):
    cursorEvents = db.getEvents(id)
    events = list(cursorEvents)
    vectorGroups = groupByVectorId(events)
    for vector in vectorGroups.keys():
        vectorGroups[vector] = sortByTime(vectorGroups[vector])
    return vectorGroups

