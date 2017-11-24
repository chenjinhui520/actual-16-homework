#!/usr/bin/env python
#coding: utf-8

import json
import logging_debug

from models import execute_sql
from models import select_all_result
from models import select_one_result
import logging

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
    sql = '''INSERT INTO users(username, email, password) values('%s', '%s', '%s')''' % (data['username'], data['email'], data['password'])
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
    sql = '''UPDATE users set username='%s',password='%s',email='%s'  WHERE id = %d;''' %  (data['username'],data['password'],data['email'],data['id'])
    logging.debug(sql)
    return execute_sql(sql)

def cleanup():
    close_db()

