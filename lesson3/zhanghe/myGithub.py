#!/usr/bin/env python
#coding: utf-8

import getpass

users = {}

# 错误3次锁定用户 
errorCount = 3

opCodes = [1, 2, 3]

def ops():
    tips = '''
1. login
2. register
3. quit'''
    print tips


def register():
    userStatus = 0
    
    print ' Register '.center(40, '*')

    # username
    while True:
        username = raw_input('Username: ').strip()
        if username in users:
            print 'username {} is exist, please use other username'.format(username)
            continue
        elif not username:
            print 'username can not null, please try again'
            continue
        else:
            break

    # email
    while True:
        email = raw_input('Email: ').strip()
        if not email:
            print 'email can not null, please try again'
            continue
        elif '@' not in email:
            print 'email format error, please try again'
            continue
        else:
            break


    # password
    while True:
        password1 = getpass.getpass('Password: ')
        if not password1:
            print 'Password can not null, please try again'
            continue
        else:
            password2 = getpass.getpass('Confirm Password: ')
            if not password2 or password1 != password2:
                print 'Password mismatch, please try again'
                continue

            break


    # register success
    users[username] = [userStatus, email, password1]
    print
    print 'register successful'
    print ' End '.center(40, '*')



def login():
    loginCount = 1 
    print ' Login'.center(40, '*')
    
    # username
    while True:
        username = raw_input('Username: ').strip()
        if username not in users:
            print 'username is not exist'
            break

        if users[username][0] == 1:
            print 'This account is locked, please contact administrator.'
            break

        while True:
            password = getpass.getpass('Password: ')
            if users[username][-1] != password:
                print 'password mismatch, please try again'
                loginCount += 1

                if loginCount > errorCount:
                    print 'password error count is too much, account is locked'
                    users[username][0] = 1
                    break
            else:
                print 'login successful'
                print ' End '.center(40, '*')
                break
        break




def main():
    while True:
        ops()
        opCode = raw_input('Please input your ops code [1,2,3]: ')
        
        try:
            opCode = int(opCode)
            if opCode not in opCodes:
                raise ValueError()
        except:
            print
            print 'ERROR: Invalid input, please try again...'
            continue
        else:
            if opCode == 3:
                print 'Quit'
                break
            elif opCode == 1:
                login()
            else:
                register()
            

if __name__ == '__main__':
    main()
