from pydantic import BaseModel
from datetime import datetime
from typing import List
from ..infra.models.models import Post


class UserBase(BaseModel):
    username: str
    email: str
    

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    description: str | None = None
    text: str

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
