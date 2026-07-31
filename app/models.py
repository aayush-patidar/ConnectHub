from .database import Base

from sqlalchemy import Column,String,Integer,TIMESTAMP,text,Text,ForeignKey

class Users(Base):
    __tablename__="Users"
    id=Column(Integer,autoincrement=True,index=True,primary_key=True,nullable=False)
    username=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    bio=Column(Text,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

class Posts(Base):
    __tablename__="Posts"
    id=Column(Integer,autoincrement=True,index=True,primary_key=True,nullable=False)
    content=Column(Text,nullable=False)
    user_id=Column(Integer,ForeignKey("Users.id",ondelete="CASCADE"),nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

class Likes(Base):
    __tablename__="Likes"
    id=Column(Integer,autoincrement=True,index=True,primary_key=True,nullable=False)
    user_id=Column(Integer,ForeignKey("Users.id",ondelete="CASCADE"),nullable=False)
    post_id=Column(Integer,ForeignKey("Posts.id",ondelete="CASCADE"),nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

    

