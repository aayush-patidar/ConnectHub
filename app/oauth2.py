from jose import jwt,JWTError
from fastapi.security.oauth2 import OAuth2PasswordBearer
from .config import settings
from . import schemas
from fastapi import HTTPException,status,Depends
from datetime import timedelta,datetime,timezone

oauth_scheme=OAuth2PasswordBearer(tokenUrl="login")


def access_token(data:dict):
    to_encode=data.copy()

    exp=datetime.now(timezone.utc)+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"]=int(exp.timestamp())

    token=jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    print (token)
    return token

def verify_token(token:str,credentials_exception):
    try:
        check=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        id=check.get("id")
        email=check.get("email")
        if not id:
            raise credentials_exception

        token_data=schemas.TokenData(id=id,email=email)
        return token_data
    except JWTError as e:
        return e

def get_user(token:str=Depends(oauth_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"user is not authorised to perform this action")
    return verify_token(token,credentials_exception)