from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from models import initDB


@app.route('/')
def hello_world():
    initDB()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

