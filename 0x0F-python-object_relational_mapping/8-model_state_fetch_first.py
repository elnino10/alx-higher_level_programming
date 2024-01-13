#!/usr/bin/python3
"""
module for a script that prints the first State object
from the database hbtn_0e_6_usa
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    DATABASE_URI = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(DATABASE_URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id)[0]
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("")

    session.close()
