from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Product(BaseModel):
    name: str
    price: int
    maker: str
    desc: str
    regdate: datetime

@router.post('/product')
async def new_user(product: Product):
    print(product)

    return {'msg': 'ok'}
