from sqlalchemy.orm import Session

from app import models, schemas


# =========================
# MEMBERS
# =========================

def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(
        name=member.name,
        email=member.email
    )

    db.add(db_member)
    db.commit()
    db.refresh(db_member)

    return db_member


def get_members(db: Session):
    return db.query(models.Member).all()


def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(
        models.Member.id == member_id
    ).first()


def update_member(
    db: Session,
    member_id: int,
    member: schemas.MemberUpdate
):
    db_member = db.query(models.Member).filter(
        models.Member.id == member_id
    ).first()

    if db_member is None:
        return None

    db_member.name = member.name
    db_member.email = member.email

    db.commit()
    db.refresh(db_member)

    return db_member


def delete_member(db: Session, member_id: int):
    db_member = db.query(models.Member).filter(
        models.Member.id == member_id
    ).first()

    if db_member is None:
        return None

    db.delete(db_member)
    db.commit()

    return db_member


# =========================
# COURSES
# =========================

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(
        name=course.name,
        trainer=course.trainer,
        schedule=course.schedule
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def get_courses(db: Session):
    return db.query(models.Course).all()


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()


def update_course(
    db: Session,
    course_id: int,
    course: schemas.CourseUpdate
):
    db_course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if db_course is None:
        return None

    db_course.name = course.name
    db_course.trainer = course.trainer
    db_course.schedule = course.schedule

    db.commit()
    db.refresh(db_course)

    return db_course


def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if db_course is None:
        return None

    db.delete(db_course)
    db.commit()

    return db_course


# =========================
# REGISTRATIONS
# =========================

def create_registration(
    db: Session,
    registration: schemas.RegistrationCreate
):
    existing_registration = db.query(models.Registration).filter(
        models.Registration.member_id == registration.member_id,
        models.Registration.course_id == registration.course_id
    ).first()

    if existing_registration is not None:
        return None

    db_registration = models.Registration(
        member_id=registration.member_id,
        course_id=registration.course_id
    )

    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)

    return db_registration


def get_registrations(db: Session):
    return db.query(models.Registration).all()


def get_registration(db: Session, registration_id: int):
    return db.query(models.Registration).filter(
        models.Registration.id == registration_id
    ).first()


def update_registration(
    db: Session,
    registration_id: int,
    registration: schemas.RegistrationUpdate
):
    db_registration = db.query(models.Registration).filter(
        models.Registration.id == registration_id
    ).first()

    if db_registration is None:
        return None

    db_registration.member_id = registration.member_id
    db_registration.course_id = registration.course_id

    db.commit()
    db.refresh(db_registration)

    return db_registration


def delete_registration(db: Session, registration_id: int):
    db_registration = db.query(models.Registration).filter(
        models.Registration.id == registration_id
    ).first()

    if db_registration is None:
        return None

    db.delete(db_registration)
    db.commit()

    return db_registration


# =========================
# PAYMENTS
# =========================

def create_payment(
    db: Session,
    payment: schemas.PaymentCreate
):
    db_payment = models.Payment(
        member_id=payment.member_id,
        amount=payment.amount,
        payment_date=payment.payment_date
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return db_payment


def get_payments(db: Session):
    return db.query(models.Payment).all()


def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(
        models.Payment.id == payment_id
    ).first()


def update_payment(
    db: Session,
    payment_id: int,
    payment: schemas.PaymentUpdate
):
    db_payment = db.query(models.Payment).filter(
        models.Payment.id == payment_id
    ).first()

    if db_payment is None:
        return None

    db_payment.member_id = payment.member_id
    db_payment.amount = payment.amount
    db_payment.payment_date = payment.payment_date

    db.commit()
    db.refresh(db_payment)

    return db_payment


def delete_payment(db: Session, payment_id: int):
    db_payment = db.query(models.Payment).filter(
        models.Payment.id == payment_id
    ).first()

    if db_payment is None:
        return None

    db.delete(db_payment)
    db.commit()

    return db_payment
