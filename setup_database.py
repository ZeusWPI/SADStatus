#!/usr/bin/env python3

from sadstatus.app import db, models

db.create_all()

services = {
    "Website": "https://zeus.ugent.be/",
    "Haldis": "https://zeus.ugent.be/haldis",
    "Tab": "https://zeus.ugent.be/tab",
    "Tap": "https://zeus.ugent.be/tap",
    "Cammie": "https://zeus.ugent.be/cammie",
    "Slotmachien": "https://kelder.zeus.ugent.be/slotmachien"
}

for name, url in services.items():
    db.session.add(models.Service(name, url))
db.session.commit()
