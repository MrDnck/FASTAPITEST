def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(items) -> list:
    return [userEntity(i) for i in items]