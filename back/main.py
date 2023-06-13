from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.responses import RedirectResponse, JSONResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


def redirect_to_docs():
    return RedirectResponse(url="/docs")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="API documentation for your store",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(app.openapi())


class User(BaseModel):
    id: str
    name: str
    ciclo: int
    password: str


#
# class Product(BaseModel):
#     id: str
#     name: str
#     price: float
#     stock: int
#
#
# class Shoppingcart(BaseModel):
#     id: str
#     name: str
#     products: list<Product>


products = [
    {"id": "1", "name": "book", "price": 5.99, "stock": 5},
    {"id": "2", "name": "laptop", "price": 100.99, "stock": 2},
    {"id": "3", "name": "table", "price": 20.99, "stock": 100}
]

users = []

users.append(User(id="1", name="Nicolas", ciclo=5, password="1234"))
users.append(User(id="2", name="Renato", ciclo=5, password="2345"))
users.append(User(id="3", name="Jose", ciclo=5, password="4567"))

# shoppingcarts = [
#     {"user_id": "1", "name": User(id="1")["name"],
#      "products": [{"id": "1", "name": "book", "price": 5.99, "stock": 1}]},
#     {"user_id": "2", "name": User(id="2")["name"],
#      "products": [{"id": "1", "name": "book", "price": 5.99, "stock": 1}]},
#     {"user_id": "3", "name": User(id="3")["name"], "products": [{"id": "1", "name": "book", "price": 5.99, "stock": 1}]}
# ]


#
# Security - RENATO
@app.post("/login/{userid}/{password}")
def login_user(userid: str, password: str):
    auth: bool = False
    for i in range(len(users)):
        if users[i].id == userid and users[i].password == password:
            auth = True

    response = {
        "code": 200,
        "authorizate": auth
    }
    return response


# USER - RENATO

@app.post("/user")
def register(user: User):
    users.append(user)
    response = {
        "code": 200,
        "user": user.dict()
    }
    return response


@app.get("/user")
def get_users():
    response = {
        "code": 200,
        "users": [user.dict() for user in users]
    }
    return json.dumps(response)


@app.get("/user/{id}")
def get_user(id: str):
    user: dict = {}
    for i in range(len(users)):
        if users[i]["id"] == id:
            user = users[i]

    if user == {}:
        raise HTTPException(status_code=404, detail="User not found")

    response = {
        "code": 200,
        "user": user,
    }
    return json.dumps(response)


# PRODUCTS - NICOLAS
# DONE
@app.get("/products")
def get_products():
    response = {
        "code": 200,
        "products": products
    }
    return json.dumps(response)


# DONE
@app.get("/products/{product_id}")
def get_product(product_id: str):
    response = next((product for product in products if product["id"] == product_id), None)
    if response is None:
        raise HTTPException(status_code=404, detail="User not found")

    return json.dumps(response)


# DONE
@app.post("/products")
def post_product(product):
    product = json.loads(product)
    products.append(product)
    response = {
        "code": 200,
        "message": "Item successfully added!"
    }

    return response


# DONE
@app.delete("/product/{product_id}")
def delete_product(product_id: str):
    for i in range(len(products)):
        if products[i]["id"] == product_id:
            del products[i]
            response = {
                "code": 200,
                "message": "Item successfully deleted!"
            }
            return response
    raise HTTPException(status_code=404, detail="Product not found")


# DONE
@app.put("/product/{product_id}")
def put_product(product_id: str, product):
    product = json.loads(product)
    for i in range(len(products)):
        if products[i]["id"] == product_id:
            products[i] = product
            response = {
                "code": 200,
                "message": "Item successfully added!"
            }
            return response
    raise HTTPException(status_code=404, detail="Product not found")

# # SHOPPINGCART - JOSE
# @app.get("/users/{user_id}/shoppingcart")
# def getShoppingcart(user_id: str):
#     response = {
#         "user_id": user_id,
#         "user_name": User(id=int(user_id))["name"],
#         "products": shoppingcarts[int(user_id)]["products"]
#     }
#
#     if user_id is None:
#         raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
#
#     return response
#
#
# @app.post("/users/{user_id}/shoppingcart")
# def postShoppingcart(user_id: str):
#     response = {
#         "code": 200,
#         "message": "Shoppingcart successfully added!"
#     }
#
#     if user_id is None:
#         raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
#
#     return response
#
#
# @app.put("users/{user_id}/shoppingcart")
# def postItemShoppingcart(user_id: str, product: dict):  # {"id": "1", "name": "book", "price": 5.99, "stock": 5}
#     product = json.loads(product)
#     shoppingcart = shoppingcarts[int(user_id) - 1]
#     if product is None:
#         raise HTTPException(status_code=404, detail="No se ha brindado el producto")
#
#     shoppingcart[int(user_id) - 1]["products"].append(product)
#
#     response = {
#         "code": 200,
#         "message": "Product successfully added into shoppingcart!"
#     }
#     return response

if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000)