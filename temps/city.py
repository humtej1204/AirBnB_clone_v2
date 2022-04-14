#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
"""SQLAlchemy Modules"""
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    __tablename__ = 'cities'
    """ The city class, contains state ID and name """
    state_id = Column(String(60), nullable=False, ForeignKey(states.id))
    name = Column(String(128), nullable=False)
