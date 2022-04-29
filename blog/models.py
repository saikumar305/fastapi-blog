from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, index=True)
    password = Column(String(128))
    fullname = Column(String(50))
    email = Column(String(50))
    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return "<User(username='%s')>" % self.username

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(1000))
    created = Column(DateTime, default=datetime.datetime.now())
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return "<Post(title='%s')>" % self.title