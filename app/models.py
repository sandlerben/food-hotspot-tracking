from app import db

class AllTweets(db.Model):
    tweets_dict = db.Column(db.Blob())
    tweets_html = db.Column(db.Blob())
    tweets_coords = db.Column(db.Blob())

    def __repr__(self):
        return '<Tweet %r>' % (self.tweets_dict)