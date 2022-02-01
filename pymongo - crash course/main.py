from pymongo import MongoClient

# connection string gotten by Mongo Atlas
connection_string = \
    "mongodb+srv://renatamoon:264500@clusterlearning.b6jyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# passing it to a variable
client = MongoClient(connection_string)

# getting the database from MongoAtlas
database = client['new_database']

# getting the collection from MongoAtlas
collection = database['contato']