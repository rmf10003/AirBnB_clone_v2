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


class DBStorage:
    """This class stores user data into our db"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage instances
        """
#the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db): 6.)
HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == test:
            #drop all tables
            Base.metadata.drop_all(self.__engine)
