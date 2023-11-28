from fastapi import APIRouter, Depends

from Schema.schemas import UserBase, AccessBase
from auth.oauth2 import get_current_user
from database import db_user, db_access
from database.db import get_db
from management.manage import is_admin

router = APIRouter(prefix='/user', tags=['user'])


# create new user
# =========================================================
# without authenticate
@router.post('/')  # response_model=UserDisplay
def create_user(user: UserBase, access: AccessBase, db=Depends(get_db)):
    x = db_user.create_user(db, user)
    access.user_id = x.user_id
    db_access.create_access(db, access)
    return {'ok'}


# ===========================================================
# # read all users
@router.get('/')
def read_all_users(db=Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    if current_user:
        if is_admin(db):
            return {'data': db_user.read_all_users(db)}
    return {'not ok'}


# ======================================================
# # read a user
@router.get('/{username}')
def read_a_user(username: str, db=Depends(get_db),
                current_user: UserBase = Depends(get_current_user)):
    if current_user:
        if is_admin(current_user):
            return {'data': db_user.get_one_user(username, db)}
    return {'not ok'}


# # ====================================================
# update a user
@router.put('/update/{username}')
def update_a_user(username: str, user: UserBase, db=Depends(get_db),
                  current_user: UserBase = Depends(get_current_user)):
    if current_user:
        if is_admin(db):
            return db_user.update_one_user(username, user)
    return {'not ok'}


# =======================================================
# delete a user
@router.delete('/delete/{username}')
def delete_a_user(username: str, db=Depends(get_db),
                  current_user: UserBase = Depends(get_current_user)):
    if current_user:
        if is_admin():
            db_user.delete_a_user(username, db)
        return {'ok'}
    return {'not ok'}
