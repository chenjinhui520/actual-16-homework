#coding: utf-8
from flask import Flask, request, render_template
import bm

listen = '0.0.0.0'
port = 5000
debug = False
dbfile = 'store.db'

app = Flask(__name__)

# index paged
@app.route('/')
def view_index():
    bm.createDBfile(dbfile)
    return render_template('index.html')


# login
@app.route('/login', methods=['GET', 'POST'])
def view_login():
    if request.method == 'POST':
        userData = request.form.to_dict()
        username = userData['username']
        password = userData['password']

        loginResult, loginInfo = bm.login(dbfile, username, password)
        return render_template('result.html', info=loginInfo)

    return render_template('login.html')


# register
@app.route('/register', methods=['GET', 'POST'])
def view_register():
    if request.method == 'POST':
        userData = request.form.to_dict()
        registerResult, registerInfo = bm.register(dbfile, userData)
        return render_template('result.html', info=registerInfo)
    return render_template('register.html')
        

# show usres
@app.route('/users')
def view_users():
    bm.createDBfile(dbfile)
    users = bm.loadData(dbfile)
    status = None
    if users:
        for k, v in users.iteritems():
            if v[0] == 0:
                status = u'正常'
            else:
                status = u'锁定'
    return render_template('users.html', users=users, status=status)


if __name__ == '__main__':
    app.run(host=listen, port=port, debug=debug)
