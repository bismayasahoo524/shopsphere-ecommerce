from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):

    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    category: Optional[str] = None
    image_url: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True