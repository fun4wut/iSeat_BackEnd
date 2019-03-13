from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from ..models import User, Area, Table
from . import main
import json
import random
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")

rand = ['btn-primary','btn-warning','btn-danger']

@main.route('/floor/<n>',methods=['GET'])
def floor(n=1):
    area = {
        "A": handleAreaAndHeat('A',n),
        "B": handleAreaAndHeat('B',n),
        "C": handleAreaAndHeat('C',n)
    }
    
    return render_template("floor.html",n=n, area=area)

@main.route('/floor/<n>/area/<s>/table/<index>')
def table(n=2,s='A',index=0):
    return json.dumps({'floor':n,'area':s,'table':index}) 

def handleAreaAndHeat(area_name: str,floor: int):
    tables = Table.query.filter_by(area = area_name).filter(Table.id.like(str(floor)+str(area_name)+r"%")).all()
    tables = [{"id":x.id,"name":x.name,"type":x.type,"c01":x.c01,"c02":x.c02,"c03":x.c03,"c04":x.c04} for x in tables]
    for table in tables:
        heat = seatHeat(table)
        if heat<0.33:
            table['heat'] = 'btn-danger'
        elif heat<0.66:
            table['heat'] = 'btn-warning'
        else:
            table['heat'] = 'btn-primary'
    return tables

def isEmptySeat(s):
    if int(s[-1])%2==0: return 1
    else: return 0

def seatHeat(table):
    # return (isEmptySeat(table['c01'])+isEmptySeat(table['c02'])+isEmptySeat(table['c03'])
    # +isEmptySeat(table['c04']))/4
    return random.randint(0,3)/3