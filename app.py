from flask import Flask, render_template, jsonify
from flask_oauth import OAuth

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9393, debug=True)

@app.route('/')
def page():
    return render_template('base.html')
    # return get_tweets()

# def get_tweets():
#     twitter = oauth.remote_app(
#         'twitter', 
#         base_url='https://api.twitter.com/1.1/',
#         request_token_url='https://api.twitter.com/oauth/request_token',
#         access_token_url='https://api.twitter.com/oauth/access_token',
#         authorize_url='https://api.twitter.com/oauth/authenticate',
#         consumer_key='YvNbcy4KN9tzndKL0GvVAQMGA',
#         consumer_secret='NNsRAUo9D7RgtDbg2ksZIwfJfUszOHXPiBoLLC87TTu61p0Ejx'
#     )

#     resp = twitter.get('search/tweets.json', data = {
#         q: 'hungry',
#         geocode: '1,38,500km'
#         })

#     if resp.status == 200:
#         tweets = resp.data
#     else:
#         tweets = None
#         flash('whoops - couldn\'t get tweets :(')

#     print resp.status

#     # return tweets
