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
def check_user(username):
    try:
        with open('store.db', 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []
    usernames = [x['username'] for x in users if x] 
    if username in usernames:
        return True
    else:
        return False
def check_email(email):
    if '@' in email:
        return True
    else:
        return False
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        # 1. check user exists
        if check_user(registerInfo['username']):
           return render_template('user.html')
        # 2. check email ok(@)
        if check_email(registerInfo['email']):
        # 3. write data to disk
            WriteFile(registerInfo)
            return render_template('done.html')
        else:
            return render_template('email.html')
    else:
        return render_template('register.html')


@app.route('/userlist')
def userlist():
    with open('store.db', 'r') as fd:
        data = json.loads(fd.read())
    return render_template('userlist.html', users=data, errmsg='login failed')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
