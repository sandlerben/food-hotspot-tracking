#from app import db

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Date 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tweet(Base):
    __tablename__ = "Tweet"
    id = Column(Integer, primary_key=True)
    lon = Column(String)
    lat = Column(String)
    html = Column(String)
    locs = Column(String)
    timestamp = Column(Date)

    def coord (self):
        return (self.lon, self.lat)

    # def __repr__(self):
    #     return '<Tweet %r %r %r %r %r>' % (self.lon) (self.lat) (self.html) (self.locs) (self.timestamp)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///tweets.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
dbsession = DBSession()
