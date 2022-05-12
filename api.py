#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from database import UserCollection
from bson.objectid import ObjectId
import json

app = Flask(__name__)
api = Api(app)

class User(Resource):

    def get(self, id):
        user = UserCollection.find_one({"_id": ObjectId(id)})
        return jsonify({
            'status': 'ok',
            'message': 'The request to get the user with the following id = ['+str(id)+'] was succeeded.',
            'data': str(user)
        })

    def post(self, id):
        if request.method == 'POST':
            newUser=json.loads(request.data)
            UserCollection.insert_one(newUser)
            return jsonify({
                'status': 'ok',
                'message': 'The user was created succsseffly.',
                'data': str(newUser)
            })
        else: 
            return jsonify({
                'status': 'bad request',
                'message': 'You need to insert user data.',
                'data': []
            }) 

    def put(self, id):
        if request.method == "PUT":
            user = json.loads(request.data)
            UserCollection.find_one_and_update({"_id":ObjectId(id)}, {"$set" : user}, upsert = True)
            return {
                'status': 'ok',
                'message': 'The user with the id = ['+str(id)+'] was modified successfly.',
                'data': user
            }
        else: 
            return {
                'status': '403',
                'message': 'Bad request.',
                'data': []
            }
         

    def delete(self, id):
        if request.method == "DELETE":
            UserCollection.delete_one({"_id":ObjectId(id)})
            return {
                'status': 'ok',
                'message': 'The user with the id = ['+str(id)+'] was deleted successfly.',
                'data': []
            }
        else: 
            return {
                'status': '403',
                'message': 'Bad request.',
                'data': []
            }


api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
	app.run(debug=True)