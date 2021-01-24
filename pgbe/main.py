from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Piece from main fastapi tutorial - readme.md @ https://github.com/tiangolo/fastapi
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
async def read_root():
    return {"Hello": "Test automated deployment - ddd"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}


# Pets part from https://medium.com/@bruno.fosados/
@app.get("/pets/")
async def get_all_pets():
    """[summary]
    Gets all pets adopted/rescued or not.
    [description]
    Endpoint for all pets.
    """
    fake_pets = [{"name": "Guero"}, {"name": "Pepita"}]
    return fake_pets