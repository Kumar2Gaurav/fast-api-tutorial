from enum import Enum
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

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


@app.get("/users/{user_id}/items/{items_id}")
async def list_items(user_id: int, item_id: int, q: str | None = None, s: bool = False):
    res = {"user_id": user_id, "item_id": item_id}
    if q:
        res.update({"q": q})
    if not s:
        res.update({"s": s})
    return res


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_items(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.tax + item.price
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{items_id}")
async def create_items(items_id: str, item: Item):
    item_dict = item.dict()
    if items_id:
        item_dict.update({"items_id": items_id})
    if item.tax:
        price_with_tax = item.tax + item.price
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/{items_id}")
async def read_items(items_id: str,
                     q: str | None = Query(
                         None,
                         min_length=3,
                         max_length=10,
                         title="sample query string",
                         alias="items-query", description="This is the sample query ")):
    results = {"items": [{"item": "foo"}, {"items": "bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/item_validations/{items_id}")
async def item_validations(items_id: int = Path(..., ge=10, lt=100, title="This is ID of item"),
                           q: str | None = Query(
                               None,
                               min_length=3,
                               max_length=10,
                               title="sample query string",
                               alias="items-query", description="This is the sample query ")):
    results = {"items": [{"item": "foo"}, {"items": "bar"}]}
    if q:
        results.update({"q": q})
    return results
