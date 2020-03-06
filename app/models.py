from datetime import datetime
from .app import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    url = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=True)
    # Broken since if now broken, else last date thing was broken
    broken_since = db.Column(db.DateTime)
    last_checked = db.Column(db.DateTime, default=datetime.fromtimestamp(0), nullable=False)
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Service %r>' % self.name

    def __init__(self, name, url, username, password):
        super()
        self.name = name
        self.url = url
        self.username = username
        self.password = password
