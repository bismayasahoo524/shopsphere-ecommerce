from pydantic import BaseModel
from datetime import datetime


class PaymentCreate(BaseModel):

    order_id: int
    amount: float


class PaymentResponse(BaseModel):

    id: int
    order_id: int
    transaction_id: str
    amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True