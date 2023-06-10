from config import Config
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

mongodb_client = PyMongo(app, uri="yourFirstStringHere")
db = mongodb_client.db

mongodb_client2 = PyMongo(app, uri="yourSecondStringHere")
db_users = mongodb_client2.db

from app import routes
