#!/usr/bin/env python
#coding: utf-8

import sys
import re
import common

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        # 1. check user exists
        # 2. check email ok(@)
        # 3. write data to disk
        print 'register post'
        username=registerInfo['username']
        if re.match('^[a-zA-Z]+[0-9]*$',username) == None:
            print 'username uncorrect'
            return render_template('status.html',msginfo='username only contains letter and number!')

        email=registerInfo['email']
        if re.match('\w+@\w+\.[a-z]+',email) == None:
            print 'email uncorrect'
            return render_template('status.html',msginfo='email format is not correct!')

        password=registerInfo['password']
        if common.CheckUserExist(username,email) == 1:
            print 'user exist'
            return render_template('status.html',msginfo='Register failed! User or email exist.')
         
        registerInfo['login_failed'] = 0
        common.WriteFile(registerInfo)
        print 'write file'
        return render_template('status.html',msginfo='User %s register success!' % username)

    else:
        return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        loginInfo = request.form.to_dict()
        print loginInfo
        username = loginInfo['username']
        password = loginInfo['password']
        if loginInfo.has_key('remember-me'):
            common.rememberMe(loginInfo)
        if username == '' or password == '':
            return render_template('status.html',msginfo='Login failed. Username or password is null!')

        userslist = common.GetUsers()
        for x in userslist:
            if x['username'] == username and x['password'] == password:
                common.UpdateLoginCnt(username,0)
                return render_template('status.html',msginfo='User %s login success!' % username)
            if x['username'] == username and x['password'] != password:
                cnt = common.GetLoginCnt(username)
                cnt += 1
                common.UpdateLoginCnt(username, cnt)
                if cnt > 3:
                    return render_template('status.html',msginfo='login failed more than 3 times! You are locked!')
                else:
                    return render_template('status.html',msginfo='Login failed. Password is uncorrect!')
            
        return render_template('status.html',msginfo='Login failed. User does not exist. Please register.')

    else:
        ischeck = ''
        username = ''
        password = ''
        rememberMe=common.getRememberMe()
        if rememberMe:
            print rememberMe
            if rememberMe[0].has_key('remember-me'):
                ischeck ='checked'
                username = rememberMe[0]['username']
                password = rememberMe[0]['password']
        return render_template('login.html',username=username,password=password,check=ischeck)


@app.route('/userslist')
def userlist():
    data=common.GetUsers()
    return render_template('userlist.html', users=data, errmsg='login failed')


@app.route('/delusers')
def deluserlist():
    userdata = common.GetUsers()
    return render_template('delusers.html', users=userdata)

@app.route('/deluser/<string:user>')
def deluser(user):
    print 'del %s' % user
    common.DelUser(user)
    return render_template('status.html',msginfo='Delete user %s successfully!' % user)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
