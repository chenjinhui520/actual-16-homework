#!/usr/bin/env python
#coding:utf-8

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session
import logging

from app.common.auth import authentication
from app.common.users import get_role

mod = Blueprint('login',__name__)


'''登录
'''
@mod.route('/login', methods=['GET', 'POST'])
def login():
    logging.debug('login')
    #print request.form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #print username
        #print password
        #if authentication(username, password):
        authinfo,ok = authentication(username, password)
        if ok:
            role = get_role(username)
            session['sign'] = {'username':username,'role':role[0]}
            return redirect("/")
        else:
            return render_template('login.html', errmsg=authinfo)
    else:
        return render_template('login.html')



'''退出
'''
@mod.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

