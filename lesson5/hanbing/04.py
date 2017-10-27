#!/usr/bin/env python
#coding:utf-8


from flask import Flask,render_template,url_for,request
import json
import hashlib
app = Flask(__name__)


data = []
filename = 'store.db'
datas = {}
dw =[]
def writeFile(filename,data):
    try:
        with open('store.db', 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []
    users.append(data)
    with open(filename,'w') as f:
            daw = json.dumps(users)
            f.write(daw)

def readFile(filename):
    with open(filename,'r') as f:
        da = f.read()
        datas = json.loads(da)
        return datas

def check_user_exists(username):
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

def  authentication(user,passw):
    pass
    #new_dict = {v: k for k,v in some_dict.items()}

@app.route('/')
def index():
    return render_template('index.html',title=u'第五次作业')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd      = request.form['pwd']
        email    = request.form['mail']
        hash_md5 = hashlib.md5(pwd)
        pwds     = hash_md5.hexdigest()
        Info     = {'username':username,'password':pwds,'email':email,'failed_count':0}
        #Info     = request.form.to_dict()
        #
        if check_user_exists(username):
            return  u'用户已经存在'
        else:
            writeFile(filename,Info)
            return   u'注册成功'
    else:
        return render_template('register.html')

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        pwd      = request.form['pwd']

    else:
        return render_template('login.html')

@app.route('/list')
def list():
    da = readFile(filename)
    return render_template('list.html',users=da)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
