from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Tweet, engine, Base
 
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
session = DBSession()
 
# Insert a Person in the person table
def make_tweet(tweets_dict):
	return Tweet(html=tweets_dict['html'], lon=tweets_dict['lon'], lat=tweets_dict['lat'])

new_tweet_dict = {'html': 'abcd', 'lon': 11.1111111, 'lat': 1.1111111}
new_tweet = make_tweet(new_tweet_dict)

session.add(new_tweet)
session.commit()
 

new_tweet_dict1 = { 'html': 'efgh', 'lon': 32.6027461, 'lat': 2.2222222}
new_tweet1 = make_tweet(new_tweet_dict)
session.add(new_tweet1)
session.commit()
