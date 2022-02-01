import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb://renatamoon:264500@clusterlearning-shard-00-00.b6jyp.mongodb.net:27017,clusterlearning"
                      "-shard-00-01.b6jyp.mongodb.net:27017,clusterlearning-shard-00-02.b6jyp.mongodb.net:27017/myFirst"
                      "Database?ssl=true&replicaSet=atlas-z3vvyr-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["ClusterLearning"]
collection = db["frutas"]

#post = {"_id": 0, "nome": "banana", "quantidade": 50}
post_1 = {"_id": 5, "nome": "abacaxi", "quantidade": 20}
post_2 = {"_id": 6, "nome": "kiwi", "quantidade": 10}

#collection.insert_one(post) - inserting the post banana in the database
#collection.insert_many([post_1, post_2]) - adding the post1 and post2 to the database cluster

#here we're going to do queries to find on the database

results = collection.find({"nome" : "abacaxi"})
print("THE RESULT FOR THE QUERY FIND IS ", results) #- resultado: <pymongo.cursor.Cursor object at 0x7faa2496d430>

print("=-"*20)

for result in results:
    print("THE RESULT FOR THIS QUERY IS ", result["_id"]) #print will be: 5 results

print("=-"*20)

results = collection.find_one({"_id": 0})
print("THE RESULT FOR THE QUERY FIND_ONE IS ", results) #this will print: {'_id': 0, 'nome': 'banana', 'quantidade': 50}

print("=-"*20)

results = collection.update_one({"_id": 5}, {"$set" : {"nome": "abacaxi"}})
print("THE RESULT FOR THE QUERY UPDATE_ONE IS ", results) #<pymongo.results.UpdateResult object at 0x7f34e977cc40>

print("=-"*20)

post_count = collection.count_documents({})
print("THE AMOUNT OF DOCUMENTS ARE ", post_count) #RESULT ARE 3
