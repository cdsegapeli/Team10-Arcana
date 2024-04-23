from application import app, mongo
import application.databaseInterface as dbi
import application.projectManager as pm
import os
import shutil
import csv
import zipfile

#TODO: have functions to clean directories
class LogIngestor:

    def __init__(self):
        self.db = dbi.DatabaseInterface()
        self.zipFileDir = 'application/zip'
        self.logDir = 'application/logs'
        self.filename = ''

    def unzipFile(self):
        with zipfile.ZipFile(self.zipFileDir+'/'+self.filename, 'r') as zipRef:
            zipRef.extractall(self.logDir)

    def parseLogs(self):
        events = []
        filesToParse = []
        for path, subdirs, files in os.walk(self.logDir):
            if len(path) > 16:
                if path[17:25] == '__MACOSX':
                    continue
            for name in files:
                if name[-4:] == '.csv':
                    filePath = os.path.join(path, name)
                    filesToParse.append(filePath)

        for file in filesToParse:
            with open(file, newline='') as logFile:
                reader = csv.reader(logFile, delimiter=',', quotechar='"')
                headers = reader.__next__()
                print(f"parsing file {file}")
                for row in reader:
                    event = dict(zip(headers, row))
                    try:
                        event['date'], event['time'] = event['dateCreated'].split(" ")
                        event['lastDate'], event['lastTime'] = event['lastModified'].split(" ")
                    except ValueError:
                        event['date'], event['time'], event['lastDate'], event['lastTime'] = '', '', '', ''
                    dataSource = file.split('/')
                    event['dataSource'] = dataSource[-1]
                    events.append(event)
        return events

    def isMalfored(self, events):
        for event in events:
            malfored = False
            for key in event.keys():
                if key == 'posture':
                    continue
                if event[key] == '':
                    malfored = True
            event['isMalformed'] = malfored
        return events
    
    def getTeamAction(self, events):
        for event in events:
            if event['team'] == 'Blue' or event['team'] == 'White':
                event['TOA'] = 'Blue Team Activity'
            else:
                event['TOA'] = 'Red Team Activity'

    # save events to database
    def clearFiles(self):
        os.remove(self.zipFileDir+'/'+self.filename)
        toRemove = os.listdir(self.logDir)
        for dir in toRemove:
            filepath = os.path.join(self.logDir, dir)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
            except Exception as e:
                print(f'Unable to delete {filepath}: {e}')


    def ingestLogs(self):
        try:
            self.unzipFile()
            events = self.parseLogs()
            self.isMalfored(events)
            self.getTeamAction(events)
            self.clearFiles()
        except Exception as e:
            print("Exception in parsing logs:")
            print(f"{e}")
        return events