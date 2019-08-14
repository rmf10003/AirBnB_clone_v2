#!/usr/bin/python3
"""module for database storage class for AirBnB"""
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Amenity": Amenity, "City": City, "Place": Place,
            "Review": Review, "State": State, "User": User}

class DBStorage:
    """This class stores user data into our db"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage instances
        """
#the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db): 6.)
    HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
    HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
    HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
    HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
    HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
                                        .format(HBNB_MYSQL_USER,
                                                HBNB_MYSQL_PWD,
                                                HBNB_MYSQL_HOST,
                                                HBNB_MYSQL_DB),
                                                pool_pre_ping=True)
        if HBNB_ENV == 'test':
            #drop all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' Query on current DB session '''
        new_dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                obj = self.__session.query(classes[c]).all()
                for o in obj:
                    key = o.__class__.__name__ + '.' + o.id
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
        Base.metadata.create_all(self.__engine)
        sessLoad = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessLoad)
        self.__session = Sessionf close(self):
        ''' calls remove() method on private session att '''
        self.__session.remove()