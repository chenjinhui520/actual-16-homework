#!/usr/bin/env  python
#coding:utf-8
'''
GitHub注册选项有三个
用户名
密码
Email

'''
import getpass
info = dict()
infos = dict()
def register():
    print '已经进入注册状态,请输入您的帐号密码与邮箱'
    username = raw_input('Please Input Username:')
    password = getpass.getpass('Please Input Password: ')
    email = raw_input('Please Input Email:')
    info[username] = {'password':password,'email':email}
    infos.update(info)
    #print info
    if username and password and email:
        print '您的帐号是 %s' %(username)
        print '您的密码是 %s' %(password)
        print '您的邮箱是 %s' %(email)
        print  '注册成功'
    else:
        print  '请完整输入需要的内容'






def Login():
    c = 0
    print '已经进入登陆状态,请输入您的帐号密码,输错三次会被锁定'
    username = raw_input('Please Input Username:')
    password = getpass.getpass('Please Input Password: ')
    if infos.get(username,0) and infos[username]['password'] == password:
        print '登陆成功'
    elif c >= 3:
        c += 1
        print '已经连续输错三次%s 用户被锁定' %(username)
    else:
        c += 1
        print '输入错误%s次,请重新输入' %(c)

while True:
    print '输入reg进入注册流程,输入login进入登陆流程'
    operation = raw_input('Please Input operating:')
    if operation == 'reg':
        register()
    elif operation == 'login':
        Login()
