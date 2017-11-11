#--*--coding: utf-8--*--

from flask import Flask                   # 从flask包导入Flask类
from flask import request                 # 从flask包导入request对象
from flask import session                 # 从flask包导入session对象 
from flask import redirect                # 从flask包导入redirect函数
from flask import render_template         # 从flask包导入render_template函数 

from common import authentication
from auth import login_required


app = Flask(__name__)
app.secret_key = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'


'''首页
'''
@app.route('/')
@login_required
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


'''用户
'''
@app.route('/users', methods=['GET', 'POST', 'DELETE', 'PUT'])
@login_required
def users():
    return render_template('users.html')


'''用户添加
'''
@app.route('/users/add', methods=['GET', 'POST'])
@login_required
def users_add():
    if request.method == 'POST':
        print dir(request.form)
        print "values: ", request.form.values()
        data = request.form.to_dict()
        print data
        if data['password'] != data['rpassword']:
            errmsg = "Confirm password error"
            return render_template('users_add.html', errmsg=errmsg)
        return redirect("/users")
    else:
        return render_template('users_add.html')


'''资产
'''
@app.route('/assets')
@login_required
def assets():
    return render_template('assets.html')


'''性能监控
'''
@app.route('/performance_monitor')
@login_required
def performance_monitor():
    return render_template('monitor.html')


'''退出
'''
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
