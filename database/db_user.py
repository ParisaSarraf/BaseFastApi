from sqlalchemy.orm import Session
from Schema.schemas import UserBase
from database.hash import Hash
from database.models import DbUser


# ====================================================
def create_user(db: Session, request: UserBase):
    db.query(DbUser).filter(DbUser.user_username == request.user_username).first()
    hashed_password = Hash.bcrypt(request.user_password)
    user = DbUser(
        user_username=request.user_username,
        user_name_surname=request.user_name_surname,
        user_password=hashed_password,
        user_national_code=request.user_national_code,
        user_presence=request.user_presence,
        user_is_admin=request.user_is_admin
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# ====================================================================
def read_all_users(db: Session):
    return db.query(DbUser).all()


# ====================================================================
def get_one_user(username, db: Session):
    user = db.query(DbUser).filter(DbUser.user_username == username).first()
    return user


# ====================================================================
def raed_a_user_username(username_user, db: Session):
    user = db.query(DbUser).filter(DbUser.user_username == username_user).first()
    return user


# ===================================================================
def delete_a_user(username, db: Session):
    user = get_one_user(username, db)
    db.delete(user)
    db.commit()
    return 'ok'


# ====================================================================
def update_one_user(username, db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.user_username == username).first()
    user.update({
        DbUser.user_username: request.user_username,
        DbUser.user_name_surname: request.user_name_surname,
        DbUser.user_password: request.user_password,
        DbUser.user_national_code: request.user_national_code,
        DbUser.user_is_admin: request.user_is_admin,
    })
    db.commit()
    return 'ok'
