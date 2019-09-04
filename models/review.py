#!/usr/bin/python3
"""This is the review class"""
import models.base_model as mb
import sqlalchemy as s
import sqlalchemy.orm as so
import os as o


class Review(mb.BaseModel, mb.Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = 'reviews'

    if o.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = s.Column(s.String(1024), nullable=False)
        place_id = s.Column(
            s.String(60),
            s.ForeignKey('places.id'),
            nullable=False
        )
        user_id = s.Column(
            s.String(60),
            s.ForeignKey('users.id'),
            nullable=False
        )
        user = so.relationship(
            'User',
            back_populates='reviews'
        )
        place = so.relationship(
            'Place',
            back_populates='reviews'
        )

    else:
        place_id = ""
        user_id = ""
        text = ""
