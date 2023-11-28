# from base64 import b64encode
# from datetime import timedelta, datetime
# from secrets import token_bytes
# from typing import Optional
#
# from fastapi import Depends, status
# from fastapi.exceptions import HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt
# from jose.exceptions import JWTError
# from sqlalchemy.orm import Session
#
# from database.db import get_db
# from database.db_user import raed_a_user_username
#
# # check url is ok by token
# oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')
#
# # openssl rand -hex 63
# SECRET_KEY = b64encode(token_bytes(63)).decode()
# # SECRET_KEY = 'KO9pP6/ZqtdCkgeb2XPUUrtizbpXLGXgmYfVYxcEUYmyfx6het0Izpjcj8ws5UVpVhBRNk/CArwpv9CcPUPF'
#
# # set algorithm
# ALGORITHM = 'HS256'
#
# # time access in site
# ACCESS_TOKEN_EXPIRE_MINUTES = 15
#
#
# # ===========================================================================
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#
#     to_encode.update({'exp': expire})
#
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#
#     return encoded_jwt
#
#
# # ==================================================================================================parisa
# # def refresh_access_token(current_token: str) -> str:
# #     try:
# #         decoded_token = jwt.decode(current_token, SECRET_KEY, algorithms=ALGORITHM)
# #         expiration_time = datetime.fromtimestamp(decoded_token['exp'])
# #         current_time = datetime.now()
# #         remaining_time = expiration_time - current_time
# #
# #         if current_time > expiration_time or remaining_time < timedelta(minutes=5):
# #             user_data = jwt.decode(current_token, SECRET_KEY, algorithms=ALGORITHM)
# #             new_token = create_access_token(user_data, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
# #             return new_token
# #         else:
# #             return current_token
# #
# #     except JWTError:
# #         return current_token
# #
# #
# # from datetime import datetime
# #
# #
# # def is_token_expired(token: str) -> bool:
# #     try:
# #         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
# #         expiration_time = datetime.fromtimestamp(decoded_token['exp'])
# #         current_time = datetime.now()
# #         return current_time > expiration_time
# #     except jwt.ExpiredSignatureError:
# #         return True
# #     except (jwt.DecodeError, jwt.InvalidTokenError):
# #         return True
# # =========================================================================================parisa
#
#
# # =========================================================================================old
# def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
#     print(token)
#     error_create = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                  detail="invalid value",
#                                  headers={'WWW-authenticate': 'bearer'})
#     try:
#         _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
#         username = _dict.get('sub')
#         if not username:
#             raise error_create
#
#     except JWTError:
#         raise error_create
#
#     user = raed_a_user_username(username, db)
#     return user
# # =========================================================================================old
# # def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
# #     error_create = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
# #                                  detail="invalid value",
# #                                  headers={'WWW-authenticate': 'bearer'})
# #     try:
# #         _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
# #         username = _dict.get('sub')
# #         if not username:
# #             raise error_create
# #
# #         if is_token_expired(token):
# #             new_token = refresh_access_token(token)
# #
# #             if new_token != token:
# #                 response.headers['Authorization'] = f"Bearer {new_token}"
# #
# #             raise error_create
# #
# #     except JWTError:
# #         raise error_create
# #
# #     user = raed_a_user_username(username, db)
# #     return user
