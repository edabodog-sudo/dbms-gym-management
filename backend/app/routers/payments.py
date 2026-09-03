from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.config import verify_api_key


router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)


# =========================
# CREATE PAYMENT - PROTECTED
# =========================

@router.post(
    "/",
    response_model=schemas.PaymentResponse,
    dependencies=[Depends(verify_api_key)]
)
def create_payment(
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_payment(
        db=db,
        payment=payment
    )


# =========================
# READ ALL PAYMENTS - PUBLIC
# =========================

@router.get(
    "/",
    response_model=list[schemas.PaymentResponse]
)
def read_payments(
    db: Session = Depends(get_db)
):
    return crud.get_payments(db=db)


# =========================
# READ ONE PAYMENT - PUBLIC
# =========================

@router.get(
    "/{payment_id}",
    response_model=schemas.PaymentResponse
)
def read_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = crud.get_payment(
        db=db,
        payment_id=payment_id
    )

    if payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


# =========================
# UPDATE PAYMENT - PROTECTED
# =========================

@router.put(
    "/{payment_id}",
    response_model=schemas.PaymentResponse,
    dependencies=[Depends(verify_api_key)]
)
def update_payment(
    payment_id: int,
    payment: schemas.PaymentUpdate,
    db: Session = Depends(get_db)
):
    updated_payment = crud.update_payment(
        db=db,
        payment_id=payment_id,
        payment=payment
    )

    if updated_payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return updated_payment


# =========================
# DELETE PAYMENT - PROTECTED
# =========================

@router.delete(
    "/{payment_id}",
    response_model=schemas.PaymentResponse,
    dependencies=[Depends(verify_api_key)]
)
def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    deleted_payment = crud.delete_payment(
        db=db,
        payment_id=payment_id
    )

    if deleted_payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return deleted_payment
