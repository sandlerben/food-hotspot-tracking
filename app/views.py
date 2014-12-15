from flask import Flask, render_template, jsonify, session, flash
from app import app, db
from flask_oauth import OAuth
# import os
# import json, models
from datetime import datetime
from pytz import timezone
from models import Tweet
# from models import dbsession
# from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/')
def page():
	return render_template('splash.html')

@app.route('/app')
def application():
	all_tweets = Tweet.query.all()
	most_recent_tweets = Tweet.query.order_by(Tweet.timestamp.desc()).limit(50)
	return render_template('base.html',all_tweets=all_tweets,most_recent_tweets=most_recent_tweets)

# Refreshes contents of database
@app.route('/refresh')
def refresh():
	tweets_dict = get_tweets()
	statuses = tweets_dict["statuses"]
	html_list = []
	eastern = timezone('US/Eastern')
	for status in statuses:
		#html_list.append(get_tweet_html(status["id"])) #get_tweet_html(status["id"]
		id_str = status["id"]
		if(status['geo']):
			tweet = Tweet(id = id_str, html=get_tweet_html(id_str), lat = status['geo']['coordinates'][0], lon=status['geo']['coordinates'][1], locs = status['user']['location'], timestamp=datetime.now(eastern))
		else:
			tweet = Tweet(id = id_str, html=get_tweet_html(id_str), lat = "", lon="", locs = status['user']['location'], timestamp=datetime.now(eastern))
		db.session.merge(tweet)
	
	db.session.commit()
	return jsonify(**tweets_dict)

# Load tweets from twitter
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

	# Search for tweets containing these words
	queries = ['mihogo','cassava','njaa','chakula ghali','hakuna chakula','enough food','expensive food','no food','mahindi','wali']
	tweets = {}

	resp = twitter.get('search/tweets.json', data = {
			'q': 'hungry',
			'geocode': '1,38,500km',
			'result_type': 'recent',
			'count':'5',
			})

	tweets = resp.data

	for query in queries:
		resp = twitter.get('search/tweets.json', data = {
			'q': query,
			'geocode': '1,38,500km',
			'result_type': 'recent',
			'count':'5',
			})

		if resp.status == 200:
			tweets['statuses'].extend(resp.data['statuses'])
		else:
			tweets = None
			flash('whoops - couldn\'t get tweets :(')

	return tweets

# Get embed html for a tweet by ID
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
		'id': id,
		'hide_media': 'true'
		})
	if resp.status == 200:
		tweet_html = resp.data
	else:
		tweet_html = None
		flash('whoops - couldn\'t get tweets :(')

	return tweet_html['html']
