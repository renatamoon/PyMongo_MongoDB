from pymongo import MongoClient
from datetime import datetime


# connection string gotten by Mongo Atlas
connection_string = \
    "mongodb+srv://renatamoon:xxxxx@clusterlearning.b6jyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# passing it to a variable
client = MongoClient(connection_string)

# getting the database from MongoAtlas
database = client['new_database']

# getting the collection from MongoAtlas
collection = database['todo']


# ------ here im entering my code

todo1 = {   "name": "Patrick", 
            "text": "My first todo", 
            "status": "open",
            "tags": ["python", "coding"],
            "date": str(datetime.datetime.utcnow())
            }

todos = database.todo

result = todos.insert_one(todo1)