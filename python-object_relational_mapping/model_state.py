#!/usr/bin/python3
"""model_state.py
Creation of the class state for SQLAlchemy in order to use ORM"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Class that represents the table states in a database'''
    __tablename__ = 'states'
    id = Column('states.id', Integer, primary_key=True, autoincrement=True)
    name = Column('states.name', String(128), nullable=False)
