#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String, getenv
from sqlalchemy.orm import relationship

class User(BaseModel):
    """User class handles all application users"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place',
                              back_populates='user',
                              cascade='delete')
        reviews = relationship('Review',
                               back_populates='user',
                               cascade='delete')

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
