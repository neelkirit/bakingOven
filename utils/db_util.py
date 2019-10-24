import datetime

import pymysql

# import json

db = pymysql.connect(db='AIHealth', user='root', passwd='root', host='localhost', port=8889)


def fetch():
    cursor = db.cursor()
    sql = "SELECT * FROM User"
    cursor.execute(sql)
    results = cursor.fetchall()
    return str(results)


def register(user_details):
    print(user_details)
    cur = db.cursor()
    now = datetime.datetime(2009, 5, 5)
    try:
        cur.execute(
            "INSERT INTO User(userid,name,product,age,profile_picture,gender,city, state, country, email, password, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (user_details['userid'], user_details['name'], user_details['product'], user_details['age'],
             user_details['profile_picture'], user_details['gender'], user_details['city'], user_details['state'],
             user_details['country'], user_details['email'], user_details['password'], now, now))
        db.commit()
        print("Registered")
    except Exception as e:
        return (str(e))
    return "Yo"
