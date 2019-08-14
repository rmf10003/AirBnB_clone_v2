#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    #only for db storage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            c_list = []
            #not sure if City is callable
            #link getter to init?
            aC_dict = models.storage.all(City)
            for c_objs in aC_dict.values():
                if c_objs.state_id == self.id:
                    c_list.append(c_objs)
            return c_list
