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
    vectorGroups = {'isMalformed':[]}
    for event in events:
        # if 'isMalformed' in event.keys():
        if event['isMalformed']:
            vectorGroups['isMalformed'].append(event)
        elif event['vectorID'] in vectorGroups.keys():
            vectorGroups[event['vectorID']].append(event)
        else:
            vectorGroups[event['vectorID']] = [event]
    return vectorGroups

def normalizeTime(events):
    for event in events:
        month, day, year = event['date'].split('/')
        if len(year) == 2:
            year = '20' + year
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
        if vector == 'isMalformed':
            continue
        vectorGroups[vector] = sortByTime(vectorGroups[vector])
    # set the Head_ID to the previous node and save it to database
    for event in vectorGroups['isMalformed']:
        event['nodeID'] = None
        event['parentID'] = None

    id = 1 
    events = []
    vectors = list(vectorGroups.keys())
    vectors.remove('isMalformed')
    for vector in vectors:
        #may need to change to undefined
        previousID = None
        for event in vectorGroups[vector]:
            event['nodeID'] = id
            event['parentID'] = previousID
            previousID = id
            id += 1
        events = events + vectorGroups[vector]
    events = events + vectorGroups['isMalformed']

    for event in events:
        event['displayInfo'] = f"Vector ID: {event['vectorID']}\nTeam: {event['team']}\nTime: {event['date']} {event['time']}\n\n{event['description']}"
    return events

