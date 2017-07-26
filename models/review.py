#!/usr/bin/python3
"""
Review Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, String, ForeignKey, getenv


class Review(BaseModel):
    """Review class handles all application reviews"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)


    else:
        place_id = ''
        user_id = ''
        text = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
