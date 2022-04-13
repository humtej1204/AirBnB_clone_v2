#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import shlex
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """ Devuelve la lista de instancias de Ciudad con
        state_id == State.id actual
        """
        var = models.storage.all()
        my_list = []
        my_obj = []
        for key in var:
            city = key.split('.', '')
            city = shlex.split(city)
            if (city[0] == 'City'):
                my_list.append(var[key])
        for items in my_list:
            if (items.state_id == self.id):
                my_obj.append(items)
        return(my_obj)
