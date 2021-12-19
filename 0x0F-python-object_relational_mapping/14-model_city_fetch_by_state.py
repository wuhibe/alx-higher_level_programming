#!/usr/bin/python3
""" print all city objects """

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sessionmaker = sessionmaker(bind=engine)
    session = Sessionmaker()
    for ci, st in session.query(City, State).filter(City.state_id == State.id):
        print("{:s}: ({:d}) {:s}".format(st.name, ci.id, ci.name))
    session.close()
