#!/usr/bin/python3
"""
module for a script that adds the State object "Louisian"
to the database hbtn_0e_6_usa
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

    session.add(State(name="Louisian"))
    session.commit()

    state = session.query(State).filter_by(name="Louisian").first()
    print(state.id)

    session.close()
