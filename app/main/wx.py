import json
from .. import db
from ..models import User, Area, Table
from . import main

@main.route('/wx/floor/<n>', methods=['GET'])
def overviewOfFloor(n):
    img_url = "https://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/37d12f2eb9389b50579fb4a38e35e5dde6116eda.jpg"
    areas = Area.query.filter_by(floor=n).all()
    name = set([x.room for x in areas])
    num = len(name)
    img = [img_url for x in name]
    rest = []
    current = []
    total = []
    for x in name:
        tmp_seat = Area.query.filter_by(floor=n,room=x).all()
        tmp_num = len(tmp_seat)
        tmp_rest = 0
        for y in tmp_seat:
            if y.occupied is None: tmp_rest+=1
        rest.append(tmp_rest)
        current.append(tmp_num-tmp_rest)
        total.append(tmp_num)

    return json.dumps({"img":img,"name":list(name),"rest":rest,"current":current,"num":num,"total":total},ensure_ascii=False)

@main.route('/wx/user/<id>',methods=['GET'])
def overviewOfUser(id):
    pass

def handleArea(area_name: str,floor: int):
    tables = Table.query.filter_by(area = area_name).filter(Table.id.like(str(floor)+str(area_name)+r"%")).all()
    return tables

@main.route('/wx/floors/<floor>', methods=['GET'])
def handleFloor(floor: int):
    A = handleArea("A",floor)
    B = handleArea("B",floor)
    return json.dumps({
        "A": [{"id":x.id,"name":x.name,"type":x.type,"c01":x.c01,"c02":x.c02,"c03":x.c03,"c04":x.c04} for x in A],
        "B": [{"id":x.id,"name":x.name,"type":x.type,"c01":x.c01,"c02":x.c02,"c03":x.c03,"c04":x.c04} for x in B],
        "ACount": len(A),
        "BCount": len(B)
    })
    #return "hello world"
