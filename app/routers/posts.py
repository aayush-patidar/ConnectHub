from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models,schemas,oauth2
from ..database import get_db

router=APIRouter(
    prefix="/post",
    tags=["Posts"]
)

@router.post("/",response_model=schemas.PostRespo,status_code=status.HTTP_201_CREATED)
def newPost(post:schemas.NewPost,db:Session=Depends(get_db),current=Depends(oauth2.get_user)):
    post=models.Posts(user_id=current.id,**post.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post

@router.get("/",response_model=List[schemas.PostRespo])
def get_post(db:Session=Depends(get_db),current=Depends(oauth2.get_user)):
    user=db.query(models.Posts).filter(models.Posts.user_id==current.id).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Post Found for this {current.id}")

    return user

@router.delete("/{id}")
def del_post(id:int,db:Session=Depends(get_db),current=Depends(oauth2.get_user)):
    post=db.query(models.Posts).filter(models.Posts.id==id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post not found with this post id")

    if post.first().user_id!=current.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"you are not authorised to perform this action")

    post.delete()
    db.commit()
    return {"msg":"Post Deleted successfully"}

@router.put("/{id}",response_model=schemas.PostRespo)
def upd_post(newpost:schemas.NewPost,id:int,db:Session=Depends(get_db),current=Depends(oauth2.get_user)):
    post=db.query(models.Posts).filter(models.Posts.id==id)

    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not exist")

    if post.first().user_id!=current.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"you are not authorised to perform this action")

    updated_post=post.update(newpost.model_dump())
    db.commit()

    new_updated=db.query(models.Posts).filter(models.Posts.id==id).first()

    return new_updated




