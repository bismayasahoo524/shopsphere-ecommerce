import random
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db


router = APIRouter(
    prefix="/payment",
    tags=["Payment"]
)


@router.post(
    "",
    response_model=schemas.PaymentResponse
)
def create_payment(
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db)
):

    # Generate a unique transaction ID
    transaction_id = str(uuid.uuid4())

    # Create payment with PENDING status
    new_payment = models.Payment(
        order_id=payment.order_id,
        transaction_id=transaction_id,
        amount=payment.amount,
        status="PENDING"
    )

    # Save payment to database
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    # Simulate payment processing
    payment_status = random.choice([
        "SUCCESS",
        "FAILED"
    ])

    # Update payment status
    new_payment.status = payment_status

    db.commit()
    db.refresh(new_payment)

    return new_payment