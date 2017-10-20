#!/bin/python
#coding: utf-8
import re
import json
import os

db = './users.db'
userslist=[]
# 记录所有用户登陆失败次数
failu={}
# 控制循环退出
status=1

def getusers():
    obj=json.load(open(db, 'r'))
    return obj

def saveusers(x):
    userslist.append(x)
    data=json.dump(userslist,open(db, 'w'))

def login():
    username = raw_input('Username :')
    password = raw_input('Password:')
    if username.isspace() or password.isspace():
        print 'username or password is null'
        return

    if os.path.exists(db):
        userslist=getusers()
        for x in userslist:
            if x['username'] == username and x['password'] == password:
                print 'login sucess'
                print 'welcome %s to login' % username
                if failu.has_key(username):
                    failu.pop(username)
                return

    print 'Account do not exist. Pleae register firstly'
    if failu.has_key(username):
        failu[username]+=1
        if failu[username] > 3:
            print 'login failed more than 3 times'
            status=0
 
    else:
        failu[username]=1

def register():
    print 'Create your personal account'
    username = raw_input('Username :')
    if re.match('^[a-zA-Z]+[0-9]*$',username) == None:
        print 'username only have letters and number'
        return

    email = raw_input('Email Address :')
    if re.match('\w+@\w+\.[a-z]+',email) == None:
        print 'incorrect emaill address. The format is like name@example.com'
        return

    if os.path.exists(db):
        userslist=getusers()
        for u in userslist:
            if u['username'] == username or u['email'] == email:
                print 'user or email exist.'
                return
    
    password = raw_input('Password:')
    user = {'username' : username , 'email' : email, 'password' : password}
    saveusers(user)
    print 'Register successfully'

def main():
    while status == 1:
        action = raw_input('action :')
        if action == 'register':
            register()
            continue

        elif action == 'login':
            login()
            continue

        elif action == 'quit':
            break

        else:
            print "action is required, please choice ['resiger', 'login', 'quit']."
            continue

main()
