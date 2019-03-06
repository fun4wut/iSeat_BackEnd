from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from . import main
import random
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")

rand = ['btn-primary','btn-warning','btn-danger']

@main.route('/floor/<n>',methods=['GET'])
def floor(n=1):
    area = {
        "a": [[random.choice(rand) for i in range(0,10)] for i in range(0,10)],
        "b": [[random.choice(rand) for i in range(0,10)] for i in range(0,10)],
        "c": [[random.choice(rand) for i in range(0,10)] for i in range(0,10)]
    }
    
    return render_template("floor.html",n=n, area=area)
