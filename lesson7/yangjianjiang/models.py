
import MySQLdb as mdb

#conn = mdb.connect(host='127.0.0.1', user='root', passwd='123456', db='dbtest2', charset='utf8')
conn = mdb.connect(host='127.0.0.1', user='root', passwd='123456', db='actual16', charset='utf8')

cursor = conn.cursor()

conn.autocommit(1)


def execute_sql(sql):
    return cursor.execute(sql)

def select_all_result(sql):
    cursor.execute(sql)
    return cursor.fetchall()

def select_one_result(sql):
    cursor.execute(sql)
    return cursor.fetchone()
