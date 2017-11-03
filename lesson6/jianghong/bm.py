#coding: utf-8
import os
import json
def createDBfile(file):
    if not os.path.exists(file):
        with open(file, 'w') as fd:
            json.dump({}, fd)
        return True
    return False


def loadData(file):
    '''
    load data file from dbfile
    '''
    with open(file, 'r') as fd:
        data = json.load(fd)
    return data


def saveData(data, file):
    '''
    save data to dbfile
    '''
    with open(file, 'w') as fd:
        json.dump(data, fd)
    return 0


def checkUsername(users, username):
    '''
    return code: 
    1: username is null
    2: username is exist
    0: username ok
    '''
    if not username:
        return 1
    if username in users:
        return 2
    return 0

def checkEmail(users, email):
    '''
    return code: 
    1: email is null
    0: email ok
    '''
    if not email:
        return 1
    return 0


def checkPassword(users, password):
    '''
    return code: 
    1: password is null
    0: password ok
    '''
    if not password:
        return 1
    return 0

    
def login(file, username, password):
    loginResult = False
    users = loadData(file)
    checkUserResult = checkUsername(users, username)
    checkPasswordResult = checkUsername(users, password)

    if checkUserResult == 1:
        info = u'用户名不能为空'
    elif checkUserResult == 0:
        info = u'该用户不存在'
    elif checkPasswordResult == 1:
        info = u'密码不能为空'
    else:
        if users[username][-1] == password:
            info = u'用户 %s 登录成功' % username
            loginResult = True
        else:
            info = u'密码输入错误'
    return (loginResult, info)


def register(file, userData):
    registerResult = False
    users = loadData(file)
    username, email, password = userData['username'], userData['email'], userData['password']

    checkUserResult = checkUsername(users, username)
    checkEmailResult = checkUsername(users, email)
    checkPasswordResult = checkUsername(users, password)

    if checkUserResult == 1:
        info = u'用户名不能为空'
    elif checkUserResult == 2:
        info = u'用户名已经存在'
    elif checkEmailResult == 1:
        info = u'邮箱不能为空'
    elif checkPasswordResult == 1:
        info = u'密码不能为空'
    else:
        users[username] = [0, email, password]
        saveData(users, file)
        registerResult = True
        info = u'用户 %s 注册成功' % username
    return (registerResult, info)
