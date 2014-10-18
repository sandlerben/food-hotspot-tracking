from app import db

class AllTweets(db.Model):
    tweets_dict = db.Column(db.Blob())
    tweets_html = db.Column(db.Blob())
    tweets_coords = db.Column(db.Blob())

    def __repr__(self):
        return '<Tweet %r>' % (self.tweets_dict)


from sqlalchemy.types import TypeDecorator, VARCHAR
import json

class JSONEncodedDict(TypeDecorator):
    """Represents an immutable structure as a json-encoded string.

    Usage::

        JSONEncodedDict(255)

    """

    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value