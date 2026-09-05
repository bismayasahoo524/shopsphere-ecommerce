from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Cart(Base):

    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, unique=True, index=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    items = relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete-orphan"
    )


class CartItem(Base):

    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)

    cart_id = Column(
        Integer,
        ForeignKey("carts.id")
    )

    product_id = Column(Integer, index=True)

    quantity = Column(Integer)

    price = Column(Float)

    cart = relationship(
        "Cart",
        back_populates="items"
    )