from fastapi import FastAPI, Request
from routes.user import user
from routes.documents import doc
from routes.tool import tool


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
app.include_router(doc)

app.include_router(tool)

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    print(client_host)
    if client_host == "arbitpay.com":
        return {"client_host": client_host, "item_id": item_id}
    else:
        return {"no authentication"}
    