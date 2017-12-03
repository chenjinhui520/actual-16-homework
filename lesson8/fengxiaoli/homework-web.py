#!/usr/bin/env python
#coding: utf-8

import sys
import re

from flask import Flask
from flask import request
from flask import session                 # 从flask包导入session对象
from flask import redirect
from flask import render_template
from common import *

app = Flask(__name__)
app.secret_key = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/add', methods=['GET', 'POST'])
def usersadd():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        print  registerInfo
        register(registerInfo)
        return redirect('/users')

    else:
        return render_template('users_add.html')

#@app.route('/users',methods=['GET', 'POST'])
@app.route('/users',methods=['GET'])
def getusers():
    search_value = request.args.get("search")
    print search_value
    if search_value:
        users = get_user(search_value)
    else:
        users = get_users()
    return render_template('users.html', users=users)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print 'login post'
        user = request.form.to_dict()
        print user
        if login_check(user['username'],user['password']):
            print 'user exist'
            return redirect('/users')

        else:
            print 'user does not  exist'
            return render_template('login.html',errmsg='Login failed. Password is wrong. Or user ' + user['username'] + ' does not exist.')

    else:
        return render_template('login.html')

@app.route('/users/del/<int:uid>',methods=['GET','POST'])
def deluser(uid):
    if request.method == 'POST':
        response = userDel(uid)
        print response
        return json.dumps({'status':0})
    

@app.route('/users/edit/<int:uid>',methods=['GET', 'POST'])
#@app.route('/users/edit',methods=['GET', 'POST'])
def updateuser(uid):
    if request.method == 'POST':
        print 'update user post'
        user = request.form.to_dict()
        print user
        user['id'] = uid
        userUpdate(user)
        return json.dumps({'status':0})



@app.route('/checkuser',methods=['GET', 'POST'])
def checkuser():
    if request.method == 'GET':
        print 'checkuser post'
        user = request.args.to_dict()
        print user
        print user['username']
        if get_user(user['username']):
            print 'user exist'
            return json.dumps({'status':1})

        else:
            print 'user does not  exist'
            return json.dumps({'status':0})

@app.route('/checkemail',methods=['GET', 'POST'])
def checkemail():
    if request.method == 'POST':
        print 'check email post'
        user = request.form.to_dict()
        if get_email(user['email']):
            print 'email exist'
            return json.dumps({'status':1})

        else:
            print 'email do not exist'
            return json.dumps({'status':0})

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
