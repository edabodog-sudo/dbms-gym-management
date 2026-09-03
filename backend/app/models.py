from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint,
    Numeric,
    Date
)

from app.database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    trainer = Column(String, nullable=False)
    schedule = Column(String, nullable=False)


class Registration(Base):
    __tablename__ = "registrations"

    __table_args__ = (
        UniqueConstraint(
            "member_id",
            "course_id",
            name="uq_member_course"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    member_id = Column(
        Integer,
        ForeignKey("members.id"),
        nullable=False
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False
    )


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    member_id = Column(
        Integer,
        ForeignKey("members.id"),
        nullable=False
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    payment_date = Column(
        Date,
        nullable=False
    )

