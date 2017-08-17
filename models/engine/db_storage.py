#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models import base_model, amenity, city, place, review, state, user
from os import getenv
from sqlalchemy import (create_engine, func)
from sqlalchemy.orm import (scoped_session, sessionmaker)
from datetime import datetime

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json

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
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        obj_orm = {}
        if cls in self.__models:
            for s in self.__session.query(
                    self.__models.get(cls)):
                obj_orm[s.__dict__["id"]] = s
        return obj_orm

class FileStorage:
    """handles long term storage of all class instances"""
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './dev/file.json'
    __objects = {}

    def all(self):
        """returns private attribute: __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)

    def delete_all(self):
        """deletes all stored objects, for testing purposes"""
        del FileStorage.__objects
        FileStorage.__objects = {}
        self.save()
