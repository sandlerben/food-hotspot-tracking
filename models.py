#from app import db

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Tweet(Base):
    __tablename__ = "Tweet"
    id = Column(Integer, primary_key=True)
    html = Column(String)
    lon = Column(String)
    lat = Column(String)

    def coord (self):
        return (self.lon, self.lat)

    def __repr__(self):
        return '<Tweet %r>' % (self.id)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///tweets.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
