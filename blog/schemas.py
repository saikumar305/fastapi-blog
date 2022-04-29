from pydantic import BaseModel
from typing import List, Optional,Any

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    created: Any

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    fullname: Optional[str] = None
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True