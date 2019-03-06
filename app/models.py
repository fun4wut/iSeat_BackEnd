from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager

class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.String(255),nullable=False,primary_key=True,autoincrement=False)
    library = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    floor = db.Column(db.Integer,nullable=False,primary_key=False,autoincrement=False)
    room = db.Column(db.String(255),nullable=False,primary_key=False,autoincrement=False)
    occupied = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    messages = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(255), nullable=False, primary_key=True, autoincrement=False)
    name = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    credit = db.Column(db.Integer, nullable=False, primary_key=False, autoincrement=False)
    study_time = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    message = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    previous_seat = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    present_seat = db.Column(db.String(255), nullable=False, primary_key=False, autoincrement=False)
    condition = db.Column(db.Integer,nullable=False,primary_key=False,autoincrement=False)
    start_time = db.Column(db.DateTime,nullable=True,primary_key=False,autoincrement=False)
    password_hash = db.Column(db.String(255),nullable=True,primary_key=False,autoincrement=False)
    # 用于支持用户登陆
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 加载用户的函数
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(str(user_id))


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
