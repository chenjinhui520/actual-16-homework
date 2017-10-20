#!/usr/bin/env python
#!coding: utf-8

'''
有个小Bug 读取文件那如果文件是空的会读取不到文件内容json模块会报错,需要默认里面有内容
'''
import json
import getpass
filename = "store.db"
info=dict()
infos=dict()
def login():
    print '已经进入登陆状态,请输入您的帐号密码,输错三次会被锁定'
    username = raw_input('Please Input Your username')
    password = raw_input('Please Input Your Password')
    authentication(username, password)


def register():
    print '已经进入注册状态,请输入您的帐号密码与邮箱'
    username = raw_input('Please Input Username:')
    password = getpass.getpass('Please Input Password: ')
    email = raw_input('Please Input Email:')
    #check_user_exists(username)
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

    writeFile(filename, infos)


def writeFile(filename, data):
    with open(filename,'ab') as f:
        datas = json.dumps(data)
        f.write(datas)


def readFile(filename):
    with open(filename,'r') as f:
        da = f.read()
        data = json.loads(da)
        return data



def printFormat(data, format="json"):
    if format == "json":
        print json.dumps(data, indent=4)
    elif format == "xml":
        pass

    elif format == "table":
        pass


def check_user_exists(username):
    data = readFile(filename)
    if  data:
        data.get(username,0)
        print '用户已存在,请重新输入'
        login()
    else:
        pass


def authentication(username, password):
    '''
        如果用户名和密码验证成功 return True 否则 return False
    '''
    c = 0
    check_user_exists(username)
    if infos.get(username,0) and infos[username]['password'] == password:
            return True
    elif c > 2:
        c += 1
        print '已经连续输错三次%s 用户被锁定' %(username)
    else:
        c += 1
        print '输入错误%s次,请重新输入' %(c)

def help():
    print '''
    login 登陆
    register 注册
    list    列出所有用户信息
    quit    退出
    '''



def main():
    while True:
        action = raw_input("please input your action: ")
        if action == 'login':
            login()

        elif action == 'register':
            register()

        elif action == 'quit':
            break;

        elif action == 'list':
            data = readFile(filename)
            printFormat(data)
            #print '222'

        elif action == 'help':
            help()

        else:
            pass

# 主函数
main()
