from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class OrderCreate(BaseModel):

    user_id: int

    total_amount: float


class OrderStatusUpdate(BaseModel):

    status: str


class OrderResponse(BaseModel):

    id: int

    user_id: int

    total_amount: float

    status: str

    created_at: datetime

    updated_at: Optional[datetime] = None


    class Config:
        from_attributes = True