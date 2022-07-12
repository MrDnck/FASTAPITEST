from fastapi import APIRouter, Response, Request
from fastapi.responses import JSONResponse

#mongodb
from config.db import mongod
from bson import ObjectId
from config.db import CollectUser, CollectDocuments

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
    uuid_user = dict(user)
    server_host = request.scope["server"][0]
    try:
        return server_host, datetime.datetime.now()
    except:
        return