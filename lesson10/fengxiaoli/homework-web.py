#!/usr/bin/env python
#coding: utf-8

import sys
import re

from flask import Flask
from flask import request
from flask import session                 # 从flask包导入session对象
from flask import redirect
from flask import render_template
from flask_script import Manager
from common import *
from auth import login_required
import logging
import hashlib



app = Flask(__name__)
#app.secret_key = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'
app.config['SECRET_KEY'] = '123456'
manager=Manager(app)

logging.basicConfig(
        filename = './logs',
        filemode = 'a',
        format = '[%(asctime)s] - [%(threadName)5s] -[%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        level = logging.DEBUG,
        datefmt='%m/%d/%y  %I:%M:%S %p'
)



@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/users/add', methods=['GET', 'POST'])
def usersadd():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        logging.debug('user add:')
        logging.debug(registerInfo)
        effect_record = register(registerInfo)
        if effect_record == 1 :
            return json.dumps({'status':0})
        else:
            return json.dumps({'status':1})

    else:
        return render_template('users_add.html')

#@app.route('/users',methods=['GET', 'POST'])
@app.route('/users',methods=['GET'])
@login_required
def getusers():
    search_value = request.args.get("search")
    logging.debug('search user:')
    logging.debug(search_value)
    if search_value == None:
        print 'get user'
        users = get_users()
    else:
        print 'search user'
        users = search(search_value)
    print users
    if users == None:
        users=''

    return render_template('users.html', users=users)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.to_dict()
        logging.debug('login post:')
        logging.debug(user)
        if authentication(user['username'],user['password']):
        #if login_check(user['username'],user['password']):
            logging.debug('user' + user['username'] + 'exist.')
            session['sign'] = user['username']
            return redirect('/users')

        else:
            logging.debug('user' + user['username'] + 'do not exist.')
            return render_template('login.html',errmsg='Login failed. Password is wrong. Or user ' + user['username'] + ' does not exist.')

    else:
        return render_template('login.html')

@app.route('/users/del/<int:uid>',methods=['GET','POST'])
def deluser(uid):
    if request.method == 'POST':
        response = userDel(uid)
        logging.debug('del user response:')
        logging.debug(response)
        return json.dumps({'status':0})
    

@app.route('/users/edit/<int:uid>',methods=['GET', 'POST'])
#@app.route('/users/edit',methods=['GET', 'POST'])
def updateuser(uid):
    if request.method == 'POST':
        user = request.form.to_dict()
        logging.debug('user edit post:')
        logging.debug(user)
        user['id'] = uid
        userUpdate(user)
        return json.dumps({'status':0})



@app.route('/checkuser',methods=['GET', 'POST'])
def checkuser():
    if request.method == 'POST':
        print 'checkuser post'
        user = request.form.to_dict()
        logging.debug('/checkuser post')
        logging.debug(user['username'])
        if get_user(user['username']):
            logging.debug('user exist')
            return json.dumps({'status':1})

        else:
            logging.debug('user does not exist')
            return json.dumps({'status':0})

@app.route('/checkemail',methods=['GET', 'POST'])
def checkemail():
    if request.method == 'POST':
        print 'check email post'
        user = request.form.to_dict()
        if get_email(user['email']):
            logging.debug('email exist')
            return json.dumps({'status':1})

        else:
            logging.debug('email do not exist')
            return json.dumps({'status':0})

@app.route('/getuser/<int:uid>',methods=['GET','POST'])
def getuser(uid):
    if request.method == 'POST':
        response = get_user_id(uid)
        logging.debug(response)
        data={'id':response[0],'username':response[1],'email':response[2],'password':response[3]}
        return json.dumps(data)

@app.route('/logout')
def logout():
    session.pop('sign')
    return redirect('/login')

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)
    #manager.run()
