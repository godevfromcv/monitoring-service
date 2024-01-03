from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash

from models.user import User

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # tbd
        user = User.get_by_username(username)
        if user and User.check_password(user.password, password):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('err')
    return render_template('login.html')


@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #tbd

        flash('done')
        return redirect(url_for('auth.login'))

    return render_template('register.html')