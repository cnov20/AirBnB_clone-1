#!/usr/bin/python3

"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""

from models.base_model import BaseModel, Base
from models import base_model, amenity, city, place, review, state, user
from os import getenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    __engine =  None
    __session = None

    def __init_(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")))
        self.__models_available = {"User": Users,
                                   "Amenity": Amenity, "City": City,
                                   "Place": Place, "Review": Review,
                                   "State": State}
        if getenv("HBNB_MYSQL_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_orm = {}
        if cls in self.__models_available:
            for s in self.__session.query(
                    self.__models.get(cls)):
                obj_orm[s.__dict__["id"]] = s
        return obj_orm

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.remove()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
