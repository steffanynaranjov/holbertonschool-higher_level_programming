#!/usr/bin/python3
"""
State Class
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    States table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """
            Return "id: name" of the object
        """
        return "{}: {}".format(self.id, self.name)
