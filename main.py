from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="This is our first route")
async def root():
    return {"message": " hewllo word"}


@app.post("/")
async def post():
    return {"message": "hello from post route"}


@app.put("/")
async def put():
    return {"message": "hello from post route"}


@app.get("/items")
async def list_items():
    return {"message": "list items route"}


@app.get("/items/items_id")
async def get_items(items_id: int):
    return {"items_id": items_id}


@app.get("/users/me")
async def get_current_user():
    return {"message": "this is current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {food_name: food_name, "message": "you like healthy food"}
    if food_name == FoodEnum.fruits:
        return {food_name: food_name, "message": "you like sweet product"}
    return {food_name: food_name, "message": "you like dairy product"}
