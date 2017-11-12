#!/usr/bin/env python
#coding: utf-8

import sys
import re
import common

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
        # 1. check user exists
        # 2. check email ok(@)
        # 3. write data to disk
        print 'register post'
        username=registerInfo['username']
        if re.match('^[a-zA-Z]+[0-9]*$',username) == None:
            print 'username uncorrect'
            return render_template('users_add.html',errmsg='username only contains letter and number!')

        email=registerInfo['email']
        if email.endswith('@51reboot') == False:
            print 'email uncorrect'
            return render_template('users_add.html',errmsg='email format is not correct!')

        password=registerInfo['password']
        rpassword=registerInfo['rpassword']
        if password != rpassword:
            return render_template('users_add.html',errmsg='The password and confirm password are different. ')

        if get_user(username):
            print 'user exist'
            return render_template('users_add.html',errmsg='Register failed! User or email exist.')
         
        #registerInfo['login_failed'] = 0
        user={'username':username,'password':password,'email':email}
        register(user)
        return redirect('/users')

    else:
        return render_template('users_add.html')

#@app.route('/users',methods=['GET', 'POST', 'DELETE', 'PUT'])
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
        loginInfo = request.form.to_dict()
        print loginInfo
        username = loginInfo['username']
        password = loginInfo['password']
        #if loginInfo.has_key('remember-me'):
        #    common.rememberMe(loginInfo)
        if username == '' or password == '':
            return render_template('login.html',errmsg='Login failed. Username or password is null!')

        userslist = get_Users()
        for x in userslist:
            if x['username'] == username and x['password'] == password:
                #common.UpdateLoginCnt(username,0)
                return render_template('/users',user=username)

            if x['username'] == username and x['password'] != password:
               # cnt = common.GetLoginCnt(username)
               # cnt += 1
               # common.UpdateLoginCnt(username, cnt)
                #if cnt > 3:
                 #   return render_template('status.html',msginfo='login failed more than 3 times! You are locked!')
                #else:
                return render_template('login.html',msginfo='Login failed. Password is uncorrect!')
            
        return render_template('login.html',msginfo='Login failed. User does not exist. Please register.')

    else:
        ischeck = ''
        username = ''
        password = ''
       # rememberMe=common.getRememberMe()
       # if rememberMe:
       #     print rememberMe
       #     if rememberMe[0].has_key('remember-me'):
       #         ischeck ='checked'
       #         username = rememberMe[0]['username']
       #         password = rememberMe[0]['password']
        return render_template('login.html',username=username,password=password,check=ischeck)



@app.route('/users/del/<int:uid>')
def deluser(uid):
    response = userDel(uid)
    print response
    return redirect('/users')

#@app.route('/users/edit/<int:uid>',methods=['GET', 'POST'])
@app.route('/users/edit',methods=['GET', 'POST'])
def updateuser():
    if request.method == 'POST':
        print 'update user post'
        user = request.form.to_dict()
        print user
        user['id'] = uid
        userUpdate(user)
        return redirect('/users')
    else:
        uid = request.args['uid']
        uid = request.args.get('uid', '')
        print uid, type(uid) 
        uid = int(uid)
        user=get_user_id(uid)
        print user[0]
        return render_template('users_edit.html',user=user[0])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
