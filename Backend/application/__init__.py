from flask import Flask
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/arcana"
app.config['SECRET_KEY'] = 'Zelda'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = 'logs/'
mongo = PyMongo(app)

from application import routes