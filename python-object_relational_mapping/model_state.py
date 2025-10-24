#!/usr/bin/python3
"""model_state.py
Creation of the class state for SQLAlchemy in order to use ORM"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    '''Class that represents the table states in a database'''
    __tablename__ = 'states'
    id = Column('states.id', Integer, primary_key=True, autoincrement=True)
    name = Column('states.name', String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
