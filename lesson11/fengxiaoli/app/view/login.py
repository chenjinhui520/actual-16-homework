#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint
from flask import Flask
from flask import request
from flask import session                 # 从flask包导入session对象
from flask import redirect
from flask import render_template
import logging
from app.log import logging_debug
from app.common.users import authentication
from app.common.users import get_role_from_user


mod = Blueprint('login', __name__)

@mod.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.to_dict()
        logging.debug('login post:')
        logging.debug(user)
        if authentication(user['username'],user['password']):
        #if login_check(user['username'],user['password']):
            username = user['username']
            role = get_role_from_user(username)
            logging.debug('user' + username + 'exist. Role=' + role[0])
            session['sign'] = { 'username' : username, 'role' : role[0]}
            return redirect('/users')

        else:
            logging.debug('user' + user['username'] + 'do not exist.')
            return render_template('login.html',errmsg='Login failed. Password is wrong. Or user ' + user['username'] + ' does not exist.')

    else:
        return render_template('login.html')


@mod.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

