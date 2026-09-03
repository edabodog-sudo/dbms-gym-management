from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.config import verify_api_key


router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)


# =========================
# CREATE COURSE - PROTECTED
# =========================

@router.post(
    "/",
    response_model=schemas.CourseResponse,
    dependencies=[Depends(verify_api_key)]
)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(get_db)
):
    return crud.create_course(
        db=db,
        course=course
    )


# =========================
# READ ALL COURSES - PUBLIC
# =========================

@router.get("/", response_model=list[schemas.CourseResponse])
def read_courses(
    db: Session = Depends(get_db)
):
    return crud.get_courses(db=db)


# =========================
# READ ONE COURSE - PUBLIC
# =========================

@router.get(
    "/{course_id}",
    response_model=schemas.CourseResponse
)
def read_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = crud.get_course(
        db=db,
        course_id=course_id
    )

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


# =========================
# UPDATE COURSE - PROTECTED
# =========================

@router.put(
    "/{course_id}",
    response_model=schemas.CourseResponse,
    dependencies=[Depends(verify_api_key)]
)
def update_course(
    course_id: int,
    course: schemas.CourseUpdate,
    db: Session = Depends(get_db)
):
    updated_course = crud.update_course(
        db=db,
        course_id=course_id,
        course=course
    )

    if updated_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated_course


# =========================
# DELETE COURSE - PROTECTED
# =========================

@router.delete(
    "/{course_id}",
    response_model=schemas.CourseResponse,
    dependencies=[Depends(verify_api_key)]
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    deleted_course = crud.delete_course(
        db=db,
        course_id=course_id
    )

    if deleted_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return deleted_course
