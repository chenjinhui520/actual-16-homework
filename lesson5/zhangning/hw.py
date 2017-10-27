#!/usr/bin/env python
#coding: utf-8

import json

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


def WriteFile(registerInfo):
    try:
        with open('store.db', 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    users.append(registerInfo)
    with open('store.db', 'w') as fd:
        fd.write(json.dumps(users))

def check_user_exists(username):
    try:
        with open('store.db', 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    usernames = [ x['username'] for x in users if x ]
    if username in usernames:
        return True
    else:
        return False

def check_email(email):
    if '@' in email:
        return True
    else:
        return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        # 1. check user exists
        if check_user_exists(registerInfo['username']):
            return '<h1 style="color:red"> 用户已存在，请重新输入 </h1>'
        # 2. check email ok(@)
        if not check_email(registerInfo['email']):
            return '<h1 style="color:red"> 邮箱格式错误，请重新输入 </h1>'
        # 3. write data to disk
        WriteFile(registerInfo)
        return '<h1 style="color:red"> 注册成功 </h1>'
    else:
        return render_template('register.html')


@app.route('/userlist')
def userlist():
    with open('store.db', 'r') as fd:
        data = json.loads(fd.read())
    return render_template('userlist.html', users=data, errmsg='login failed')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
