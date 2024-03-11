from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
Base = declarative_base()


class BaseModel:
    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        self.id = uuid.uuid4()
        self.created_at = self.updated_at = datetime.now()


    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()
