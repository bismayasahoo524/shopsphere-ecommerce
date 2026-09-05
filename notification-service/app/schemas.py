from pydantic import BaseModel, EmailStr


class OrderConfirmation(BaseModel):
    order_id: int
    customer_email: EmailStr
    customer_name: str


class PaymentConfirmation(BaseModel):
    order_id: int
    payment_id: str
    customer_email: EmailStr
    customer_name: str
    amount: float


class ShipmentNotification(BaseModel):
    order_id: int
    customer_email: EmailStr
    customer_name: str
    tracking_number: str