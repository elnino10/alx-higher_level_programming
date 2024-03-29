#!/usr/bin/python3
"""Defines City."""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Defines the cities table."""
    __tablename__ = 'cities'
    id = Column(
        Integer, primary_key=True,
        nullable=False,
        autoincrement="auto",
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
