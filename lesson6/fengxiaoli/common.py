#!/usr/bin/env python
#coding: utf-8

import json


database='./store.db'
rememberme='./rememberme'

def WriteFile(registerInfo):
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    users.append(registerInfo)
    with open(database, 'w') as fd:
        fd.write(json.dumps(users))

def GetUsers():
    try:
        with open(database,'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
            users= []
    return users

def CheckUserExist(user,email):
    try:
        with open(database,'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
            users= []
    for u in users:
        if u['username'] == user or u['email'] == email:
            print 'user or email exist.'
            return 1
    return 0

def UpdateLoginCnt(user,count):
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    for u in users:
        if u['username'] == user:
            u['login_failed'] = count
            break

    with open(database, 'w') as fd:
        fd.write(json.dumps(users))

def GetLoginCnt(user):
    cnt = 0
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []

    for u in users:
        if u['username'] == user:
            cnt=u['login_failed']
            break
    return cnt

def DelUser(user):
    try:
        with open(database, 'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []
    index = 0
    for u in users:
        if u['username'] == user:
            users.pop(index)
            break
        index += 1

    with open(database, 'w') as fd:
        fd.write(json.dumps(users))

def rememberMe(saveuser):
    users = []
    users.append(saveuser)
    with open(rememberme, 'w') as fd:
        fd.write(json.dumps(users))


def getRememberMe():
    try:
        with open(rememberme,'r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
            users= []
    return users

