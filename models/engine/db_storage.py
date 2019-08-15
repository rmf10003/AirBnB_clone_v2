#!/usr/bin/python3
"""module for database storage class for AirBnB"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
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
        print("butthole2\n\n\n\n\n")
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' Query on current DB session '''
        new_dict = {}
        for c in models.classes.keys():
            print("yolo mofo {}\n\n".format(c))
            if cls is None or cls is c:
                obj = self.__session.query(models.classes[c]).all()
                for o in obj:
                    #not sure if key is correct
                    key = c + '.' + o.id
                    new_dict[key] = o
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
        print("butthole\n\n\n\n\n")
        print("{}".format(type(self.__engine)))
        Base.metadata.create_all(self.__engine)
        print("butthole\n\n\n\n\n")
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        print("butthole\n\n\n\n\n")
        self.__session = Session()
        print("butthole\n\n\n\n\n")
