#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
class State:
    Base = declarative_base():
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
    
