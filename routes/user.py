from fastapi import APIRouter, Response
from config.db import mongod
from schemas.user import userEntity, usersEntity
from models.user import USER
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


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
    userEntity(mongod.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)