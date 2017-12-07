#!/usr/bin/env python
#coding:utf-8

from app.models import execute_sql
from app.models import select_all_result 
from app.models import select_one_result


from crypt import encryption


def checkname(username):
    ret = 0
    sql = '''select username from users; '''
    usernames = select_all_result(sql)
    for x in range(len(usernames)):
        if "".join(tuple(usernames[x])) == username['username']:
            ret = 1
    if ret == 1:
        return False
    else:
        return True


def register(data):
    md5passwd = encryption(data['password'])
    sql = '''INSERT INTO users(username, email, password,role) values('%s', '%s', '%s','%s')''' % (data['username'], data['email'], md5passwd,data['role'])
    return execute_sql(sql)

def get_users():
    sql = '''SELECT id,username,password,email,role FROM users '''
    return select_all_result(sql)

def get_role(name):
    sql = '''SELECT role FROM users WHERE username = '%s'; ''' % name
    return select_one_result(sql)

def get_pwd(username):
    sql = '''SELECT password FROM users WHERE username = '%s'; ''' % username
    return select_one_result(sql)

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
    tmp_password = kwargs['password']
    email = kwargs['email']
    role = kwargs['role']
    db_password = get_pwd(username)
    if db_password == tmp_password:
        passowrd = tmp_password
        sql = ''' UPDATE users SET username="%s",password="%s",email="%s",role="%s" WHERE id = %s; ''' % (username,password,email,role,uid)
    else:
        password = encryption(tmp_password) 
        sql = ''' UPDATE users SET username="%s",password="%s",email="%s",role="%s" WHERE id = %s; ''' % (username,password,email,role,uid)
    return execute_sql(sql)

