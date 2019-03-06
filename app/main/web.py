from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from . import main

@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")
