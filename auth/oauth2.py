from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session

from database.db import get_db
from database.db_user import raed_a_user_username

# check url is ok by token
oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')

# in terminal type
# openssl rand -hex 127
SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'
# or
# SECRET_KEY = b64encode(token_bytes(127)).decode()

# set algorithm
ALGORITHM = 'HS256'

# time access in site
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def refresh_access_token(current_token: str) -> str:
    try:
        # get the current token and Extraction data
        decoded_token = jwt.decode(current_token, SECRET_KEY, algorithms=ALGORITHM)
        expiration_time = datetime.fromtimestamp(decoded_token['exp'])
        current_time = datetime.now()
        remaining_time = expiration_time - current_time

        # Checking whether the token has expired or the remaining time of the token is less than 3 minutes
        if current_time > expiration_time or remaining_time < timedelta(minutes=5):

            # Open current token and extract user information
            user_data = jwt.decode(current_token, SECRET_KEY, algorithms=ALGORITHM)

            # Create a new token with a new expiration time
            new_token = create_access_token(user_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
            return new_token

        else:
            return current_token

    except JWTError:
        return current_token


# ================================================================================
def get_current_user(token: str = Depends(oauth_scheme),
                     db: Session = Depends(get_db)):
    # Define an exception to handle non-validation errors
    error_create = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail="invalid value",
                                 headers={'WWW-authenticate': 'bearer'})
    try:
        # Opening the token and extracting the required information (such as username)
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')

        # If the username is not present in the token, it will return a non-validation error
        if not username:
            raise error_create

        # If the token has expired, it updates the token
        if is_token_expired(token):
            refresh_access_token(token)

            raise error_create

    # It should also return a non-validation error so that the client requests a new token again
    except JWTError:
        # Returns a non-validation error if an error occurred while opening the token
        raise error_create

    user = raed_a_user_username(username, db)
    return user


# ================================================================================
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Copy the data to a new variable
    to_encode = data.copy()

    # If the expiration time is set, calculate the expiration time based on it
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    # Otherwise, set the token expiration time to default (5 minutes).
    else:
        expire = datetime.utcnow() + timedelta(minutes=5)

    # # Add expiration time to data
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Return the generated token
    return encoded_jwt


# ================================================================================
def is_token_expired(token: str) -> bool:
    # Open the token and extract the expiration time
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        expiration_time = datetime.fromtimestamp(decoded_token['exp'])
        current_time = datetime.now()

        # Check if the current time is greater than the expiration time
        return current_time > expiration_time

    # If there are any errors related to the token (such as an error in opening the token or the token is invalid),
    # we consider the token to be expired.
    except (jwt.DecodeError, jwt.InvalidTokenError):
        return True


# =================================================================================
def up_token():
    pass
