from application import app, mongo
from flask import jsonify, render_template, request, url_for, redirect, flash, session
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import cross_origin
import datetime
import json
import requests #send request to another ip
from application.generateGraph import sortEvents
import application.databaseInterface as dbi
import application.projectManager as pm
import application.logIngestor as li

db = dbi.DatabaseInterface()
projectManager = pm.ProjectManager('')
logIngestor = li.LogIngestor()

@app.route("/view-projects", methods=['GET'])
@cross_origin()
def index():
    projects = db.getAllProjects()
    return json.loads(dumps(projects))

# Open a project
@app.route("/open-project", methods=['POST'])
@cross_origin()
def openProject():
    if request.method == "POST":
        projectManager.currentProject = request.json['ID']['$oid']
        db.updateProjectDate(projectManager.currentProject)
    return 'updated tracked project'

# Create a project
@app.route("/create-project", methods=['POST'])
@cross_origin()
def createProject():
    if request.method == "POST":
        today = datetime.datetime.now()
        newDate = datetime.datetime.strftime(today, "%m/%d/%Y")
        newTime = datetime.datetime.strftime(today, "%H:%M")
        try:
            id = db.createProject({'name': request.json['Name'],
                                                    'analyst': request.json['Analyst'],
                                                    'startDate': newDate,
                                                    'startTime': newTime,
                                                    'endDate': newDate,
                                                    'endTime': newTime})
            events = logIngestor.ingestLogs()
            db.addEvents(events, id)
            projectManager.currentProject = id
            return 'Create Project'
        except:
            print('Unable to create project')
            return 'Unable to create project'
        
@app.route('/upload-file', methods=['POST', 'GET'])
@cross_origin()
def getZipFile():
    if request.method == 'POST':
        file = request.files['LogsFile']
        file.save('application/zip/'+file.filename)
        logIngestor.filename = file.filename
    return 'file uploaded successful'

@app.route('/upload-additional-logs', methods=['POST'])
@cross_origin()
def getLogsFile():
    if request.method == 'POST':
        try:
            file = request.files['LogsFile']
            file.save('application/zip/'+file.filename)
            logIngestor.filename = file.filename
            events = logIngestor.ingestLogs()
            db.addEvents(events, projectManager.currentProject)
        except Exception as e:
            print(f"Error in parsing logs: {e}")
    return 'file uploaded successful'

# Update a project
@app.route("/update-project", methods=['POST'])
@cross_origin()
def updateProject():
    if request.method == 'POST':
        id = request.json['ID']['$oid']
        try:
            project = {'name':request.json['Name'],
                        'analyst': request.json['Analyst']}
            db.updateProject(id, project)
            return 'Project updated'
        except:
            print('Unable to update project.')
    
    return redirect(url_for('index'))

# Delete a project from the database
@app.route("/delete-project", methods=['POST'])
@cross_origin()
def deleteProject():
    if request.method == 'POST':
        id = request.json['ID']['$oid']
        try:
            db.deleteProject(id)
            print("Successfully deleted project")
        except:
            print(f'Unable to delete Project {id}')
    return 'Project Deleted'

# View all events stored in the database
@app.route("/view-events")
@cross_origin()
def viewEvents():
    try:
        events = db.getEvents(projectManager.currentProject)
    except:
        print('unable to retrieve events')
    return json.loads(dumps(events))

# Create a new Event
@app.route("/create-event", methods=['GET', 'POST'])
@cross_origin()
def createEvent():
    if request.method == 'POST':
        today = datetime.datetime.now()
        newDate = datetime.datetime.strftime(today, "%m/%d/%Y")
        newTime = datetime.datetime.strftime(today, "%H:%M")
        try:
            posture = ''
            if request.json['Posture']:
                posture = request.json['Posture']
            event = {'date':request.json['Date'],
                    'time':request.json['Time'],
                    'description': request.json['Description'],
                    'team': request.json['Team'],
                    'posture': posture,
                    'vectorID': request.json['VectorID'],
                    'sourceIP': request.json['SourceIP'],
                    'targetIP': request.json['TargetIP'],
                    'analyst': request.json['Analyst'],
                    'location': request.json['Location'],
                    'lastModifiedDate': newDate,
                    'lastModifiedTime': newTime}
            db.createEvent(projectManager.currentProject, event)
            return 'Event Created.'
        except Exception as e:
            print(f'Unable to create event: {e}')
    return 'Event not created.'

# Update the event from editEvent
@app.route("/update-event", methods=['GET', 'POST'])
@cross_origin()
def updateEvent():
    if request.method == 'POST':
        id = request.json['ID']['$oid']
        try:
            event = {'date':request.json['Date'],
                    'time':request.json['Time'],
                    'description': request.json['Description'],
                    'team': request.json['Team'],
                    'posture': request.json['Posture'],
                    'vectorID': request.json['VectorID'],
                    'sourceIP': request.json['SourceIP'],
                    'targetIP': request.json['TargetIP'],
                    'analyst': request.json['Analyst'],
                    'location': request.json['Location']}
            db.updateEvent(id, event)
        except:
            print('Unable to update event.')
    
    return 'Updated Event'

# Delete an event
@app.route("/delete-event", methods=['GET', 'POST'])
@cross_origin()
def deleteEvent():
    if request.method == 'POST':
        id = request.json['ID']['$oid']
        try:
            db.deleteEvent(id)
            print("Successfully deleted event")
        except:
            print('Unable to find Event')
    return 'Deleted Event'

@app.route('/view-toas')
@cross_origin()
def viewToas():
    toas = db.getBaseToas()
    return json.loads(dumps(toas))

