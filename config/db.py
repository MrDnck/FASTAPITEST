from pymongo import MongoClient

mongod = MongoClient("mongodb://mongo:SPIdq6IRQnadduPp19wJ@containers-us-west-54.railway.app:7115")
MDb = mongod["IAaplicacion"]


#Tablas (collections)
CollectUser = MDb["users"]
CollectDocuments = MDb["documentos"]