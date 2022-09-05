
from fastapi import APIRouter, Response, Request
from fastapi.responses import JSONResponse
from config.db import mongod
from config.db import CollectUser, CollectDocuments
from schemas.user import userEntity, usersEntity
from models.user import USER, USERCREATE, USERCHECK
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


import uuid
import requests


from modules.jwtFuncion import write_token, validate_token
from modules.passTool import createdHashPass, checkPassHash
from modules.tool import vMail, CurrentTimeForIp




user = APIRouter()


@user.post('/register')
def registerUser(user: USERCREATE, request: Request):
    userReq = dict(user)
    emailInfo = vMail(userReq["email"])
    RequestDbMail = CollectUser.find({"email": userReq["email"]})
    client_host = request.client.host
    JSONResquestIp = requests.post(f"http://ip-api.com/json/{client_host}")
    IpJson = JSONResquestIp.json()
    TimeLoad = CurrentTimeForIp(client_host)
    try:
        ListaCorreoCount = list(RequestDbMail)
        if len(ListaCorreoCount) >= 1 or emailInfo["status"] == False or userReq["password"] != userReq["replypassword"]:
            return JSONResponse(content={"success": False}, status_code=201)
        elif len(ListaCorreoCount) == 0:
            data = {
                "success": True,
                "email": userReq["email"]
            }
            #dataRegister = dict(data)
            #dataRegister["uuid_user"] = str(uuid.uuid4()).replace("-","")
            userReq["password"] = createdHashPass(userReq["password"])
            userReq["mailDomainInfo"] = emailInfo["domain"]
            userReq["uuid_user"] = str(uuid.uuid4()).replace("-","")
            userReq["suscription"] = "free"
            userReq["is_enabled"] = True
            del IpJson["status"]
            userReq["dataRegisterIp"] = IpJson
            userReq["TimeRegister"] = TimeLoad
            del userReq["replypassword"]
            CollectUser.insert_one(userReq)
            return JSONResponse(content=data, status_code=201)
        else:
            return JSONResponse(content={"success": False}, status_code=400)
    except:
        return JSONResponse(content={"success": False}, status_code=400)

@user.post("/create-token")
def checkLogin(Data: USERCHECK, request : Request):
    Data = dict(Data)
    IPclient = request.client.host
    try:
        credencials = list(CollectUser.find({"email": Data["email"]}))[0]
        promt = Data["password"]
        dbHash = credencials["password"]
        if checkPassHash(promt , dbHash) and credencials["email"] == Data["email"]:
            returnData = {
                "type": "normal",
                "idClient": str(credencials["_id"]),
                "key": credencials["uuid_user"],
                "masterkey": IPclient
            }
            token = write_token(returnData)
            return JSONResponse(content={
                "succes": True,
                "token": token
            }, status_code= 201)
        else:
            return JSONResponse(content={
                "succes": False
            }, status_code= 401)
    except:
        return JSONResponse(content={
                "succes": False
            }, status_code= 400)


@user.post("/userinfo")
def informacion(test : dict):
    test = dict(test)
    test1 = validate_token(test["token"], output= True)
    print(type(test1))
    return test1




@user.get('/users')
def todosLosUsuarios():
    return usersEntity(CollectUser.find())

@user.post('/create-user')
def crearUsuario(user: USER):
    nuevoUsuario = dict(user)
    #del nuevoUsuario["id"]
    id = CollectUser.insert_one(nuevoUsuario).inserted_id
    usuario = CollectUser.find_one({"_id": id})
    return userEntity(usuario)



@user.get('/user/{id}')
def obtenerUnUsuario(id: str):
    return userEntity(CollectUser.find_one({"_id": ObjectId(id)}))

@user.get("/userbymail")
def obtenerUsuarioPorMail(email : str):
    dato = CollectUser.find({"email": email})
    dato[0]
    return usersEntity(dato)


@user.delete('/user/{id}')
def obtenerUnUsuario(id: str):
    try:
        userEntity(CollectUser.find_one_and_delete({"_id": ObjectId(id)}))
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
    


from modules.user import toolsUser
@user.get("/test1")
def test1():
    test = toolsUser("62e499bec43c3bda20525d9e", "9985d7d61da1429aa1e9c983df62b980")
    print("Adad", test.usuario)