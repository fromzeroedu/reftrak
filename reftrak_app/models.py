from datetime import datetime

from application import db

class RedirectList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True, index=True)
    url = db.Column(db.String(255), index=True)
    description = db.Column(db.String(64), index=True)

    def __init__(self, code, url, description=None):
        self.code = code
        self.url = url
        self.description = description

    def __repr__(self):
        return '<Redirect %s>' % self.id

class RedirectLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), index=True)
    referrer = db.Column(db.String(255), index=True)
    code = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime(), index=True)

    def __init__(self, ip, referrer, code, timestamp=datetime.utcnow()):
        self.ip = ip
        self.referrer = referrer
        self.code = code
        self.timestamp = timestamp

    def __repr__(self):
        return '<RedirectLog %s>' % self.id
