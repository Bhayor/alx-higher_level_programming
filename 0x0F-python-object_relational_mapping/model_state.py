#!/usr/bin/python3
""" contains State class and Base, an instance of declarative_base() """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMD = MetaData()
Base = declarative_base(metadata=myMD)


class State(Base):
    """ Class with id and name attr of each states """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
