from fastapi import FastAPI, Request
from routes.user import user


app = FastAPI()

usersss = [
    {
        "_id": "544545",
        "name": "Cristian",
        "correo": "dalamates@gmail.com",
        "password": "cristian",
    }
]


app.include_router(user)


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    print(client_host)
    if client_host == "217.148.141.46":
        return {"client_host": client_host, "item_id": item_id}
    else:
        return {"no authentication"}
    