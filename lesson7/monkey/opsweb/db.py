
import MySQLdb

def connect(host, port, user, passwd, db, charset='utf8'):
    conn = mdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    conn.autocommit(1)
    return conn

def execute_sql(sql):
    cursor = conn.cursor()
    cursor.execute(sql)


def bulker_execute_sql(sql):
    pass


def fetch(sql):
    pass
