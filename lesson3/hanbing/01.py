#!/usr/bin/env  python
#coding:utf-8
'''
1. 仿照Github(https://github.com)登陆和注册用户。
2. 注册用户填写注册信息，注册完成，提示用户注册成功。
3. 登陆输入用户名和密码，验证成功，提示用户登陆成功信息；
   验证失败，提示错误的用户名和密码；
   连续输入错误3次，锁定用户，该用户不能在继续输入退出；

'''
import getpass

def register():
    username = raw_input('Please Input Username:')
    password = getpass.getpass('Please Input Password: ')
    email    = raw_input('Please Input Email:')
    if username and password and email:
        print '您的帐号是 %s' %(username)
        print '您的密码是 %s' %(password)
        print '您的邮箱是 %s' %(email)
        print  '注册成功'






def Login():
    pass

print '输入reg进入注册流程,输入login进入登陆流程'
operation = raw_input('Please Input operating:')
#while  1:
if operation == 'reg':
    register()
