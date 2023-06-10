from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from app import db_users
from bson.objectid import ObjectId

@app.route('/')
@app.route('/index')
def index():
    return flask.jsonify(json.loads(json_util.dumps(db.livros.find({}).sort("_id", 1))))

@app.route('/create', methods=['POST'])
def create():
    json_data = request.json
    if json_data is not None:
        db.livros.insert_one(json_data)
        return jsonify(mensagem='Recipe was created sucessfully')
    else:
        return jsonify(mensagem='Recipe was not created sucessfully')

@app.route('/createUser', methods=['POST'])
def createUser():
    json_data = request.json
    if json_data is not None:
        db_users.users.insert_one(json_data)
        return jsonify(mensagem='User was created sucessfully')
    else:
        return jsonify(mensagem='User was not created sucessfully')

@app.route('/listUsers')
def listUsers():
    return flask.jsonify(json.loads(json_util.dumps(db_users.users.find({}))))

@app.route("/getid/<string:userId>")
def getid(userId):
    livros = db.livros.find_one({"_id": ObjectId(userId)})
    return flask.jsonify(json.loads(json_util.dumps(livros)))

@app.route("/delete/<string:userId>")
def delete(userId):
    result = db.livros.delete_one({"_id": ObjectId(userId)})
    if(result.deleted_count > 0):
        return jsonify(mensagem='Recipe was deleted sucessfully')
    else:
        return jsonify(mensagem='Recipe was not deleted sucessfully')

@app.route('/update', methods=['POST'])
def update():
    json_data = request.json
    if json_data is not None and db.livros.find_one({"_id": ObjectId(json_data["id"])}) is not None:
        db.livros.update_one({'_id': ObjectId(json_data["id"])}, {"$set": {'title': json_data["title"], 'autor': json_data["autor"],'ingredients': json_data["ingredients"],'how': json_data["how"],'image': json_data["image"],'time': json_data["time"]}})
        return jsonify(mensagem='Recipe was updated sucessfully')
    else:
        return jsonify(mensagem='Recipe was not updated sucessfully')
