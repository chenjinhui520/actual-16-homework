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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        registerInfo = request.form.to_dict()
        # 1. check user exists
        # 2. check email ok(@)
        # 3. write data to disk
        WriteFile(registerInfo)
        return 'register'
    else:
        return render_template('register.html')


@app.route('/userlist')
def userlist():
    with open('store.db', 'r') as fd:
        data = json.loads(fd.read())
    return render_template('userlist.html', users=data, errmsg='login failed')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
