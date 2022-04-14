#!/usr/bin/python3
from os import getenv
""" City Module for HBNB project """
from models.base_model import BaseModel, Base

"""SQLAlchemy Modules"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    __tablename__ = 'cities'
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ""
        name = ""
