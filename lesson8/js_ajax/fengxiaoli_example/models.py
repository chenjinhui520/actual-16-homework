
import MySQLdb as mdb

conn = mdb.connect(host='112.74.164.107', user='monkey', passwd='monkey123', db='dbtest', charset='utf8')

cursor = conn.cursor()

conn.autocommit(1)


def execute_sql(sql):
    return cursor.execute(sql)

def select_all_result(sql):
    cursor.execute(sql)
    return cursor.fetchall()

def close_db():
    cursor.close()
    conn.close()
