#!/usr/bin/python3
""" model base """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """ constructor """

        if kwargs:
            """ dictionary representation """
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            """ new instance """
            self.id = str(uuid4())
            self.update_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """" return de representation of the instance """
        nameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(nameClass, self.id, self.__dict__)

    def save(self):
        """ save the changes and update the date """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dictionary """
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update({'created_at': self.created_at.isoformat()})
        dictionary.update({'update_at': self.update_at.isoformat()})
        return dictionary
