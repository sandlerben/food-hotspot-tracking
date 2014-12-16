from app import app, db

class Tweet(db.Model):
    #__tablename__ = "Tweet"
    id = db.Column(db.BigInteger, primary_key=True)
    lon = db.Column(db.String)
    lat = db.Column(db.String)
    html = db.Column(db.String)
    locs = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def coord (self):
        return (self.lon, self.lat)
