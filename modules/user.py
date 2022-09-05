
import re
import datetime
from modules.db import users, plans
from bson import ObjectId


def countDay(year: int, month: int, day: int):
    return



class toolsUser:
    def __init__(self, oId : str, uuidUser: str):
        self.oId = oId
        self.uuidUser = uuidUser
        self.usuario = users.find_one({"_id": ObjectId(self.oId), "uuid_user": self.uuidUser})
        u = self.usuario
        if u.get("suscription") == "free" or u.get("expireSuscription") == None:
            pass
        elif u.get("expireSuscription"):
            pass
            print("a")
    def setMasterKey(self, masterKey: str):
        users.update_one({"_id": ObjectId(self.oId), "uuid_user": self.uuidUser}, {"$set": {"masterkey": masterKey}})
    def checkAutorization(self, masterKey: str):
        usuario = self.usuario
        if masterKey == usuario.get("masterkey"):
            return True
        elif masterKey != usuario.get("masterkey") or usuario.get("masterkey") == None:
            return False
    def updateInformation(self):
        infoUser = users.find_one({"_id": ObjectId(self.oId), "uuid_user": self.uuidUser})
        return
    


usuario = toolsUser("62e499bec43c3bda20525d9e", "9985d7d61da1429aa1e9c983df62b980")

#print(type(usuario.usuario))
#print(usuario.checkAutorization("76748444"))

#print(usuario.userInfo())

#users.update_one({"_id": ObjectId("62d4b234f298e013a3c98f6d")}, {"$inc": {"test": 1}})



