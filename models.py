from app import db

class Tweet(db.Model):
    tweets_dict = db.Column(db.Blob(), primary_key=True)

    def __repr__(self):
        return '<Tweet %r>' % (self.tweets_dict)