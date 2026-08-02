from fastapi import FastAPI,APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,oauth2

router=APIRouter(
    prefix="/like",
    tags=["Likes"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(like:schemas.Like,db:Session=Depends(get_db),current=Depends(oauth2.get_user)):
    check=db.query(models.Likes).filter(models.Likes.id==like.post_id,models.Likes.user_id==current.id)
    found_vote=check.first()
    if (like.flag==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"User has already voted")

        new_vote=models.Likes(post_id=like.post_id,user_id=current.id)
        db.add(new_vote)
        db.commit()
        return {"msg":"successfully added vote"}

    else:

        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"vote does not exist")

        check.delete()
        db.commit()
        return {"msg":"successfully deleted vote"}
