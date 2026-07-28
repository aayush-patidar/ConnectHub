from fastapi import FastAPI,HTTPException,status,Depends,APIRouter
from .. import models,schemas,oauth2,utils
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post("/",response_model=schemas.TokenRespo)
def login(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    logged_in=db.query(models.Users).filter(models.Users.email==user.username).first()
    if not logged_in:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User does not exist")

    if not utils.verify(user.password,logged_in.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Password not matched")

    data={"id":logged_in.id,"email":logged_in.email}
    token=oauth2.access_token(data)
    return {"access_token":token,"token_type":"bearer"}

