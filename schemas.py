from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class Product(ProductCreate):
    id: int

    class Config:
        orm_mode = True