#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint
from flask import request
from flask import session                 # 从flask包导入session对象
from flask import redirect
from flask import render_template
from flask_script import Manager
import logging
import hashlib

from app.common.users import *
from app.common.auth import login_required

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/',methods=['GET'])
@login_required
def getusers():
    search_value = request.args.get("search")
    logging.debug('search user:')
    logging.debug(search_value)
    if search_value == None:
        users = get_users()
    else:
        print 'search user'
        users = search(search_value)
    if users == None:
        users=''

    return render_template('users.html', users=users)


@mod.route('/add', methods=['GET', 'POST'])
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

@mod.route('/del/<int:uid>',methods=['GET','POST'])
def deluser(uid):
    if request.method == 'POST':
        response = userDel(uid)
        logging.debug('del user response:')
        logging.debug(response)
        return json.dumps({'status':0})


@mod.route('/edit/<int:uid>',methods=['GET', 'POST'])
#@app.route('/users/edit',methods=['GET', 'POST'])
def updateuser(uid):
    if request.method == 'POST':
        user = request.form.to_dict()
        logging.debug('user edit post:')
        logging.debug(user)
        user['id'] = uid
        userUpdate(user)
        return json.dumps({'status':0})

@mod.route('/checkuser',methods=['GET', 'POST'])
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

@mod.route('/checkemail',methods=['GET', 'POST'])
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

@mod.route('/getuser/<int:uid>',methods=['GET','POST'])
def getuser(uid):
    if request.method == 'POST':
        response = get_user_id(uid)
        logging.debug(response)
        data={'id':response[0],'username':response[1],'email':response[2],'password':response[3]}
        return json.dumps(data)

