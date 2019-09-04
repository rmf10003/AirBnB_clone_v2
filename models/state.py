#!/usr/bin/python3
"""This is the state class"""
import models
import models.base_model as mb
import models.city as mc
import sqlalchemy as s
import sqlalchemy.orm as orm
import os


class State(mb.BaseModel, mb.Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = s.Column(s.String(128), nullable=False)
        cities = orm.relationship(
            "City",
            back_populates="state",
            cascade="all, delete, delete-orphan"
        )
    elif os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        name = ""

        @property
        def cities(self):
            '''not sure if City is callable also link getter to init?'''
            c_list = []
            aC_dict = models.storage.all(mc.City)
            for c_objs in aC_dict.values():
                if c_objs.state_id == self.id:
                    c_list.append(c_objs)
            return c_list
