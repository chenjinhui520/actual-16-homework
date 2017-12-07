#!/usr/bin/env python
#coding:utf-8
from flask import session
from flask import redirect
from functools import wraps

##验证
from crypt import encryption
from app.models import select_one_result

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not session.get('sign',None):
            return redirect('/login')
       
        return func(*args,**kwargs)
    return wrapper 

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
