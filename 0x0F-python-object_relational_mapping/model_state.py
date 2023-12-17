#!/usr/bin/python3
'''Write a python file that contains the class definition of a State'''


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''this is class'''

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincremet=True)
    name = Column(String(128), nullable=False)
