#!/bin/python
#coding: utf-8
import re
import sys

counter = 0
#filename = 'store.db'
persioninfos = [] 
failu={}

while True:
    action = raw_input('action :')

    if action == 'register':

        print 'Create your personal account'
        username = raw_input('Username :')
        if re.match('^[a-zA-Z]+[0-9]*$',username) == None:
            print 'username only have letters and number'
            continue
        email = raw_input('Email Address :')
        if re.match('\w+@\w+\.[a-z]+',email) == None:
            print 'incorrect emaill address. The format is like name@example.com'
            continue
        for u in persioninfos:
            if u['username'] == username or u['email'] == email:
                print 'user or email exist.'
                continue
        password = raw_input('Password:')
        user = {'username' : username , 'email' : email, 'password' : password}
        persioninfos.append(user)
        print 'Register successfully'
        continue

    elif action == 'login':

        username = raw_input('Username :')
        password = raw_input('Password:')
        if username.isspace() or password.isspace():
            print 'username or password is null'
            continue

        for x in persioninfos:
            if x['username'] == username and x['password'] == password:
                print 'login sucess'
                print 'welcome %s to login' % username
            else:
                print 'Account do not exist. Pleae register firstly'
                if failu.has_key(username):
                    failu[username]+=1
                    if failu[username] > 3:
                        print 'login failed more than 3 times'
                        sys.exit()
                else:
                    failu[username]=1

        continue

    elif action == 'quit':
        break
    else:
        print "action is required, please choice ['resiger', 'login', 'quit']."
        continue
