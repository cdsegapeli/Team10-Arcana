from flask import jsonify
from bson import ObjectId
import json
import os
import shutil
import application.databaseInterface as dbi

db = dbi.DatabaseInterface()

# Project Manager:
# Read the json file and conver to a dictionary (like a hashmap)
# call the database manager and save it to the database
# Knows project directory from docker???
# Load project manager
class ProjectManager:
    currentProject = ''

    def __init__(self, id):
        self.currentProject = id
        return
    
    def importProject(self, jsonFile):
        try:
            filepath = os.path.join('application/json/', jsonFile)
            with open(filepath, 'r') as file:
                # Load JSON data from the uploaded file
                projectData = json.load(file)

                # Extract events directly from project_data
                events = projectData.get('events', [])
                del projectData['events']

                # Insert project data into the Projects collection
                projectID = db.createProject(projectData)

                # Insert events into the Events collection with the associated project_id
                eventIDs = db.importEvents(projectID, events)
                self.clearFiles('application/json')

                return jsonify({
                    'success': True,
                    'project_id': projectID,
                    'inserted_event_ids': eventIDs
                })

        except json.JSONDecodeError:
            print("json error")
        except Exception as e:
            print(f'{e}')

    def exportProject(self, projectID):
        project = db.getProjectInfo(projectID)
        del project['_id']
        events = list(db.getEvents(projectID))
        project['events'] = events
        return project

    def clearFiles(self, directory):
        toRemove = os.listdir(directory)
        for dir in toRemove:
            filepath = os.path.join(directory, dir)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
            except Exception as e:
                print(f'Unable to delete {filepath}: {e}')
    