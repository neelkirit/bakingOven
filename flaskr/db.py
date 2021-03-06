import pymysql

from flask import g


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(db='bakingOven', user='admin', passwd='aihnet!2345',
                               host='bakingoven.cprvx5ilx4zn.us-east-1.rds.amazonaws.com', port=3306)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
