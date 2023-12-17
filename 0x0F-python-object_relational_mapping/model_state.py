#!/usr/bin/python3
'''Write a python file that contains the class definition of a State'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):

    __tablename__ = 'states'

     id = Column(Integer, primary_key=True)
     name =  Column(String(128), nullable=False)

     engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
             .format("root", "root", "hbtn_0e_4_usa"), pool_pre_ping=True)

     Base.metadata.create_all(engine)
