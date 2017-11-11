#!/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template,url_for,request
from models import User,db
from common import *
from datetime import datetime


app = Flask(__name__)
#初始化数据库
#db.drop_all()
#db.create_all()

#首页 导航
@app.route("/")
def index():
    return  render_template('index.html')

#登陆验证
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd      = request.form['password']
        return  authentication(username,pwd)
    else:
        return  render_template('login.html')

#注册
@app.route("/register",methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd      = request.form['password']
        email    = request.form['email']
        return Adduser(username,pwd,email)
    else:
        return  render_template('register.html')

@app.route('/admin',methods=['POST','GET'])
def admin():
    ll = listuser()
    return  render_template('admin.html',lists=ll)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
