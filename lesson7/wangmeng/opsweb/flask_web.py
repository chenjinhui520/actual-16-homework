#!/usr/bin/env python
#--*--coding: utf-8--*--

from flask import Flask                   # 从flask包导入Flask类
from flask import request                 # 从flask包导入request对象
from flask import session                 # 从flask包导入session对象 
from flask import redirect                # 从flask包导入redirect函数
from flask import render_template         # 从flask包导入render_template函数 

from common import authentication
from common import register
from common import get_user
from common import get_users 
from common import userDel 

from common import userEdit
from common import register_user_exist
from common import recognize_passwd

app = Flask(__name__)
app.secret_key = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'

'''首页
'''
@app.route('/')
def index():
    return render_template('index.html')

'''登录
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authentication(username, password):
            session['username'] = username
            return redirect("/")
        else:
            errmsg = "Incorrect username or password."
            return render_template('login.html', errmsg=errmsg)
    else:
        return render_template('login.html')

'''用户信息
'''
@app.route('/users', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users():
    search_value = request.args.get("search")
    print search_value
    if search_value:
        users = get_user(search_value) 
        #for i in users:
        #    for j in i:
        #        print j
    else:
        users = get_users()
        #for i in users:
        #    for j in i:
        #        print j
    return render_template('users.html', users=users)

'''用户删除
'''
@app.route('/users/<int:uid>', methods=['GET'])
def usersDel(uid):
    response = userDel(uid)
    print response
    return redirect('/users')

'''用户编辑
'''
@app.route('/users/edit', methods=['GET', 'POST'])
def users_edit():
    #errmsgs = ['[User cannot be null...]','[Email type wrong...]','[Email suffix error...]','Password type error...']
    if request.method == 'POST':
        data = request.form.to_dict()
        print 'form.to_dict:',data
        userEdit(data)
        '''
        ret = userEdit(data)
        if ret in errmsgs:
            return render_template('users_edit.html', errmsg=ret)
        else:
            return redirect('/users')
        '''
        return redirect('/users')
    if request.method == 'GET':
        data = request.args.get('num','')
        print 'args.get:',data
        return render_template('users_edit.html', num=data)
        #return redirect('/users')

'''用户添加
'''
@app.route('/users/add', methods=['GET', 'POST'])
def users_add():
    l = []
    if request.method == 'POST':
        data = request.form.to_dict()
        if data['password'] != data['rpassword']:
            errmsg = "Confirm password error"
            return render_template('users_add.html', errmsg=errmsg)
        # 1. 判断用户是否存在，用户存在，提示改用户已被注册
        if data['username'] in register_user_exist():
            errmsg = "User had been existed!!"
            return render_template('users_add.html', errmsg=errmsg)

        # 2. 判断邮箱的后缀是不是公司的邮箱后缀 @51reboot.com
        if '@' not in data['email']:
            errmsg = "Email type illegal?[john2\033[1;33;41m@\033[0m51reboot.com]"
            return render_template('users_add.html', errmsg=errmsg)
        if '@' in data['email']:
            if data['email'].split('@')[1] != '51reboot.com':
                errmsg = "Email suffix error...[@\033[1;33;41m51reboot.com\033[0m]"
                return render_template('users_add.html', errmsg=errmsg)

        # 3. 密码复杂性要求 长度不能低于8位 必须包含大写、小写和数字等。(特殊字符)
        if not recognize_passwd(data['password']):
            errmsg = "Password type error...[Tty666$$]"
            return render_template('users_add.html', errmsg=errmsg)

        print data
        response = register(data)
        print response

        return redirect("/users")
    else:
        return render_template('users_add.html')


'''资产
'''
@app.route('/assets')
def assets():
    return render_template('assets.html')

'''性能监控
'''
@app.route('/performance_monitor')
def performance_monitor():
    return render_template('monitor.html')

'''退出
'''
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
