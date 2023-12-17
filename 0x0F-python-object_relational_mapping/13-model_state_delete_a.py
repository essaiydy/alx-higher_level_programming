#!/usr/bin/python3
'''Write a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa'''

import re
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    Session = session()
    paterne = r'.*a.*'
    rows = Session.query(State).all()

    for row in rows:
        if re.match(paterne, row.name):
            Session.delete(row)
    
    Session.commit()
