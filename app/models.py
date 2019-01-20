from . import db

class Seat(db.Model):
    __tablename__ = 'seats'
    id = db.Column(db.String(255),nullable=False,primary_key=True,autoincrement=True)
    library = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    floor = db.Column(db.Integer,nullable=False,primary_key=False,autoincrement=False)
    room = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    occupied = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    messages = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(255), nullable=False, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    violation = db.Column(db.Integer, nullable=False, primary_key=False, autoincrement=False)
    study_time = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    message = db.Column(db.String(255), nullable=False, primary_key=True, autoincrement=False)
    previous_seat = db.Column(db.String(255), nullable=False, primary_key=True, autoincrement=False)
    present_seat = db.Column(db.String(255), nullable=False, primary_key=True, autoincrement=False)
