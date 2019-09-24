import pymysql

db = pymysql.connect(db='AIHealth', user='root', passwd='root', host='localhost', port=8889)


def fetch_all():
    cursor = db.cursor()
    sql = "SELECT * FROM User"
    cursor.execute(sql)
    results = cursor.fetchall()
    return str(results)
