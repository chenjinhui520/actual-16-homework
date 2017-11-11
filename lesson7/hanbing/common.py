#!/usr/bin/env python
#coding:utf-8

from models import *
import hashlib



def Adduser(username,password,email):
   hash_md5 = hashlib.md5(password)
   pwds     = hash_md5.hexdigest()
   if check_user_exists(username,email):
        u = User(username=username, password=pwds,email=email)
        db.session.add(u)
        db.session.commit()
        return '注册成功...'
   else:
        return '用户名或Email已经存在'

def check_user_exists(username,email):
    us = User.query.filter_by(username=username).first()
    em = User.query.filter_by(email=email).first()
    if us is None and em is None:
        return True
    else:
        return False


def  authentication(username,pwd):
    hash_md5 = hashlib.md5(pwd)
    pwds     = hash_md5.hexdigest()
    us = User.query.filter_by(username='test1').first()
    if  username == us.username and pwds == us.password:
        return '登陆成功...'
    else:
        return '帐号或密码错误'

def listuser():
    lists =  User.query.all()
    return  lists
