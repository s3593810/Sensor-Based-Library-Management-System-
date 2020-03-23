# pip3 install flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy
# python3 flask_main.py
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from iot_api import api, db

"""
This iot_main class inegrates the cloud database with the api
and helps geeting, posting and delating functions through api calls thus acts as 
the server for the site.
"""
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Update HOST and PASSWORD appropriately.
HOST = "35.244.105.250"
USER = "root"
PASSWORD = "abc123"
DATABASE = "LMS"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host = "127.0.0.1",port ="5000")
