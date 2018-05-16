from flask import Flask, request, escape, render_template
import json
import datetime
import services

app = Flask(__name__)
messages = []

@app.route("/", methods = ['POST', 'GET'])
def message():
    return render_template("status.html", services=services.check())
        

if __name__ == "__main__":
    app.run()

