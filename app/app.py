from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
# Supress Flask warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from app import models, checker


@app.route("/")
def message():
    # update
    update_online_status()

    return render_template("status.html", services=models.Service.query.all(), override=False)

@app.route("/happy")
def happy():
    return render_template("status.html", services=models.Service.query.all(), override=True)

def update_online_status():
    last_possible_time = datetime.now() - config.CHECK_INTERVAL
    # Filter by services that haven't been updated for CHECK_INTERVAL
    for service in models.Service.query.filter(models.Service.last_checked < last_possible_time):
        online = checker.is_online(service.url)
        if not online and service.online:
            service.broken_since = datetime.now()
        service.online = online
        service.last_checked = datetime.now()
        db.session.add(service)
    db.session.commit()
