#!/usr/bin/env python3

from app.app import db, models

db.create_all()

services = {
    "Website": "https://zeus.ugent.be/",
    "Haldis": "https://haldis.zeus.gent",
    "Tab": "https://tab.zeus.gent",
    "Tap": "https://tap.zeus.gent",
    "Cammie": "https://zeus.ugent.be/cammie",
    "Slotmachien": "https://kelder.zeus.ugent.be/slotmachien",
    "Wiki": "https://zeus.ugent.be/wiki",
    "Gamification": "https://zeus.ugent.be/game",
    "Mattermost": "https://mattermost.zeus.gent",
    "Cammiechat": "https://kelder.zeus.ugent.be/messages"
}

for name, url in services.items():
    db.session.add(models.Service(name, url))
db.session.commit()
