#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask import render_template
from common import login
from common import register
from common import listt
from common import writeFile
from common import readFile
import sys
reload(sys)
sys.setdefaultencoding('utf8')

filename = 'store.db'

app = Flask(__name__)

@app.route('/')
def showF():
    return render_template('index.html')

@app.route('/login')
def loginF():
    login = login()
    return render_template('login.html',login=login)

@app.route('/register')
def registerF():
    name = raw_input('请输入注册账号：').strip()
    passwd = raw_input('请输入注册密码：').strip()
    passwd2 = raw_input('请确认注册密码：').strip()
    if passwd == passwd2:
        email = raw_input('请输入注册邮箱：').strip()
        data = name + '|' + passwd + '|' + email
        writeFile(filename,data)
        a = '注册成功！'
    else:
        a = '<两次输入密码不一致！>'
    return a

    return render_template('register.html',register=regis)

@app.route('/listt')
def listtF():
    li = listt()
    print li
    return render_template('listt.html',listt=li)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9898,debug=True)
