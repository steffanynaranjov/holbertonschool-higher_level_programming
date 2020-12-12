#!/usr/bin/python3
"""
all the states
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = "mysql+mysqldb://{}:{}@localhost/{}"

    engine = create_engine(
        engine.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    for stat, cit in row:
        print('{}: ({}) {}'.format(stat.name, cit.id, cit.name))

    session.close()
