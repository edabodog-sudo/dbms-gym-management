from datetime import date
from decimal import Decimal

from pydantic import BaseModel, EmailStr


class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    pass


class MemberResponse(MemberBase):
    id: int

    class Config:
        from_attributes = True


class CourseBase(BaseModel):
    name: str
    trainer: str
    schedule: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    pass


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True


class RegistrationBase(BaseModel):
    member_id: int
    course_id: int


class RegistrationCreate(RegistrationBase):
    pass


class RegistrationUpdate(RegistrationBase):
    pass


class RegistrationResponse(RegistrationBase):
    id: int

    class Config:
        from_attributes = True


class PaymentBase(BaseModel):
    member_id: int
    amount: Decimal
    payment_date: date


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    pass


class PaymentResponse(PaymentBase):
    id: int

    class Config:
        from_attributes = True
