from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.config import verify_api_key


router = APIRouter(
    prefix="/members",
    tags=["members"]
)


# =========================
# CREATE MEMBER - PROTECTED
# =========================

@router.post(
    "/",
    response_model=schemas.MemberResponse,
    dependencies=[Depends(verify_api_key)]
)
def create_member(
    member: schemas.MemberCreate,
    db: Session = Depends(get_db)
):
    return crud.create_member(db=db, member=member)


# =========================
# READ ALL MEMBERS - PUBLIC
# =========================

@router.get("/", response_model=list[schemas.MemberResponse])
def read_members(db: Session = Depends(get_db)):
    return crud.get_members(db=db)


# =========================
# READ ONE MEMBER - PUBLIC
# =========================

@router.get("/{member_id}", response_model=schemas.MemberResponse)
def read_member(
    member_id: int,
    db: Session = Depends(get_db)
):
    member = crud.get_member(
        db=db,
        member_id=member_id
    )

    if member is None:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return member


# =========================
# UPDATE MEMBER - PROTECTED
# =========================

@router.put(
    "/{member_id}",
    response_model=schemas.MemberResponse,
    dependencies=[Depends(verify_api_key)]
)
def update_member(
    member_id: int,
    member: schemas.MemberUpdate,
    db: Session = Depends(get_db)
):
    updated_member = crud.update_member(
        db=db,
        member_id=member_id,
        member=member
    )

    if updated_member is None:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return updated_member


# =========================
# DELETE MEMBER - PROTECTED
# =========================

@router.delete(
    "/{member_id}",
    response_model=schemas.MemberResponse,
    dependencies=[Depends(verify_api_key)]
)
def delete_member(
    member_id: int,
    db: Session = Depends(get_db)
):
    deleted_member = crud.delete_member(
        db=db,
        member_id=member_id
    )

    if deleted_member is None:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return deleted_member
