#coding: utf-8

import json
import sys
import re

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
database='./store.db'

def WriteFile(registerInfo):
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    users.append(registerInfo)
    with open(database, 'w') as fd:
        fd.write(json.dumps(users))

def GetUsers():
    try:
        with open(database,'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
            users= []
    return users

def CheckUserExist(user,email):
    try:
        with open(database,'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
            users= []
    for u in users:
        if u['username'] == user or u['email'] == email:
            print 'user or email exist.'
            return 1
    return 0

def UpdateLoginCnt(user,count):
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    for u in users:
        if u['username'] == user:
            u['login_failed'] = count
            break

    with open(database, 'w') as fd:
        fd.write(json.dumps(users))

def GetLoginCnt(user):
    cnt = 0
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    for u in users:
        if u['username'] == user:
            cnt=u['login_failed']
            break
    return cnt

def DelUser(user):
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []
    index = 0
    for u in users:
        if u['username'] == user:
            users.pop(index)
            break
        index += 1

    with open(database, 'w') as fd:
        fd.write(json.dumps(users))


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
        if CheckUserExist(username,email) == 1:
            print 'user exist'
            return render_template('status.html',msginfo='Register failed! User or email exist.')
         
        registerInfo['login_failed'] = 0
        WriteFile(registerInfo)
        print 'write file'
        return render_template('status.html',msginfo='User %s register success!' % username)

    else:
        return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        loginInfo = request.form.to_dict()
        username = loginInfo['username']
        password = loginInfo['password']
        if username == '' or password == '':
            return render_template('status.html',msginfo='Login failed. Username or password is null!')

        userslist = GetUsers()
        for x in userslist:
            if x['username'] == username and x['password'] == password:
                UpdateLoginCnt(username,0)
                return render_template('status.html',msginfo='User %s login success!' % username)
            if x['username'] == username and x['password'] != password:
                cnt = GetLoginCnt(username)
                cnt += 1
                UpdateLoginCnt(username, cnt)
                if cnt > 3:
                    return render_template('status.html',msginfo='login failed more than 3 times! You are locked!')
                else:
                    return render_template('status.html',msginfo='Login failed. Password is uncorrect!')
            
        return render_template('status.html',msginfo='Login failed. User does not exist. Please register.')

    else:
        return render_template('login.html')


@app.route('/userslist')
def userlist():
    data=GetUsers()
    return render_template('userlist.html', users=data, errmsg='login failed')


@app.route('/delusers')
def deluserlist():
    userdata = GetUsers()
    return render_template('delusers.html', users=userdata)

@app.route('/deluser/<string:user>')
def deluser(user):
    print 'del %s' % user
    DelUser(user)
    return render_template('status.html',msginfo='Delete user %s successfully!' % user)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
