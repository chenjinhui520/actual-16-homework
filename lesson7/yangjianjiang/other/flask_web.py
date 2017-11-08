#!/usr/bin/env python
#coding: utf-8

from flask import Flask
from flask import request
from flask import render_template
import common
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        loading = request.form.to_dict()
        #print loading
        #print common.login(loading['username'],loading['password'])
        if common.login(loading['username'],loading['password']):
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        #print registerInfo
        # 1. check user exists
        if common.check_user_exists(registerInfo['username']):
            return render_template('user_exist.html')
        # 2. check email ok(@)
        if not common.check_email(registerInfo['email']):
            return render_template('email.html')
        else:
        # 3. write data to disk
            common.WriteFile(registerInfo)
            return render_template('success.html')
    else:
        return render_template('register.html')


@app.route('/userlist')
def userlist():
    data = common.ReadFile()
    #data = [ {'index' : index, 'username':user['username'], 'email':user['email'], 'password':user['password']} for index, user in enumerate(data1) ]
    return render_template('userlist.html', users=data, errmsg='login failed')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
