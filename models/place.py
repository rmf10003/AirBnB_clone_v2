#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, Column, String
from models.base_model import Integer
from sqlalchemy import Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

# place_amenity = Table('place_amenity', Base.metadata,
#                         Column('place_id', String(60),
#                             ForeignKey('places.id'), nullable=False),
#                         Column('amenity_id', String(60),
#                             ForeignKey('amenities.id'), nullable=False))

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship(
            'Review', back_populates='place',
            cascade='all, delete, delete-orphan'
        )
        
        user = relationship(
            'User', back_populates='places'
        )
        # amenities = relationship(
        #     'Amenity', secondary=place_amenity,
        #     viewonly=False, back_populates='place_amenities')
        cities = relationship(
            'City', back_populates='places')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter for review return list of reviews."""
            reviews_inst = []
            reviews_dict = models.storage.all('Review')
            for key, value in reviews_dict.items():
                if self.id == value.place_id:
                    reviews_inst.append(value)
            return reviews_inst

    # @property
    # def amenities(self):
    #     """getter for amenities returns list of amenity instanc"""
    #     return self.amenity_ids
    
    # @amenities.setter
    # def amenities(self, obj):
    #     """setter for amenities"""
    #     if isinstance(obj, Amenity):
    #         self.amenity_ids.append(obj.id)
