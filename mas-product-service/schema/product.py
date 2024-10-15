from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    desc: str
    price: int
    maker: str
    regdate: str

class Product(ProductBase):
    pno: int

    # ORM 맵핑을 위한 설정
    class Config:
        from_attribute=True