from flask import Flask, render_template, jsonify,session
from flask_oauth import OAuth

app = Flask(__name__)

@app.route('/')
def page():
	#return render_template('base.html')
	return get_tweets()

def get_tweets():
	oauth = OAuth()
	twitter = oauth.remote_app('twitter',base_url='https://api.twitter.com/1.1/',request_token_url='https://api.twitter.com/oauth/request_token',access_token_url='https://api.twitter.com/oauth/access_token',authorize_url='https://api.twitter.com/oauth/authenticate',consumer_key='MH1GPY8XpYgT9P5zVlWeDjHaQ',consumer_secret='cmq6yblCsQiXD9LVwKK7Xh5DcZTA3fwlNPykWMzVegDMOWMkAm')

	# session['twitter_token'] = (
 #        '2835780022-2UlRmdzQLVbel8qr2RiQsDzPnSOhUBqW8JYmIoE',
 #        't7mHe7nZqPO1y9dz5tLQRQFcXJZlB4h5MUfi2pdPdO0pg'
 #    )

	@twitter.tokengetter
	def get_twitter_token(token=None):
		return None
	    #return session.get('twitter_token')

	resp = twitter.get('search/tweets.json', data = {
		'q': 'hungry',
		'geocode': '1,38,500km'
		})

	if resp.status == 200:
		tweets = resp.data
	else:
		tweets = None
		flash('whoops - couldn\'t get tweets :(')


	return tweets



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9393, debug=True)
