import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    follower = relationship("Follower", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("user.id"))
    media = relationship("Media", back_populates="post")

   
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer(), primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="follower")



class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer(), primary_key=True)
    type = Column(Enum(), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer(), ForeignKey("post.id"))
    post = relationship("Post", back_populates="media")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer(), primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer(), ForeignKey("user.id"))
    post_id = Column(Integer(), ForeignKey("post.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
