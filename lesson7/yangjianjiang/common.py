

from models import execute_sql
from models import select_all_result 
from models import select_one_result




def authentication(username, password):
    return True 


def register(data):
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], data['password'])
    print sql
    return execute_sql(sql)

def get_users():
    sql = '''SELECT * FROM users '''
    return select_all_result(sql)

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    return execute_sql(sql)

def userInfo(uid):
    sql = '''SELECT * FROM users WHERE id = %s; ''' % uid
    return select_one_result(sql)
def userEdit(uid,**kwargs):
    username = kwargs['username']
    password = kwargs['password']
    email = kwargs['email']
    sql = ''' UPDATE users SET username="%s",password="%s",email="%s" WHERE id = %s; ''' % (username,password,email,uid)
    return execute_sql(sql)

