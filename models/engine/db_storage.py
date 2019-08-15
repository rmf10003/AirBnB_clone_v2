#!/usr/bin/python3
"""module for database storage class for AirBnB"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session




class DBStorage:
    """ class for DBstorage """
    __engine = None
    __session = None
    classes = {'State': State, 'City': City,
               'User': User, 'Amenity': Amenity,
               'Place':Place, 'Review': Review}

    def __init__(self):
        """constructor for DBStorage instances
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(HBNB_MYSQL_USER,
                                                HBNB_MYSQL_PWD,
                                                HBNB_MYSQL_HOST,
                                                HBNB_MYSQL_DB),
                                                pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' Query on current DB session '''
        new_dict = {}
        for class_name in self.classes.keys():
            if cls is None or cls == class_name:
                obj_list = self.__session.query(self.classes[class_name]).all()
                for obj in obj_list:
                    #not sure if key is correct
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)


    def new(self, obj):
        ''' adds objects to current DB session '''
        self.__session.add(obj)

    def save(self):
        ''' commits all changes to
         current DB '''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes obj from current session if not none obj '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        ''' reloads data from DB '''
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
