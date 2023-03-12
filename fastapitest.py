'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World!"