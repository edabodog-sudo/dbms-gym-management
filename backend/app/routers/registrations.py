from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.config import verify_api_key


router = APIRouter(
    prefix="/registrations",
    tags=["registrations"]
)


# =========================
# CREATE REGISTRATION - PROTECTED
# =========================

@router.post(
    "/",
    response_model=schemas.RegistrationResponse,
    dependencies=[Depends(verify_api_key)]
)
def create_registration(
    registration: schemas.RegistrationCreate,
    db: Session = Depends(get_db)
):
    new_registration = crud.create_registration(
        db=db,
        registration=registration
    )

    if new_registration is None:
        raise HTTPException(
            status_code=409,
            detail="Member already registered for this course"
        )

    return new_registration


# =========================
# READ ALL REGISTRATIONS - PUBLIC
# =========================

@router.get(
    "/",
    response_model=list[schemas.RegistrationResponse]
)
def read_registrations(
    db: Session = Depends(get_db)
):
    return crud.get_registrations(db=db)


# =========================
# READ ONE REGISTRATION - PUBLIC
# =========================

@router.get(
    "/{registration_id}",
    response_model=schemas.RegistrationResponse
)
def read_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    registration = crud.get_registration(
        db=db,
        registration_id=registration_id
    )

    if registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return registration


# =========================
# UPDATE REGISTRATION - PROTECTED
# =========================

@router.put(
    "/{registration_id}",
    response_model=schemas.RegistrationResponse,
    dependencies=[Depends(verify_api_key)]
)
def update_registration(
    registration_id: int,
    registration: schemas.RegistrationUpdate,
    db: Session = Depends(get_db)
):
    updated_registration = crud.update_registration(
        db=db,
        registration_id=registration_id,
        registration=registration
    )

    if updated_registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return updated_registration


# =========================
# DELETE REGISTRATION - PROTECTED
# =========================

@router.delete(
    "/{registration_id}",
    response_model=schemas.RegistrationResponse,
    dependencies=[Depends(verify_api_key)]
)
def delete_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    deleted_registration = crud.delete_registration(
        db=db,
        registration_id=registration_id
    )

    if deleted_registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return deleted_registration
