from pydantic import BaseModel,EmailStr,Field
from datetime import datetime

class NewUser(BaseModel):
    username:str
    email:EmailStr
    password:str=Field(min_length=6,max_length=12)
    bio:str

class UserRespo(BaseModel):
    username:str
    created_at:datetime

class Login(BaseModel):
    email:EmailStr
    password:str=Field(min_length=6,max_length=12)

class TokenRespo(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:int
    email:EmailStr


