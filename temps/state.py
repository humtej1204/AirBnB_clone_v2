#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="cities", cascade="all, delete")
    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id
            equals to the current State.id"""
            from models.__init__ import storage
            from models.city import City
            list_cities = [filter(
                lambda c: c.state_id == self.id,
                storage.all(City).values()
            )]
            return list_cities

