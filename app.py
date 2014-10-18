from flask import Flask, render_template, jsonify, session
from flask_oauth import OAuth

app = Flask(__name__)

app.secret_key = 't\xea\x85B\xda&\xc3\xdf\x9c\x8f=\xf7\xfa\xa0\xe6\xd3\xf7\x899\xdf\xc0\xdb\x7f<'

@app.route('/write')
def write():
	tweets_dict = {
	'tweet' : { 'html': 'abcd', 'coords': 11.1111111, 1.1111111},
	'tweet' : { 'html': 'efgh', 'coords': 32.6027461, 2.2222222}
	}
	tweets_html = models.AllTweets.query.all('html')
	tweets_coords = models.AllTweets.query.all('coords')
	u = models.AllTweets(tweets_dict, tweets_html, tweets_coords)
	db.session.add(u)
	db.session.commit()

@app.route('/display')
def display():
	tweets_dict
	models.AllTweets.query.all('tweets_dict')
	models.AllTweets.query.all('tweets_html')
	models.AllTweets.query.all('tweets_coords')


@app.route('/')
def page():
	#return render_template('base.html')
	#return jsonify(**get_tweets())
	tweets_dict = get_tweets()
	statuses = tweets_dict["statuses"]
	html_list = []
	for status in statuses:
		html_list.append(get_tweet_html(status["id"]))
	return render_template('base.html',html_list=html_list,geodata=extract_geodata(statuses))

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

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9393, debug=True)
