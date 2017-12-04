import hashlib
from models import execute_sql
from models import select_all_result 
from models import select_one_result

def encryption(dstr):
    md5sum = hashlib.md5(dstr)
    return md5sum.hexdigest()


def authentication(username, password):
    sql = '''select username,password from users where username='%s' '''%username
    data = select_one_result(sql)
    md5pwd = encryption(password)
    if not data:
        return "username:%s is not found!"%username,False
    #elif data[0] != username:
    #    return "username:%s is not found!"%username,False
    elif data[1] != md5pwd:
        return "username:%s bad password"%username,False
    else:
        return None,True 


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
    md5passwd = encryption(data['password'])
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], md5passwd)
    #print sql
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
    #print sql
    return execute_sql(sql)

