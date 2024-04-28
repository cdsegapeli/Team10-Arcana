from application import mongo
from bson import ObjectId
import datetime


# TODO: call the User Activity logger call to each create/ edit/ delete
# TODO: add functions for retireving, saving, updating, deleting graph
class DatabaseInterface:

    def __init__(self):
        self.projectsDB = mongo.db.Projects
        self.eventsDB = mongo.db.Events
        self.deletedEventsDB = mongo.db.DeletedEvents
        self.originEventsDB = mongo.db.OriginEvents
        self.baseToaDB = mongo.db.BaseTeamActions
        self.custToaDB = mongo.db.CustomTeamActions
        self.userActivityLogDB = mongo.db.UserActivityLogs
        self.graphDB = mongo.db.EventGraph

    def logActivity(self, str):
        today = datetime.datetime.now()
        timestamp = datetime.datetime.strftime(today, "%m/%d/%Y %H:%M")
        self.userActivityLogDB.insert_one({"timestamp":timestamp,
                                        "activity":str})

    def createProject(self, project):
        try:
            id = self.projectsDB.insert_one(project)
            self.logActivity(f"Project ID - {str(id.inserted_id)}: PROJECT CREATED")
            return str(id.inserted_id)
        except:
            print("Unable to add new project to the database")
            return ''

    def getAllProjects(self):
        return self.projectsDB.find()

    def getProjectInfo(self, id):
        return self.projectsDB.find_one_or_404({'_id': ObjectId(id)})
    
    def updateProject(self, id, newProject):
        today = datetime.datetime.now()
        newDate = datetime.datetime.strftime(today, "%m/%d/%Y")
        newTime = datetime.datetime.strftime(today, "%H:%M")
        try:
            self.projectsDB.update_one(
                {'_id': ObjectId(id)},
                {'$set':
                    {'name':newProject['name'],
                     'analyst': newProject['analyst'],
                     'lastModifiedDate': newDate,
                     'lastModifiedTime': newTime}
            })
            self.logActivity(f"Project ID - {id}: PROJECT UPDATED")
        except:
            print(f"Unable to update project with id {id}")

    def updateProjectDate(self, projectID):
        today = datetime.datetime.now()
        newDate = datetime.datetime.strftime(today, "%m/%d/%Y")
        newTime = datetime.datetime.strftime(today, "%H:%M")
        try:
            self.projectsDB.update_one(
                {'_id': ObjectId(projectID)},
                {'$set':
                    {'endDate': newDate,
                     'endTime': newTime}
            })
        except:
            print(f"Unable to update project with id {id}")
    
    def deleteProject(self, id):
        try:
            self.projectsDB.delete_one({'_id': ObjectId(id)})
            self.eventsDB.delete_many({'projectID':ObjectId(id)})
            self.deletedEventsDB.delete_many({'projectID':ObjectId(id)})
            self.custToaDB.delete_many({'projectID':ObjectId(id)})
            # TODO: also call delete graph
            self.logActivity(f"Project ID - {id}: PROJECT DELETED")
        except:
            print("Unable to delete project and associated Events")

    def createEvent(self, projectID, event):
        event['projectID'] = ObjectId(projectID)
        event['dataSource'] = ''
        try:
            event = self.checkIfMalformed(event)
            event = self.checkTOA(event)
            self.eventsDB.insert_one(event)
            self.originEventsDB.insert_one(event)
            self.logActivity(f"Project ID - {projectID}: EVENT CREATED: {event}")
        except Exception as e:
            print(f"Unable to add the event to the database: {e}")

    def addEvents(self, events, projectID):
        for event in events:
            try:
                self.eventsDB.insert_one({
                    "projectID": ObjectId(projectID),
                    "date": event['date'],
                    "time": event['time'],
                    "description": event['description'],
                    "team": event['team'],
                    'posture': '',
                    "vectorID": event['vectorId'],
                    "sourceIP": event['sourceHost'],
                    "targetIP": event['targetHost'],
                    "analyst": event['initials'],
                    "location": event['location'],
                    "dataSource": event['dataSource'],
                    "isMalformed": event['isMalformed'],
                    "TOA": event['TOA'],
                    "lastModifiedDate": event['lastDate'],
                    "lastModifiedTime": event['lastTime']
                })
                self.originEventsDB.insert_one({
                    "projectID": ObjectId(projectID),
                    "date": event['date'],
                    "time": event['time'],
                    "description": event['description'],
                    "team": event['team'],
                    'posture': '',
                    "vectorID": event['vectorId'],
                    "sourceIP": event['sourceHost'],
                    "targetIP": event['targetHost'],
                    "analyst": event['initials'],
                    "location": event['location'],
                    "dataSource": event['dataSource'],
                    "isMalformed": event['isMalformed'],
                    "TOA": event['TOA'],
                    "lastModifiedDate": event['lastDate'],
                    "lastModifiedTime": event['lastTime']
                })
            except:
                print("Unable to add events to database.")
        self.logActivity(f"Project ID - {projectID}: EVENTS ADDED: {events}")

    def importEvents(self, projectID, events):
        importedIDs = []
        for event in events:
            event['projectID'] = ObjectId(projectID)
            event = self.checkIfMalformed(event)
            event = self.checkTOA(event)
            try:
                # Here check if isMalformed and TOA is set
                self.eventsDB.insert_one(event)
                self.originEventsDB.insert_one(event)
                self.logActivity(f"Project ID - {projectID}: EVENTS IMPORTED: {events}")
            except Exception as e:
                print(f"Unable to import events: {e}")
        return importedIDs
    
    def getEvents(self, id):
        return self.eventsDB.find({"projectID":ObjectId(id)})
    
    def getEventInfo(self, id):
        return self.eventsDB.find_one_or_404({'_id':ObjectId(id)})
    
    def updateEvent(self, id, newEvent):
        today = datetime.datetime.now()
        newDate = datetime.datetime.strftime(today, "%m/%d/%Y")
        newTime = datetime.datetime.strftime(today, "%H:%M")
        try:
            newEvent = self.checkIfMalformed(newEvent)
            self.eventsDB.update_one(
                {'_id': ObjectId(id)},
                {'$set':
                    {'date':newEvent['date'],
                    'time':newEvent['time'],
                    'description': newEvent['description'],
                    'team': newEvent['team'],
                    'posture': newEvent['posture'],
                    'vectorID': newEvent['vectorID'],
                    'sourceIP': newEvent['sourceIP'],
                    'targetIP': newEvent['targetIP'],
                    'analyst': newEvent['analyst'],
                    'location': newEvent['location'],
                    'dataSource': '',
                    'isMalformed': newEvent['isMalformed'],
                    'lastModifiedDate': newDate,
                    'lastModifiedTime': newTime}
            })
            self.logActivity(f"EVENT ID - {id}: EVENT UPDATED")
        except Exception as e:
            print(f"Unable to update event with id {id}: {e}")

    def deleteEvent(self, id):
        try:
            deletedEvent = self.eventsDB.find({'_id': ObjectId(id)})
            self.deletedEventsDB.insert_one(deletedEvent[0])
            self.eventsDB.delete_one({'_id': ObjectId(id)})
            self.logActivity(f"EVENT ID - {id}: EVENT DELETED")
        except Exception as e:
            print(f"Unable to delete event with id {id}: {e}")

    def getDeletedEvents(self, id):
        return self.deletedEventsDB.find({"projectID":ObjectId(id)})

    def recoverDeletedEvent(self, id):
        try:
            event = self.deletedEventsDB.find({'_id': ObjectId(id)})
            self.eventsDB.insert_one(event[0])
            self.deletedEventsDB.delete_one({'_id': ObjectId(id)})
        except:
            print("Unable to recover deleted event.")

    # Functions for Team Oriented Actions
    def createCustToa(self, toa):
        try:
            self.custToaDB.insert_one(toa)
            self.logActivity(f"Project ID - {toa['projectID']}: TOA CREATED: {toa}")
        except:
            print('Unable add TOA to database.')
    
    def createBaseToa(self, toa):
        try:
            self.baseToaDB.insert_one(toa)
            self.logActivity(f"TOA CREATED: {toa}")
        except:
            print('Unable add TOA to database.')

    def getBaseToas(self):
        try:
            return self.baseToaDB.find()
        except:
            print("Unable to retrieve default team oriented actions.")
            return []
        
    def updateToa(self, id, toa):
        try:
            if toa['iconFilename'] == '':
                self.baseToaDB.update_one(
                {'_id': ObjectId(id)},
                {'$set':
                    {'team': toa['team'],
                     'actionName': toa['actionName'],}
                })
            else:
                self.baseToaDB.update_one(
                    {'_id': ObjectId(id)},
                    {'$set':
                        {'team': toa['team'],
                        'actionName': toa['actionName'],
                        'iconFilename': toa['iconFilename']}
                })
            self.logActivity(f"TOA UPDATED: {toa}")
        except:
            print("Unable to update TOA")

    def deleteToa(self, id):
        try:
            self.baseToaDB.delete_one({'_id': ObjectId(id)})
            self.logActivity(f"TOA DELETED: {id}")
        except:
            print("Unable to delete TOA from database")

    def getCustToas(self, projectID):
        try:
            return self.custToaDB.find({'projectID': ObjectId(projectID)})
        except Exception as e:
            print(f"Unable to retrieve custom team oriented actions: {e}")
            return []

    def getToaInfo(self, id):
        try:
            toa = self.custToaDB.find({'_id': ObjectId(id)})
            return toa
        except:
            print("Unable to retrieve TOA from database.")

    def updateCustToa(self, id, toa):
        try:
            if toa['iconFilename'] == '':
                self.custToaDB.update_one(
                {'_id': ObjectId(id)},
                {'$set':
                    {'team': toa['team'],
                     'actionName': toa['actionName'],}
                })
            else:
                self.custToaDB.update_one(
                    {'_id': ObjectId(id)},
                    {'$set':
                        {'team': toa['team'],
                        'actionName': toa['actionName'],
                        'iconFilename': toa['iconFilename']}
                })
            self.logActivity(f"Project ID - {id}: TOA UPDATED: {toa}")
        except Exception as e:
            print(f"Unable to update TOA: {e}")

    def deleteCustToa(self, id):
        try:
            self.custToaDB.delete_one({'_id': ObjectId(id)})
            self.logActivity(f"TOA DELETED: {id}")
        except:
            print("Unable to delete TOA from database")
    
    # functions for UserActivityLogs
    def getUserActivityLogs(self):
        return self.userActivityLogDB.find()     
    
    def checkIfMalformed(self, event):
        malformed = False
        for key in event.keys():
            if key == 'posture':
                continue
            elif event[key] == '':
                malformed = True
        event['isMalformed'] = malformed
        return event
    
    def checkTOA(self, event):
        if event['team'] == 'Blue' or event['team'] == 'White':
            event['TOA'] = 'Blue Team Activity'
        else:
            event['TOA'] = 'Red Team Activity'
        return event

    def getGraph(self, projectID):
        try:
            return self.graphDB.find({'projectID': ObjectId(projectID)})
        except Exception as e:
            print(f'Unable to find graph for project {projectID}: {e}')
            return False

    def saveGraph(self, projectID, graph):
        graph['projectID'] = ObjectId(projectID)
        try:
            self.graphDB.delete_one(ObjectId(projectID))
            self.graphDB.insert_one(graph)
        except Exception as e:
            print(f'Unable to update graph: {e}')
