from fastapi import APIRouter, Response, Request
from fastapi.responses import JSONResponse

#mongodb
from config.db import mongod
from bson import ObjectId
from config.db import CollectUser, CollectDocuments, CollectPlans

#models
from models.user import USER, USERCREATE
from starlette.status import HTTP_204_NO_CONTENT

#others
import uuid
import requests
import datetime



#modules customs
from modules.tool import vMail, CurrentTimeForIp
from modules.validate import *


doc = APIRouter()

@doc.post("/createdoc")
def createDocument(user: dict, request: Request):
    Userdata = {
        "uuid_user": "21b38fbcdfc447bf8856d733188d1b87",
        "uuid_doc": str(uuid.uuid4()).replace("-",""),
        "Timedata": "2022/11/15",
        "suscription": "free",
        "typeDoc": "normal"
    }
    #request.scope["server"][0]
    Userdata["uuid_user"]
    #CollectDocuments.insert_one(Userdata)
    Userinfo = dict(CollectUser.find_one({"uuid_user": Userdata["uuid_user"]}))
    longUserInfo = len(Userinfo["docsCreate"])
    PlanInfo = CollectPlans.find_one({"name": Userdata["suscription"]})
    try:
        hola = "longDoc" in PlanInfo["permission"]
        print(hola)
        return longUserInfo
    except:
        return