#--*--coding: utf-8--*--

from flask import Flask                   # 从flask包导入Flask类
from flask import request                 # 从flask包导入request对象
from flask import session 
from flask import redirect                # 从flask包导入redirect函数
from flask import render_template         # 从flask包导入render_template函数 

from common import register
from common import get_user
from common import get_users 
from common import userDel 
from common import authentication

from auth import login_required 

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456' 


'''首页
'''
@app.route('/')
@login_required
def index():
    #if not session.get('sign', None):
    #    return redirect('/login')
    return render_template('index.html')


'''登录
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 验证登陆成功
        if authentication(username, password):
            session['sign'] = username
            return redirect("/")
        else:
            errmsg = "Incorrect username or password."
            return render_template('login.html', errmsg=errmsg)
    else:
        return render_template('login.html')


'''用户
'''
@app.route('/users', methods=['GET'])
def users():
    if not session.get('sign', None):
        return redirect('/login')
    #search_value = request.args.get("search")
    #print search_value
    #if search_value:
    #    users = get_user(search_value) 
    #else:
    #    users = get_users()
    users = get_users()
    return render_template('users.html', users=users)


'''用户编辑
'''
@app.route('/users/edit', methods=['GET', 'POST'])
def usersEdit():
    if request.method == 'POST':
        modifyInfo = request.form.to_dict()
        # 修改数据库
        # userEdit(modifyInfo)
        # "UPDATE users SET password = '%s' wehre username = '%s'" % (modifyInfo['username'], modifyInfo['password'])
        return redirect('/users')
    else:
        username = request.args['username']
        print username
        return render_template('users_edit.html', username=username)


'''用户删除
'''
@app.route('/users/<int:uid>', methods=['GET'])
@login_required
def usersDel(uid):
    response = userDel(uid)
    print response
    return redirect('/users')


'''用户添加
'''
@app.route('/users/add', methods=['GET', 'POST'])
def users_add():
    if request.method == 'POST':
        data = request.form.to_dict()
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


'''资产
'''
@app.route('/assets')
def assets():
    if not session.get('sign', None):
        return redirect('/login')
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
    #session.pop('sign')

    session.clear()

    #del session['sign']
    return redirect('/login')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True, threaded=True)
