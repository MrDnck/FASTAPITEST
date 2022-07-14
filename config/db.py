from pymongo import MongoClient
import os
from dotenv import  load_dotenv

load_dotenv()

mongod = MongoClient(os.getenv("URLMONGO"))
MDb = mongod["IAaplicacion"]


#Tablas (collections)
CollectUser = MDb["users"]
CollectDocuments = MDb["documentos"]
CollectPlans = MDb["plans"]


