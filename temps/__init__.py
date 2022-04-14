#!/usr/bin/python3
import os

"""Environmental Variable"""
store = os.getenv("HBNB_TYPE_STORAGE")

if store == "db":
    """This module instantiates an object of class DBStorage"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    """This module instantiates an object of class FileStorage"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
