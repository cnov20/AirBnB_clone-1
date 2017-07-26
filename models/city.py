#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel, Base, Column, Table, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey
from os import getenv


class City(BaseModel):
    """City class handles all application cities"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="city", cascade="all, delete, delete-orphan")
        __mapper_args = {"confirm_deleted_rows": False}
    else:
        name = ''
        state_id = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)

"""    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def place(self):
            return_places = models.storage.all("Place").values()
            end = [place for place in return_places if place.city_id = self.id]
            return end
"""
