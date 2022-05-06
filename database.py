import pymongo 
from pymongo import MongoClient

# config
db_uri = 'mongodb+srv://admin:5kVbEzQNzHYI4Bw7@cluster0.nlqon.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(db_uri)

# collections
db = client["Cluster0"]
UserCollection = db["Users"]

# # find all
# for x in UserCollection.find():
#   print(x)
