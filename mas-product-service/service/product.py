from sqlalchemy.orm import Session
from schema.product import ProductBase
from models.product import Product


# 회원가입 처리
# 기본 회원정보 + 번호, 가입일
def register(db: Session, product: ProductBase):
    product = Product(**product.model_dump()) # 유효성 검사
    db.add(product)
    db.commit()
    db.refresh(product)
    print(product)

    return product