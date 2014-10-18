from flask import Flask, render_template, jsonify, session, flash
from flask_oauth import OAuth
import json, models
from datetime import datetime
from models import Tweet
from models import dbsession
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.secret_key = 't\xea\x85B\xda&\xc3\xdf\x9c\x8f=\xf7\xfa\xa0\xe6\xd3\xf7\x899\xdf\xc0\xdb\x7f<'

@app.route('/')
def page():
	return render_template('splash.html')

@app.route('/app')
def map():
	#return render_template('base.html')
	#return jsonify(**get_tweets())
	# for status in statuses:
	# html_list.append(get_tweet_html(status["id"]))
	all_tweets = dbsession.query(Tweet).all()
	return render_template('base.html',all_tweets=all_tweets)

@app.route('/refresh')
def refresh():
	tweets_dict = get_tweets()
	statuses = tweets_dict["statuses"]
	html_list = []
	for status in statuses:
		print status
		#html_list.append(get_tweet_html(status["id"])) #get_tweet_html(status["id"]
		if(status['geo']):
			tweet = Tweet(html="a", lat = status['geo']['coordinates'][0], lon=status['geo']['coordinates'][1], timestamp=datetime.now())
		else:
			tweet = Tweet(html="a", lat = "", lon="", timestamp=datetime.now())
		dbsession.add(tweet)
	
	dbsession.commit()







	return jsonify(**tweets_dict)

def get_tweets():
	oauth = OAuth()
	twitter = oauth.remote_app('twitter',base_url='https://api.twitter.com/1.1/',request_token_url='https://api.twitter.com/oauth/request_token',access_token_url='https://api.twitter.com/oauth/access_token',authorize_url='https://api.twitter.com/oauth/authenticate',consumer_key='MH1GPY8XpYgT9P5zVlWeDjHaQ',consumer_secret='cmq6yblCsQiXD9LVwKK7Xh5DcZTA3fwlNPykWMzVegDMOWMkAm')

	session['twitter_token'] = (
		'2835780022-2UlRmdzQLVbel8qr2RiQsDzPnSOhUBqW8JYmIoE',
		't7mHe7nZqPO1y9dz5tLQRQFcXJZlB4h5MUfi2pdPdO0pg'
	)

	@twitter.tokengetter
	def get_twitter_token(token=None):
		return session.get('twitter_token')

	resp = twitter.get('search/tweets.json', data = {
		'q': 'hungry',
		'geocode': '1,38,500km',
		'result_type': 'mixed',
		'count':'50',
		})

	if resp.status == 200:
		tweets = resp.data
	else:
		tweets = None
		flash('whoops - couldn\'t get tweets :(')


	return tweets

def get_tweet_html(id):
	oauth = OAuth()
	twitter = oauth.remote_app('twitter',base_url='https://api.twitter.com/1.1/',request_token_url='https://api.twitter.com/oauth/request_token',access_token_url='https://api.twitter.com/oauth/access_token',authorize_url='https://api.twitter.com/oauth/authenticate',consumer_key='MH1GPY8XpYgT9P5zVlWeDjHaQ',consumer_secret='cmq6yblCsQiXD9LVwKK7Xh5DcZTA3fwlNPykWMzVegDMOWMkAm')

	session['twitter_token'] = (
		'2835780022-2UlRmdzQLVbel8qr2RiQsDzPnSOhUBqW8JYmIoE',
		't7mHe7nZqPO1y9dz5tLQRQFcXJZlB4h5MUfi2pdPdO0pg'
	)

	@twitter.tokengetter
	def get_twitter_token(token=None):
		return session.get('twitter_token')

	resp = twitter.get('statuses/oembed.json', data = {
		'id': id
		})
	if resp.status == 200:
		tweet_html = resp.data
	else:
		tweet_html = None
		flash('whoops - couldn\'t get tweets :(')

	return tweet_html['html']

def extract_geodata(statuses):
	coordinate_list = []
	for status in statuses:
		if(status['geo'] is not None):
			coordinate_list.append(status['geo']['coordinates'])
	return coordinate_list

def user_locations(statuses):
	loc_list = []
	for status in statuses:
		loc_list.append(status['user']['location'])
	return loc_list

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9393, debug=True)
	app.config.from_object('config')
