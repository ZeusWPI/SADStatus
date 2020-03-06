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
from .statusenum import Status


@app.route("/")
def message():
    # update
    update_online_status()

    return render_template("status.html", services=models.Service.query.all(), override=False, Status=Status)

@app.route("/happy")
def happy():
    return render_template("status.html", services=models.Service.query.all(), override=True, Status=Status)

def update_online_status():
    last_possible_time = datetime.now() - config.CHECK_INTERVAL
    # Filter by services that haven't been updated for CHECK_INTERVAL
    for service in models.Service.query:#.filter(models.Service.last_checked < last_possible_time):
        status = checker.status(service)
        if status == Status.BROKEN and service.status != Status.BROKEN:
            service.broken_since = datetime.now()
        service.status = status.value
        service.last_checked = datetime.now()
        db.session.add(service)
    db.session.commit()
