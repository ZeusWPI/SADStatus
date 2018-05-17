from .app import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    url = db.Column(db.String(1024), unique=True, nullable=False)
    # Broken since if now broken, else last date thing was broken
    broken_since = db.Column(db.DateTime)
    last_checked = db.Column(db.DateTime)
    online = db.Column(db.Boolean)

    def __repr__(self):
        return '<Service %r>' % self.name

    def __init__(self, name, url):
        super(self.__class__, self).__init__()
        self.name = name
        self.url = url
