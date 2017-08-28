#!/usr/bin/python3

"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:

    __engine = None
    __session = None

    """handles long term storage of all class instances"""

    CNC = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")))

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):

        ''' models_available = ["User", "State", "City", "Amenity",
        "Place", "Review"] '''

        obj_orm = {}
        if cls is None:
            for key, val in self.CNC.items():
                for query in self.__session.query(val):
                    obj_orm[query.id] = query

        else:
            for query in self.__session.query(self.CNC[cls]):
                obj_orm[query.id] = query

        return obj_orm

    def new(self, obj):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        '''        Session = sessionmaker(bind=self.__engine) '''
        self.__sesssion = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session.remove()
