from . import db

class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.String(255),nullable=False,primary_key=True,autoincrement=False)
    library = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    floor = db.Column(db.Integer,nullable=False,primary_key=False,autoincrement=False)
    room = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    occupied = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    messages = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(255), nullable=False, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    credit = db.Column(db.Integer, nullable=False, primary_key=False, autoincrement=False)
    study_time = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    message = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    previous_seat = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    present_seat = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    condition = db.Column(db.Integer,nullable=False,primary_key=False,autoincrement=False)
    start_time = db.Column(db.Time,nullable=True,primary_key=False,autoincrement=False)
    password_hash = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.String(255),nullable=False,primary_key=True,autoincrement=False)
    name = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    type = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    area = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    c01 = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    c02 = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    c03 = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    c04 = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    
