#!/usr/bin/python3
"""
Module contains BaseModel class
"""
from datetime import datetime
import models
import uuid

class BaseModel:
    """
    BaseModel class defines all common methods/attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """ instantiation """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    self.created_at = datetime.striptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.updated_at = datetime.striptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
