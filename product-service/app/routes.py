from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# GET ALL PRODUCTS
@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):

    products = db.query(models.Product).all()

    return products


# GET PRODUCT BY ID
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# CREATE PRODUCT
@router.post(
    "/",
    response_model=schemas.ProductResponse,
    status_code=201
)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = models.Product(
        **product.model_dump()
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# UPDATE PRODUCT
@router.put(
    "/{product_id}",
    response_model=schemas.ProductResponse
)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):

    existing_product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

    if existing_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    for key, value in product.model_dump().items():
        setattr(existing_product, key, value)

    db.commit()
    db.refresh(existing_product)

    return existing_product


# DELETE PRODUCT
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }