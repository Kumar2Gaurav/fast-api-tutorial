from fastapi import FastAPI

app = FastAPI()


@app.get("/",description="This is our first route",deprecated=True)
async def root():
    return {"message": " hewllo word"}


@app.post("/")
async def post():
    return {"message": "hello from post route"}


@app.put("/")
async def put ():
    return {"message": "hello from post route"}
