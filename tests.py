import unittest
import requests
import json
from bson.objectid import ObjectId
from users import usersData
from database import UsersCollection


class TestUser(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:5000/users/'
        self.firstUser = '627d15bbf51252ebe7d18927'     # usersData[0]
        self.secondUser = '627d15bef51252ebe7d18929'    # usersData[1]
        self.newUser = usersData[2]
        self.updateUser = usersData[3]

    def test_get(self):
        response = requests.get(url=self.url+self.firstUser)
        body = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['status'], 'ok')
        self.assertEqual(usersData[0], UsersCollection.find_one(usersData[0], {'_id': 0}))

    def test_post(self):
        response = requests.post(url=self.url+self.firstUser, json=self.newUser)
        body = json.loads(response.text)
        print(body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['status'], 'ok')
        self.assertEqual(self.newUser, UsersCollection.find_one(self.newUser, {'_id': 0}))

    def test_put(self):
        updatedData = {
            "name": "Test test",
            "username": "Test",
            "email": "Test@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }
        response = requests.put(url=self.url+self.firstUser, json=updatedData)
        self.assertEqual(response.status_code, 200)
        newData = UsersCollection.find_one({"_id": ObjectId(self.firstUser)}, {'_id': 0})
        self.assertEqual(newData, updatedData)


    def test_delete(self):
        response = requests.delete(url=self.url+self.secondUser)
        body = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['status'], 'ok')
