from fastapi import APIRouter, Response, Request
from config.db import mongod
from models.user import USER
from models.tool import TOOL
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


from modules.validate import *
from modules.image import getImageSearch


tool = APIRouter()

@tool.post('/getImage')
def getImage(data: TOOL):
    data = dict(data)
    string = data["string"]
    tipo = data["type"]
    dataImage = getImageSearch(string, tipo)
    print(dataImage)
    return dataImage