#coding: utf-8

from flask import Flask
from flask import flash
from flask import request
from flask import redirect
from flask import render_template

from common import register
from common import get_users
from common import authentication


app = Flask(__name__)

'''
    配置secret_key,否则不能实现session对话
    os.urandom(24)
'''
app.secret_key = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'



'''用户登录
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authentication(username, password):
            flash('You were successfully logged in')
            return redirect("/")
        else:
            return render_template('login.html', errmsg="Incorrect username or password.")
    else:
        return render_template('login.html')


'''首页
'''
@app.route('/')
def index():
    return render_template('index.html')


'''用户
'''
@app.route('/users')
def users():
    users = get_users()
    return render_template('users.html', users=users)


'''用户添加
'''
@app.route('/users/add', methods=['GET', 'POST'])
def users_add():
    if request.method == 'POST':
        data = request.form.to_dict()
        register_msg, ok = register(data)
        if ok:
            print "register sucess"
            return redirect('/users')
        return render_template('users_add.html')
    else:
        return render_template('users_add.html')


'''退出
'''
@app.route('/logout')
def logout():
    return redirect('/login')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
