from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import models
from models import customer, employee, order, payment, reservation, review, room
from models.Base import Base

# Load the environment variables from the .env file
load_dotenv()

classes = [customer, employee, order, payment, reservation, review, room]


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        USER_NAME = getenv('USER_NAME')
        SQL_PWD = getenv('SQL_PWD')
        SQL_HOST = getenv('SQL_HOST')
        SQL_DB = getenv('SQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER_NAME, SQL_PWD, SQL_HOST, SQL_DB))

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            return None
        else:
            return self.__session.query(cls).all()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes:
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls:
            if value.id == id:
                return value

        return None

    def count(self, cls):
        """
        count the number of objects in storage
        """
        return len(models.storage.all(cls))
