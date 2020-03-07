#!/usr/bin/env python3

from app.app import db, models

db.create_all()

    # Display name: (url, username, password)
services = {
    "Website": ("https://zeus.ugent.be/", None, None),
    "Haldis": ("https://haldis.zeus.gent", None, None),
    "Tab": ("https://tab.zeus.gent", None, None),
    "Tap": ("https://tap.zeus.gent", None, None),
    "Cammie": ("https://zeus.ugent.be/cammie", None, None),
    "Wiki": ("https://zeus.ugent.be/wiki", None, None),
    "Gamification": ("https://zeus.ugent.be/game", None, None),
    "Mattermost": ("https://mattermost.zeus.gent", None, None),
    "Cammiechat": ("https://kelder.zeus.ugent.be/messages/", None, None),
    "Cat": ("https://cat.zeus.gent", None, None),
}

for name, (url, username, password) in services.items():
    db.session.add(models.Service(name, url, username, password))
db.session.commit()
