from config import Config
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

mongodb_client = PyMongo(app, uri="mongodb+srv://progAvan:progAvan@cluster0.k87m7.mongodb.net/livros")
db = mongodb_client.db

mongodb_client2 = PyMongo(app, uri="mongodb+srv://progAvan:progAvan@cluster0.k87m7.mongodb.net/users")
db_users = mongodb_client2.db

from app import routes
