from flask import Flask, render_template, jsonify,session
from flask_oauth import OAuth

app = Flask(__name__)

@app.route('/')
def page():
	#return render_template('base.html')
	return get_tweets()

def get_tweets():
	oauth = OAuth()
	twitter = oauth.remote_app('twitter',base_url='https://api.twitter.com/1.1/',request_token_url='https://api.twitter.com/oauth/request_token',access_token_url='https://api.twitter.com/oauth/access_token',authorize_url='https://api.twitter.com/oauth/authenticate',consumer_key='YvNbcy4KN9tzndKL0GvVAQMGA',consumer_secret='NNsRAUo9D7RgtDbg2ksZIwfJfUszOHXPiBoLLC87TTu61p0Ejx')

	session['twitter_token'] = (
        '821931824-uOlM9gUpj14OcuMbY2QXU13Zntt2eNQgui5cquFo',
        'f3S676wxZp3Z8xGjiS4ismqGBgtN1VcmNEWnrci1XOaMU'
    )

	@twitter.tokengetter
	def get_twitter_token(token=None):
	    return session.get('twitter_token')

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
