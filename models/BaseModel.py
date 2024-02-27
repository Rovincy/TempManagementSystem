#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class BaseModel:
    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        return self.__str__()

    def save(self):
        models.storage.new(self)  # if it already exists, it will update it, cos primary key is unique
        models.storage.save()


    def delete(self):
        models.storage.delete(self)
