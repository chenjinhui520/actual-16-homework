
from app.models import execute_sql
from app.models import select_result
from app.models import select_all_result
from app.common.crypt import encryption


def register(data):
    md5passwd = encryption(data['password'])
    sql = '''INSERT INTO users(username, email, password, role) values('%s', '%s', '%s', '%s')''' % (data['username'], data['email'], md5passwd, data['role'])
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
    print sql
    return execute_sql(sql)

def get_passwd_from_username(username):
    sql = '''SELECT password FROM users WHERE username = '%s';''' % username
    return select_result(sql)

def get_role_from_username(username):
    sql = '''SELECT role FROM users WHERE username = '%s';''' % username
    return select_result(sql)
