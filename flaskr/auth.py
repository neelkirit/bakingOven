from flask import (
    Blueprint, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# The authentication blueprint has views to register new users and to log in and log out.
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        db = get_db()
        cur = db.cursor()
        error = None

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif cur.execute(
                'SELECT id FROM User WHERE email = %s', (email,)
        ) != 0:
            error = 'User {} is already registered.'.format(email)

        if error is None:
            cur.execute(
                'INSERT INTO User (email, password) VALUES (%s, %s)',
                (email, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

    return error


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        db = get_db()
        cur = db.cursor()
        error = None
        result = cur.execute(
            'SELECT email,password FROM User WHERE email = %s', (email,)
        )
        db.commit()
        user = cur.fetchall()[0]
        if result == 0:
            error = 'Incorrect username.'
        elif not check_password_hash(user[1], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['email'] = user[0]
            return session['email']

    return error


@bp.before_app_request
def load_logged_in_user():
    email = session.get('email')

    if email is None:
        g.user = None
    else:
        db = get_db()
        cur = db.cursor()
        g.user = cur.execute(
            'SELECT * FROM User WHERE email = %s', (email,)
        )
        db.commit()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
