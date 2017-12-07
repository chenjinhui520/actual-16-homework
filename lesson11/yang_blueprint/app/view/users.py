#!/usr/bin/env python
#coding:utf-8

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import jsonify


import logging
import json

from app.common.auth import login_required

from app.common.auth import authentication
from app.common.users import get_role
from app.common.users import checkname
from app.common.users import register 
from app.common.users import get_users
from app.common.users import get_user
from app.common.users import userDel
from app.common.users import userInfo
from app.common.users import userEdit

mod = Blueprint('users',__name__,url_prefix='/users')


@mod.route('/checkusername', methods=['GET', 'POST', 'DELETE', 'PUT'])
@login_required
def checkusername():
    logging.debug('')
    if request.method == 'POST':
        data = request.form.to_dict()
        print data
        if checkname(data):
            #return json.dumps({"status":0})
            ret = {"status":0}
        else:
            #return json.dumps({"status":1})
            ret = {"status":1}
        return jsonify(ret)
    else:
        return redirect("/users")


'''用户
'''
@mod.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
@login_required
def users():
    logging.debug('')
    search_value = request.args.get("search")
    if request.method == 'POST':
        data = request.form.to_dict()
        #if data['username'] and data['email'] and data['password']:
        response = register(data)
        #    return "11111111"
        #else:
        return json.dumps({"status":1})
    else:
        if search_value:
            users = get_user(search_value)
        else:
            users = get_users()
        return render_template('users.html', users=users)


'''用户删除
'''
@mod.route('/<int:uid>', methods=['GET'])
@login_required
def usersDel(uid):
    logging.debug('')
    response = userDel(uid)
    return redirect('/users')

'''用户修改
'''
@mod.route('/edit', methods=['POST','GET'])
@login_required
def usersedit():
    logging.debug('user eidt')
    if request.method == 'POST':
        data = request.form.to_dict()
        print data
        print type(data)
        user = userEdit(**data)
        return json.dumps({'status':0})
    else:
        return redirect('/users')


'''用户添加
'''
@mod.route('/add', methods=['GET', 'POST'])
def users_add():
    logging.debug('user add')
    if request.method == 'POST':
        data = request.form.to_dict()
        print data
        if data['password'] != data['rpassword']:
            errmsg = "Confirm password error"
            return render_template('users_add.html', errmsg=errmsg)
        # 1. 判断用户是否存在，用户存在，提示改用户已被注册

        # 2. 判断邮箱的后缀是不是公司的邮箱后缀 @51reboot.com

        # 3. 密码复杂性要求 长度不能低于8位 必须包含大写、小写和特殊字符等

        print data
        response = register(data)
        print response

        return redirect("/users")
    else:
        return render_template('users_add.html')

