#!/usr/bin/python3
'''Write a script that lists all State objects that 
contain the letter a from the database hbtn_0e_6_usa'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    rows = session().query(State).filter(State.name=='%a%')

    for row in rows:
        print("{}: {}".format(row.id, row.name))
