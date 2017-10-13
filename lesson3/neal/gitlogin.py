#coding: utf-8
import os
import json

counter = 0
while True:
    print "please choice ['register', 'login', 'quit']."
    action = raw_input('action :')
    if action == 'register':
        print 'Create your personal account'
        username = raw_input('Username :')
        email = raw_input('Email Address :')
        password = raw_input('Password:')
        person = {'username' : username , 'email' : email, 'password' : password}
        print 'register successful'
    elif action == 'login':
        username = raw_input('Username :')
        password = raw_input('Password:')
        if username == 'neal' and password == 'neal':
            print 'login sucess,welcome to github.'
        else:
            print 'incorrect username or password'
            counter+=1
            if counter>2:
                print 'login lockdown'
                break

    elif action == 'quit':
        break
    else:
        print "action is required, please choice ['register', 'login', 'quit']."
