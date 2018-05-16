from tinydb import TinyDB, Query
from datetime import datetime

import urllib.request

db = TinyDB("services.db")

def check():
    db = TinyDB("services.db")
    query = Query()
    items = db.search(query.name != "")
    for service in items:
        online = checkonline(service["url"])
        query = Query()
        if (not online):
            db.update({"last_broken": int(datetime.now().timestamp())}, query.name == service["name"])
        db.update({"last_checked": int(datetime.now().timestamp()), "online": online}, query.name == service["name"])
    return db.all()

def checkonline(url):
    try:
        return urllib.request.urlopen(url).getcode() == 200
    except Exception as e:
        return False

def addService(name, url):
    db.insert(
        {
            "name": name,
            "url": url,
            "last_broken": 0,
            "last_checked": 0,
            "online": False
        }
    )

