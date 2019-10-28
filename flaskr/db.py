import pymysql

from flask import g


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(db='bakingOven', user='root', passwd='root', host='localhost', port=8889)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
