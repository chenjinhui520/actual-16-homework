

from models import execute_sql
from models import select_all_result 
from models import select_one_result




def authentication(username, password):
    return True 


def rname(username):
    ret = 0
    sql = '''select username from users; '''
#    print sql
    usernames = select_all_result(sql)
 #   print usernames
    for x in range(len(usernames)):
        if "".join(tuple(usernames[x])) == username['username']:
            ret = 1
    if ret == 1:
        return False
    else:
        return True


def register(data):
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], data['password'])
    print sql
    return execute_sql(sql)

def get_users():
    sql = '''SELECT id,username,password,email FROM users '''
    return select_all_result(sql)

def get_user(name):
    sql = '''SELECT id,username,password,email FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    return execute_sql(sql)

def userInfo(uid):
    sql = '''SELECT * FROM users WHERE id = %s; ''' % uid
    return select_one_result(sql)
def userEdit(**kwargs):
    uid  = kwargs['id']
    username = kwargs['username']
    password = kwargs['password']
    email = kwargs['email']
    sql = ''' UPDATE users SET username="%s",password="%s",email="%s" WHERE id = %s; ''' % (username,password,email,uid)
    print sql
    return execute_sql(sql)

