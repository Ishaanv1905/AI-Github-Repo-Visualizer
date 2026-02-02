from flask import Flask
from routes.auth import login
from routes.dashboard import dashboard

app = Flask(__name__)

@app.route("/")
def home():
    return login()

@app.route("/dashboard")
def dash():
    return dashboard()
