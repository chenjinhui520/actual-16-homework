
import MySQLdb as mdb
from config.parseConfig import parseconfig

config = parseconfig('app/config/my.conf','mysqld')
conn = mdb.connect(
        host=config['host'],
        user=config['user'], 
        passwd=config['password'],
        db=config['db'],
        charset=config['charset'])

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

def close_db():
    cursor.close()
    conn.close()
