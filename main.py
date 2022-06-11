from fastapi import FastAPI, Request

app = FastAPI()

users = [
    {
        "_id": "544545",
        "name": "Cristian",
        "correo": "dalamates@gmail.com",
        "password": "cristian",
    }
]

@app.get("/users")
def get_usuarios():
    return users

@app.post("/users")
def post_users():
    print()
    return "gracias"


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    print(client_host)
    if client_host == "217.148.141.46":
        return {"client_host": client_host, "item_id": item_id}
    else:
        return {"no authentication"}
    