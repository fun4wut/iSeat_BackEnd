from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(id=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect('main.index')
        else:
            return render_template('login.html')
    elif request.method == 'GET':
        return render_template('login.html')