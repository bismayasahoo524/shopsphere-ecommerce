from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


VALID_ORDER_STATUSES = [
    "CREATED",
    "PAYMENT_PENDING",
    "PAID",
    "PROCESSING",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED"
]


# Create Order
@router.post(
    "",
    response_model=schemas.OrderResponse
)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):

    new_order = models.Order(
        user_id=order.user_id,
        total_amount=order.total_amount,
        status="CREATED"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


# Get Order by ID
@router.get(
    "/{order_id}",
    response_model=schemas.OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(
        models.Order
    ).filter(
        models.Order.id == order_id
    ).first()

    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


# Get All Orders for a User
@router.get(
    "/user/{user_id}",
    response_model=list[schemas.OrderResponse]
)
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_db)
):

    orders = db.query(
        models.Order
    ).filter(
        models.Order.user_id == user_id
    ).all()

    return orders


# Update Order Status
@router.put(
    "/{order_id}/status",
    response_model=schemas.OrderResponse
)
def update_order_status(
    order_id: int,
    status_update: schemas.OrderStatusUpdate,
    db: Session = Depends(get_db)
):

    order = db.query(
        models.Order
    ).filter(
        models.Order.id == order_id
    ).first()

    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if status_update.status not in VALID_ORDER_STATUSES:

        raise HTTPException(
            status_code=400,
            detail="Invalid order status"
        )

    order.status = status_update.status

    db.commit()
    db.refresh(order)

    return order