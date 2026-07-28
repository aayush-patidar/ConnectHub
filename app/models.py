from .database import Base

from sqlalchemy import Column,String,Integer,TIMESTAMP,text,Text

class Users(Base):
    __tablename__="Users"
    id=Column(Integer,autoincrement=True,index=True,primary_key=True,nullable=False)
    username=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    bio=Column(Text,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))