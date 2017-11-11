

from models import execute_sql
from models import select_all_result 




def authentication(username, password):
    return True 


def ssum(x, y):
    return x + y


def register(data):
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s');''' % (data['username'], data['email'], data['password'])
    print sql
    return execute_sql(sql)

def get_users():
    sql = '''SELECT * FROM users; '''
    return select_all_result(sql)

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    return execute_sql(sql)
    
def modifi_passwd(modifi_data):
    sql = '''update users set password ='%s' where username ='%s'; ''' %(modifi_data['password'],modifi_data['username'])
    print(sql)
    return execute_sql(sql)
   
if __name__ == '__main__':
    print "__name__", __name__
    s = ssum(3, 2)
    print "common ssum: ", s
