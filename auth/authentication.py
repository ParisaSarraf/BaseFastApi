from fastapi import APIRouter, Depends, status

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from database import models
from database.db import get_db
from database.hash import Hash

from auth import oauth2

router = APIRouter(tags=['authentication'])


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.user_username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid username")

    if Hash.verify(user.user_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid password")

    access_token = oauth2.create_access_token(data={'sub': request.username})

    return {
        'accessToken': access_token,
        'username': user.user_username,
        'detail': 'ok'
    }
