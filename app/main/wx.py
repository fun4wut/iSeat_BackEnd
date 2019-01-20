import json
from .. import db
from ..models import User, Seat
from . import main

@main.route('/wx/floor/<n>', methods=['GET'])
def overviewOfFloor(n):
    img_url = "https://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/37d12f2eb9389b50579fb4a38e35e5dde6116eda.jpg"
    seats = Seat.query.filter_by(floor=n).all()
    name = set([x.room for x in seats])
    img = [img_url for x in name]
    rest = []
    current = []
    for x in name:
        tmp_seat = Seat.query.filter_by(floor=n,room=x).all()
        tmp_num = len(tmp_seat)
        tmp_rest = 0
        for y in tmp_seat:
            if y.occupied is None: tmp_rest+=1
        rest.append(tmp_rest)
        current.append(tmp_num-tmp_rest)

    return json.dumps({"img":img,"name":list(name),"rest":rest,"current":current},ensure_ascii=False)