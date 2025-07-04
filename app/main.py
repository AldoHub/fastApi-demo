from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

#import the routers
from app.routers import products_mongo, users, products, basic_auth, jwt_auth

app = FastAPI()

#add the routers to the app
app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth.router)
app.include_router(jwt_auth.router)
app.include_router(products_mongo.router)

#static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#run the module on windows using --- python -m fastapi dev main.py    