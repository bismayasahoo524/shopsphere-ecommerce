from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db
from .product_client import get_product


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post(
    "",
    response_model=schemas.CartResponse
)
def add_to_cart(
    cart_data: schemas.CartCreate,
    db: Session = Depends(get_db)
):

    product = get_product(cart_data.product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    cart = db.query(models.Cart).filter(
        models.Cart.user_id == cart_data.user_id
    ).first()

    if not cart:
        cart = models.Cart(
            user_id=cart_data.user_id
        )

        db.add(cart)
        db.commit()
        db.refresh(cart)

    cart_item = db.query(
        models.CartItem
    ).filter(
        models.CartItem.cart_id == cart.id,
        models.CartItem.product_id == cart_data.product_id
    ).first()

    if cart_item:
        cart_item.quantity += cart_data.quantity

    else:
        cart_item = models.CartItem(
            cart_id=cart.id,
            product_id=cart_data.product_id,
            quantity=cart_data.quantity,
            price=product["price"]
        )

        db.add(cart_item)

    db.commit()
    db.refresh(cart)

    return cart


@router.get(
    "/{user_id}",
    response_model=schemas.CartResponse
)
def get_cart(
    user_id: int,
    db: Session = Depends(get_db)
):

    cart = db.query(models.Cart).filter(
        models.Cart.user_id == user_id
    ).first()

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart not found"
        )

    return cart


@router.put(
    "/{item_id}",
    response_model=schemas.CartItemResponse
)
def update_cart_item(
    item_id: int,
    item_data: schemas.CartItemUpdate,
    db: Session = Depends(get_db)
):

    cart_item = db.query(
        models.CartItem
    ).filter(
        models.CartItem.id == item_id
    ).first()

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    cart_item.quantity = item_data.quantity

    db.commit()
    db.refresh(cart_item)

    return cart_item


@router.delete(
    "/{item_id}"
)
def delete_cart_item(
    item_id: int,
    db: Session = Depends(get_db)
):

    cart_item = db.query(
        models.CartItem
    ).filter(
        models.CartItem.id == item_id
    ).first()

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    db.delete(cart_item)
    db.commit()

    return {
        "message": "Item removed from cart"
    }