@app.route('/view-custom-toas')
@cross_origin()
def viewCustomToas():
    toas = db.getCustToas(projectManager.currentProject)
    return json.loads(dumps(toas))

@app.route('/create-base-toa', methods=['POST'])
@cross_origin()
def createBaseToa():
    if request.method == 'POST':
        if request.json['IconFilename'] == '':
            filename = ''
        else:
            dir = request.json['IconFilename'].split("/")
            filename = dir[-1]
        toa = {'team': request.json['Team'],
               'actionName': request.json['ActionName'],
               'iconFilename': filename}
        db.createBaseToa(toa)
    return 'Created Base TOA'

@app.route('/create-custom-toa', methods=['POST'])
@cross_origin()
def createCustomToa():
    if request.method == 'POST':
        if request.json['IconFilename'] == '':
            filename = ''
        else:
            dir = request.json['IconFilename'].split("/")
            filename = dir[-1]
        toa = {'projectID': ObjectId(projectManager.currentProject),
               'team': request.json['Team'],
               'actionName': request.json['ActionName'],
               'iconFilename': filename}
        db.createCustToa(toa)
    return 'Created Custom TOA'

@app.route('/update-base-toa', methods=['POST'])
@cross_origin()
def updateBaseToa():
    if request.method == 'POST':
        if request.json['IconFilename'] == '':
            filename = ''
        else:
            dir = request.json['IconFilename'].split("/")
            filename = dir[-1]
        toa = {'team': request.json['Team'],
               'actionName': request.json['ActionName'],
               'iconFilename': filename}
        db.updateToa(request.json['ID']['$oid'], toa)
    return 'Updated Base TOA'

@app.route('/update-custom-toa', methods=['POST'])
@cross_origin()
def updateCustToa():
    if request.method == 'POST':
        if request.json['IconFilename'] == '':
            filename = ''
        else:
            dir = request.json['IconFilename'].split("/")
            filename = dir[-1]
        toa = {'team': request.json['Team'],
               'actionName': request.json['ActionName'],
               'iconFilename': filename}
        db.updateCustToa(request.json['ID']['$oid'], toa)
    return 'Updated Custom TOA'

@app.route('/delete-base-toa', methods=['POST'])
@cross_origin()
def deleteBaseToa():
    if request.method == 'POST':
        db.deleteToa(request.json['ID']['$oid'])
    return 'Deleted Custom TOA'

@app.route('/delete-custom-toa', methods=['POST'])
@cross_origin()
def deleteCustToa():
    if request.method == 'POST':
        db.deleteCustToa(request.json['ID']['$oid'])
    return 'Deleted Custom TOA'

@app.route('/sort-events')
@cross_origin()
def getSortedEvents():
    events = sortEvents(projectManager.currentProject)
    print(events)
    return json.loads(dumps(events))

@app.route('/view-deleted-events')
@cross_origin()
def viewDeletedEvents():
    deletedEvents = db.getDeletedEvents(projectManager.currentProject)
    return json.loads(dumps(deletedEvents))

@app.route('/recover-event', methods=['POST'])
@cross_origin()
def recoverEvent():
    if request.method == 'POST':
        id = request.json['ID']['$oid']
        db.recoverDeletedEvent(id)
    return 'Recover successful'

@app.route('/view-user-activity-logs')
@cross_origin()
def viewUserActivityLogs():
    logs = db.getUserActivityLogs()
    return json.loads(dumps(logs))
    
#this function sends data to another ip 
def send_data_to_ip(ip_address, data):
    url = f'http://{ip_address}/path-to-receiving-endpoint'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code, response.json()

#format your data retrieval routes to return JSON files specifically
# structured as project.json and events.json

# Assuming this is the format needed, adjust as necessary
@app.route("/get-projects-json", methods=['GET'])
def get_projects_json():
    projects = mongo.db.Projects.find()
    return jsonify(json.loads(dumps(projects)))

@app.route("/get-events-json", methods=['GET'])
def get_events_json():
    events = mongo.db.Events.find()
    return jsonify(json.loads(dumps(events)))


#Takes the destination IP address as input (from Angular frontend).
#Retrieves the necessary data from MongoDB.
#Calls the send_data_to_ip function to send this data to the specified IP.
@app.route("/sync", methods=['POST'])
def sync():
    ip_address = request.form.get('ipAddress')  # Ensure this matches your form's input name
    # Retrieve project and events data
    projects = json.loads(dumps(mongo.db.Projects.find()))
    events = json.loads(dumps(mongo.db.Events.find()))
    # Assuming you want to send both in a single request
    data = {'projects': projects, 'events': events}
    status_code, response = send_data_to_ip(ip_address, data)
    if status_code == 200:
        return jsonify({'status': 'success', 'message': 'Data sent successfully'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Failed to send data'}), status_code
      
# Route to handle uploading and saving project data from a JSON file
@app.route("/upload-project", methods=['POST'])
@cross_origin()
def uploadProject():
    try:
        if request.method == 'POST':
            # Check if a JSON file was uploaded
            if 'ProjectFile' not in request.files:
                return jsonify({'error': 'No file part'}), 400

            file = request.files['ProjectFile']

            # Check if no file was selected
            if file.filename == '':
                return jsonify({'error': 'No selected file'}), 400

            # Check if the file is a JSON file
            if file and file.filename.endswith('.json'):
                file.save('application/json/'+file.filename)
                projectManager.importProject(file.filename)

                return 'result'
    except Exception as e:
        print(f'{e}')
        
@app.route('/export-project', methods=['GET'])
@cross_origin()
def exportProject():
    if request.method == 'GET':
        project = projectManager.exportProject(projectManager.currentProject)
        return json.loads(dumps(project))
    return 'Export failed'