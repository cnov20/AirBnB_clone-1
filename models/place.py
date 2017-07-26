#!/usr/bin/python3
"""
Place Class from Models Module
"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import ForeignKey, Float, String, Column, Integer
from sqlalchemy.orm import relationship, backref


class PlaceAmenity(Base):
    __tablename__ = 'place_amenity'
    metadata = Base.metadata
    place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
    amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)

class Place(BaseModel):
    """Place class handles all application places"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__="places"

        city_id = Column(String(60),
                     ForeignKey("cities.id"),
                     nullable=False)
        user_id = Column(String(60),
                     ForeignKey("users.id"),
                     nullable=False)
        name = Column(String(60),
                  nullable=False)
        description = Column(String(1024),
                         nullable=False)
        number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
        number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
        max_guest = Column(Integer,
                       default=0,
                       nullable=False)
        price_by_night = Column(Integer,
                            default=0,
                            nullable=False)
        latitude = Column(Float,
                      nullable=True)

        longitude = Column(Float,
                       nullable=True)
        amenities = relationship("Amenity", secondary="place_amenity",
                             backref="places")

        reviews = relationship("Review", backref="place", cascade="delete")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = 0
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenities = ""
        amenity_ids = ['', '']

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)

"""    if getenv("HBNB_TYPE_STORAGE", ) != "db":
        @property
        def reviews(self):
            all_reviews = models.storge.all("Review").values()
            end = [end for end in all_reviews if end.place_id == self.id]
            return end

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            end = []
            for s in self.amenities_id:
                m = models.storage.get("Amenity", i)
                if n is not None:
                    end.append(n)
            return end
"""
