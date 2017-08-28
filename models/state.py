#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """State class handles all application states"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
      __tablename__ = 'states'
      name = Column(String(128), nullable=False)
      cities = relationship("City", backref='state', cascade="delete, delete-orphan")

    else:
        name = ''

        def cities(self):
            cities = relationship("City", backref='state', cascade="delete, delete-orphan")
            return cities

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
