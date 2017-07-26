#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String, getenv
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """State class handles all application states"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
      __tablename__ = 'states'
      name = Column(String(128), nullable=False)
      cities = relationship("City", back_populates='state', cascade="delete, delete-orphan")

    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
