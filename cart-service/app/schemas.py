from pydantic import BaseModel
from typing import List
from datetime import datetime


class CartCreate(BaseModel):

    user_id: int
    product_id: int
    quantity: int


class CartItemUpdate(BaseModel):

    quantity: int


class CartItemResponse(BaseModel):

    id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True


class CartResponse(BaseModel):

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    items: List[CartItemResponse] = []

    class Config:
        from_attributes = True