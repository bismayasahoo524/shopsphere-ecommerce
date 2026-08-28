from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from .database import Base


class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, nullable=False)

    transaction_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    amount = Column(Float, nullable=False)

    status = Column(
        String,
        default="PENDING",
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )