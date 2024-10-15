from pydantic import BaseModel

class UserBase(BaseModel):
    userid: str
    passwd: str
    name: str
    email: str

class User(UserBase):
    mno: int
    regdate: str

    # ORM 맵핑을 위한 설정
    class Config:
        from_attribute=True