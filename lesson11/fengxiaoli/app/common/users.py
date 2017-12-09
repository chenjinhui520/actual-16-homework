#!/usr/bin/env python
#coding: utf-8

import json
#import logging_debug

from app.models import execute_sql
from app.models import select_all_result
from app.models import select_one_result
import logging
import hashlib

rememberme='./rememberme'

logging.basicConfig(
        filename = './logs',
        filemode = 'a',
        format = '[%(asctime)s] - [%(threadName)5s] -[%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        level = logging.DEBUG,
        datefmt='%m/%d/%y  %I:%M:%S %p'
)


#def rememberMe(saveuser):
#    users = []
#    users.append(saveuser)
#    with open(rememberme, 'w') as fd:
#        fd.write(json.dumps(users))
#
#
#def getRememberMe():
#    try:
#        with open(rememberme,'r') as fd:
#            users = json.loads(fd.read())
#    except Exception as e:
#            users= []
#    return users

def register(data):
    md5passwd = encrption(data['password'])
    sql = '''INSERT INTO users(username, email, password,role) values('%s', '%s', '%s','%s')''' % (data['username'], data['email'], md5passwd, data['role'])
    logging.debug(sql)
    return execute_sql(sql)

def get_users():
    sql = '''SELECT * FROM users '''
    return select_all_result(sql)

def login_check(name,password):
    sql = '''SELECT * FROM users WHERE username = '%s' and password = '%s';''' % (name,password)
    logging.debug(sql)
    return select_one_result(sql)

def get_user(name):
    sql = '''SELECT * FROM users WHERE username = '%s';''' % name
    return select_one_result(sql)

def get_email(email):
    sql = '''SELECT * FROM users WHERE email = '%s';''' % email
    return select_one_result(sql)

def get_user_id(uid):
    sql = '''SELECT * FROM users WHERE id = '%d';''' % uid
    return select_one_result(sql)

def userDel(uid):
    sql = '''DELETE FROM users WHERE id = %s; ''' % uid
    logging.debug(sql)
    return execute_sql(sql)

def userUpdate(data):
    md5passwd = encrption(data['password'])
    sql = '''UPDATE users set username='%s',password='%s',email='%s',role='%s'  WHERE id = %d;''' %  (data['username'], md5passwd, data['email'], data['id'], data['role'])
    logging.debug(sql)
    return execute_sql(sql)

def search(name):
    sql = '''SELECT * FROM users WHERE username like '%s\%' or email like '%s\%';''' % (name,name)
    print sql
    return select_one_result(sql)

def encrption(dstr):
    md5sum = hashlib.md5(dstr)
    return md5sum.hexdigest()

def authentication(username,password):
    md5passwd=encrption(password)
    print md5passwd
    return login_check(username, md5passwd)

def get_role_from_user(username):
    sql = '''SELECT role FROM users WHERE username = '%s';''' % username
    return select_one_result(sql)

def cleanup():
    close_db()

