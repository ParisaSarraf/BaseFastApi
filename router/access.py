from typing import List

from fastapi import APIRouter, Depends

from Schema.schemas import AccessBase, AccessDisplay
from database import db_access
from database.db import get_db

router = APIRouter(prefix='/access', tags=['access'])


# =======================================================
# create new access
@router.post('/', response_model=AccessDisplay)
def create_access(arte: AccessBase, db=Depends(get_db)):
    return db_access.create_access(db, arte)


# =======================================================
# read all access
@router.get('/', response_model=List[AccessDisplay])
def read_all_access(db=Depends(get_db)):
    return db_access.read_all_access(db)


# =======================================================
# read a access
@router.get('/{id_arte}', response_model=AccessDisplay)
def raed_an_access(id_arte: int, db=Depends(get_db)):
    return db_access.raed_a_access(id_arte, db)


# # =======================================================
# update a access
@router.post('/update/{id_arte}', response_model=AccessDisplay)
def update_an_access(id_arte: int, user: AccessBase, db=Depends(get_db)):
    return db_access.update_an_access(id_arte, db, user)


# =======================================================
# delete a access
@router.post('/delete/{id_arte}')
def delete_an_access(id_arte: int, db=Depends(get_db)):
    return db_access.delete_a_access(id_arte, db)
