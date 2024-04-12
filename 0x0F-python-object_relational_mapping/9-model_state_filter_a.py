#!/usr/bin/python3
""" lists states with the letter 'a' """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchmey.orm import sessionmaker

if __name__ = "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).filter(state.name.like('%a%'))
    for instance in instances:
        print(instance.id, instance.name, sep=": ")
