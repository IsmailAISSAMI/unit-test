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
            'message': 'The request to get data has succeeded.',
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
        updatedData=json.loads(request.data)
        UserCollection.find_one_and_update({"_id":ObjectId(id)}, {"$set" : updatedData}, upsert = False )
            
        return jsonify({
            'status': 'ok',
            'message': 'The user was created succsseffly.',
            'data': str(newUser)
        })
         

    def delete(self, id):
        return {
            'status': 'ok',
            'message': 'The user was deleted successfully.',
            'data': [id]
        }


api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
	app.run(debug=True)