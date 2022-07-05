from fastapi import APIRouter, Response, Request
from config.db import mongod
from schemas.user import userEntity, usersEntity
from models.user import USER
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


from modules.validate import *


user = APIRouter()

@user.get('/users')
def todosLosUsuarios():
    return usersEntity(mongod.local.user.find())

@user.post('/create-user')
def crearUsuario(user: USER):
    nuevoUsuario = dict(user)
    del nuevoUsuario["id"]
    id = mongod.local.user.insert_one(nuevoUsuario).inserted_id
    usuario = mongod.local.user.find_one({"_id": id})
    return userEntity(usuario)

@user.get('/user/{id}')
def obtenerUnUsuario(id: str):
    return userEntity(mongod.local.user.find_one({"_id": ObjectId(id)}))


@user.delete('/user/{id}')
def obtenerUnUsuario(id: str):
    try:
        userEntity(mongod.local.user.find_one_and_delete({"_id": ObjectId(id)}))
        return Response(status_code=HTTP_204_NO_CONTENT)
    except:
        return "no funciono"




@user.get("/item/{item_id}")
def items(item_id: str, request: Request):
    print(request)
    client_host = request.client.host
    client_port = str(request.client.port)
    print(type(client_host))
    print(type(client_port))
    ipRequest = f"{client_host}:{client_port}"
    print(ipRequest)
    if ipRequest == "128.14.65.197:0":
        return {"client_host": ipRequest, "item_id": item_id}
    else:
        return {"no authentication"}
    