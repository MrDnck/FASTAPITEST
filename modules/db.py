from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


#mongo db conected
dbmongo = MongoClient(os.getenv("URLMONGO"))
MDb = dbmongo["IAaplicacion"]


#Tablas (collections)
users = MDb["users"]
plans = MDb["plans"]

docsJust = MDb["documentos"]

