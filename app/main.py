from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users,login,posts

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(users.router)
app.include_router(login.router)
app.include_router(posts.router)