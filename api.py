#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from database import UsersCollection
from bson.objectid import ObjectId
import json

app = Flask(__name__)
api = Api(app)


class User(Resource):

    def get(self, id):
        founded = UsersCollection.find_one({"_id": ObjectId(id)})
        return jsonify({'status': 'ok', 'message': 'The user '+str(id)+' was successfully found', 'data': str(founded)})

    def post(self, id):
        if request.method == 'POST':
            new_user = json.loads(request.data)
            UsersCollection.insert_one(new_user)
            return jsonify({'status': 'ok', 'message': 'The user was created successfully.', 'data': str(new_user)})
        else:
            return jsonify({'status': 'bad request', 'message': 'Use POST methode.', 'data': 'None'})

    def put(self, id):
        if request.method == "PUT":
            user = json.loads(request.data)
            UsersCollection.find_one_and_update({"_id": ObjectId(id)}, {"$set": user}, upsert=True)
            return jsonify({'status': 'ok', 'message': 'The user with the id = ['+str(id)+'] was modified successfly.', 'data': user})
        else:
            return jsonify({'status': 'Bad request', 'message': 'Use PUT methode.', 'data': 'None'})

    def delete(self, id):
        if request.method == "DELETE":
            UsersCollection.delete_one({"_id": ObjectId(id)})
            return jsonify({'status': 'ok', 'message': 'The user with the id = ['+str(id)+'] was deleted successfly.', 'data': []})
        else:
            return jsonify({'status': 'Bad request', 'message': 'Use DELETE methode.', 'data': 'None'})


api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)
