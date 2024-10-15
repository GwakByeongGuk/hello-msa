from fastapi import APIRouter, Depends
from schema.product import Product, ProductBase
from sqlalchemy.orm import Session
from service.database import get_db
from service.product import register

router = APIRouter()

@router.post('/product', response_model=Product)
async def new_product(product: ProductBase, db:Session=Depends(get_db)):
    print(product)

    return register(db, product)
