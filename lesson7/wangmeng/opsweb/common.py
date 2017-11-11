#!/usr/bin/env python
#coding:utf-8

from models import execute_sql
from models import select_all_result 
from models import select_user_exist

def authentication(username, password):
    return True 

def ssum(x, y):
    return x + y

def register(data):
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], data['password'])
    print sql
    return execute_sql(sql)

def get_users():
    sql = '''SELECT * FROM users;'''
    return select_all_result(sql)

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_all_result(sql)

def register_user_exist(l=[]):
    sql = '''select username from users;'''
    ret = select_user_exist(sql)
    for i in ret:
        for j in i:
            l.append(i)
    return l

def recognize_passwd(password):
    a = 0
    b = 0
    c = 0
    d = 0
    if len(password)>=8:
        for i in password:
            if i.isdigit():
                a = 1
            if i == i.upper():
                b = 1
            if i == i.lower():
                c = 1
            if i in ['!','@','#','$','%','^','&','*']: 
                d = 1
        if (a+b+c+d) == 4:
            return True
        else:
            return False
    else:
        return False

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s;''' % uid
    print sql
    return execute_sql(sql)

def userEdit(data):
    ## 1. 判断用户是否为空
    #if data['username'] == '':
    #    errmsg = "[User cannot be null...]"
    #    return errmsg
    ## 2. 判断邮箱的后缀是不是公司的邮箱后缀 @51reboot.com
    #elif '@' not in data['email']:
    #    errmsg = "[Email type wrong...]"
    #    return errmsg
    #elif '@' in data['email']:
    #    if data['email'].split('@')[1] != '51reboot.com':
    #        errmsg = "[Email suffix error...]"
    #        return errmsg
    ## 3. 密码复杂性要求 长度不能低于8位 必须包含大写、小写和数字等。(特殊字符)
    #elif recognize_passwd(data['password']) == False:
    #    errmsg = "Password type error..."
    #    print errmsg
    #    return errmsg
    #else:

    sql = '''update users set username='%s',email='%s',password='%s' where id = %s;''' %(data['username'],data['email'],data['password'],data['num'])
    return execute_sql(sql)


if __name__ == '__main__':
    print "__name__", __name__
    s = ssum(3, 2)
    print "common ssum: ", s
