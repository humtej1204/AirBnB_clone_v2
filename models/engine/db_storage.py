#!/usr/bin/python3
""" new class for sqlAlchemy """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Initialization Constructor
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        sqlEnv = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if sqlEnv == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a list of obj (dictionary)
        Return:
            returns a dictionary of __object
        """
        all_dict = {}
        for i in classes:
            if cls is None or cls == i:
                my_objs = self.__session.query(classes[i]).all()
                for obj in my_objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    all_dict[key] = obj
        return (all_dict)

    def new(self, obj):
        """ añadir un nuevo elemento en la tabla
        """
        self.__session.add(obj)

    def save(self):
        """ confirmar todos los cambios de
        la sesión actual de la base de datos
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Eliminar un elemento de la tabla
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        crea todas las tablas en la base de datos
        crea la sesión de base de datos actual
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        Closes Session
        """
        self.__session.close()
