#!/usr/bin/env python
#coding: utf-8

import getpass
import json
import os
import sys
from prettytable import PrettyTable


dbfile = 'mydbfile.db' #存储账号信息
maxLoginCount = 3 # 最大登录次数

# 账号格式
# {account: [accountStatus, email, password]}
# account: 账户名称
# accountStatus: 账户状态. 0表示状态正常，1表示账户锁定
# email: 账户邮箱
# password: 账户密码

def help():
    print '''
    help        --> 查看帮助信息
    list        --> 列出所有账户信息
    lock        --> 锁定账户
    unlock      --> 解锁账户
    delete      --> 删除账户
    register    --> 注册账户
    login       --> 登录
    quit        --> 退出
    '''


def quit():
    print 'Quit'
    sys.exit()


# 用户操作状态
def operaters():
    return ['help', 'list', 'lock', 'unlock', 'delete', 'login', 'register', 'quit']


# 创建数据库文件
def createDBfile(filename):
    if not os.path.exists(filename):
        fd = open(filename, 'w')
        data = {}
        json.dump(data, fd)
        fd.close()


# 打开数据库文件
def openFile(filename):
    fd = open(filename, 'r')
    data = json.load(fd)
    fd.close()
    return data


# 写入数据库文件
def writeFile(filename, data):
    fd = open(filename, 'w')
    json.dump(data, fd)
    fd.close()


def readFile(filename):
    users = openFile(filename)
    return users


def formatTable(data):
    tableHeader = ['账户名称', '账户状态', '邮箱', '密码']
    # print '-' * 70
    # print '| {:^10}| {:^10}| {:^25}| {:^15}|'.format('Account', 'Status', 'Email', 'Password')
    # print '-' * 70
    # for k, v in data.iteritems():
    #     if v[0] == 0:
    #         status = 'OK'
    #     else:
    #         status = 'LOCK'

    #     print '| {:<10}| {:^10}| {:<25}| {:<15}|'.format(k, status, v[1], v[2])
    #     print '-' * 70
    table = PrettyTable(field_names=tableHeader)
    for k, v in data.iteritems():
        if v[0] == 0:
            status = 'OK'
        else:
            status = 'LOCK'
        table.add_row([k, status, v[1], v[2]])
        
    print table


# 列出所有注册账户
def listAccount():
    if len(users) == 0:
        print 'No Any User'
    else:
        formatTable(users)



# 锁定账户
def lock():
    if len(users) == 0:
        print '没有可操作的用户'
    else:
        while True:
            lockUser = raw_input('请输入要锁定的用户: ').strip()
            if lockUser == 'FS':
                break

            if lockUser not in users:
                print '用户不存在, 请重新输入'
                continue
            else:
                users[lockUser][0] = 1
                writeFile(dbfile, users)
                print '锁定用户成功'
                break


# 解锁账户
def unlock():
    if len(users) == 0:
        print '没有可操作的用户'
    else:
        while True:
            unlockUser = raw_input('请输入解锁的用户: ').strip()
            if unlockUser == 'FS':
                break

            if unlockUser not in users:
                print '用户不存在, 请重新输入'
                continue
            else:
                users[unlockUser][0] = 0
                writeFile(dbfile, users)
                print '解锁用户成功'
                break
    

# 删除用户
def deleteAccount():
    if len(users) == 0:
        print '没有可操作的用户'
    else:
        while True:
            deleteUser = raw_input('请输入要删除的用户: ').strip()
            if deleteUser == 'FS':
                break

            if deleteUser not in users:
                print '用户不存在, 请重新输入'
                continue
            else:
                del users[deleteUser]
                writeFile(dbfile, users)
                print '删除用户成功'
                break


## 登录
def login():
    if len(users) == 0:
        print '没有可操作的用户'
    else:
        loginCount = 1 
        print ' Login'.center(40, '*')

        # username
        while True:
            username = raw_input('Username: ').strip()
            if username not in users:
                print '用户名不存在，请重新输入'
                continue

            if users[username][0] == 1:
                print '账户被锁定，请先解锁'
                break

            while True:
                password = getpass.getpass('Password: ')
                if users[username][-1] != password:
                    print '密码不匹配，请重新输入'
                    loginCount += 1

                    if loginCount > maxLoginCount:
                        print '密码错误次数太多，账户被锁定'
                        users[username][0] = 1
                        writeFile(dbfile, users)
                        break
                else:
                    print '欢迎您回来'
                    print ' End '.center(40, '*')
                    break
            break


# 注册
def register():
    # 设置用户状态，0表示状态正常，1表示用户锁定
    userStatus = 0
    print ' Register '.center(40, '*')

    # username
    while True:
        username = raw_input('Username: ').strip()
        if username in users:
            print '该用户已经存在，请使用其他用户'
            continue
        elif not username:
            print '用户名不能为空，请重新输入'
            continue
        else:
            break

    # email
    while True:
        email = raw_input('Email: ').strip()
        if not email:
            print '邮箱不能为空，请重新输入'
            continue
        elif '@' not in email:
            print '邮箱格式错误，请重新输入'
            continue
        else:
            break


    # password
    while True:
        password1 = getpass.getpass('Password: ')
        if not password1:
            print '密码不能为空，请重新输入'
            continue
        else:
            password2 = getpass.getpass('Confirm Password: ')
            if not password2 or password1 != password2:
                print '两次输入的密码不匹配，请重新输入'
                continue

            break


    users[username] = [userStatus, email, password1]
    writeFile(dbfile, users)
    print
    print '注册成功'
    print ' End '.center(40, '*')


# 主程序
def main():
    createDBfile(dbfile)
    global users
    users = readFile(dbfile)

    while True:
        ops = raw_input('Please input you operate [help, list, lock, unlock, delete, login, register, quit]: ').strip()
        if ops not in operaters():
            print 'Invalid choice, try again'
            continue

        '''
        if ops == 'help':
            help()
        elif ops == 'quit':
            quit()
        elif ops == 'list':
            listAccount()
        elif ops == 'lock':
            lock()
        elif ops == 'unlock':
            unlock()
        elif ops == 'delete':
            deleteAccount()
        elif ops == 'login':
            login()
        elif ops == 'register':
            register()
        '''

        actionMap = {'delete': deleteAccount, 'help': help, 'list': listAccount, 'lock': lock, 'unlock': unlock, 'quit': quit, 'login': login, 'register': register}
        actionMap[ops]()

if __name__ == '__main__':
    main()
