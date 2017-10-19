#!/usr/bin/env python
#!coding: utf-8

import json
import sys
quit_cmd = ['q','quit','exit']
storename = 'store.db'
count = 0
error_counter = {}
black_list = 'black.txt'
def add_blacklist(username):
    with open(black_list,'a') as f:
        f.write(str(username)+'\n')
    return True
def in_blacklist(username):
    with open(black_list,'r') as f:
        for line in f:
            if username == line.strip():
                return True
    return False

def login():
    global count
    user_name = raw_input('请输入用户名:')
    if in_blacklist(user_name) :
        print "用户名%s已被锁定，禁止登陆"%user_name
        return False
    else:
        password = raw_input('请输入密码：')
        if authentication(user_name,password):
            print "登录成功"
        else:
            count += 1
            error_counter.update({user_name:count})
            while True:
                print "您输入的密码错误，请重新输入"
                password = raw_input('请输入密码：')
                if authentication(user_name,password):
                    print "登录成功"
                    break
                else:
                    count +=1
                    error_counter.update({user_name:count})
                    if error_counter[user_name] >= 3:
                        add_blacklist(user_name)
                        print "用户已被锁定，请更换用户输入"
                        break

def register():
    user_name = raw_input('输入用户名:')
    while check_user_exists(user_name):
        user_name = raw_input('输入用户名:')
    email = raw_input('输入邮件地址:')
    password = raw_input('输入密码:')
    try:
        #print user_name
        #print email
        #print password
        old_data = readFile(storename)
        #print 'old:',old_data
        reg_data = {user_name:{'password':password,'email':email}}
        #print type(old_data)
        #print type(reg_data)
        old_data.update(reg_data)
        #print 'new:',old_data
    except:
        old_data = {user_name:{'password':password,'email':email}}
        #print old_data
    writeFile(storename,old_data)
    return "您已注册成功"



def writeFile(filename, data):
    fd = open(filename,'w')
    try:
        fd.write(json.dumps(data))
    except:
        pass
    fd.close()
    

def readFile(filename):
    fd = open(filename,"r+")
    try:
        data = json.loads(fd.read())
    except:
        data = ''
    fd.close()
    return data
def printJson(data):
    print json.dumps(data, indent=4)


def check_user_exists(username):
    user_data = readFile(storename)
    if username in user_data:
        print  "你输入的用户已存在，请重新输入"
        return True
def authentication(username, password):
    try:
        data = readFile(storename)
    except:
        pass 
    if username in data and password == data[username]['password']:
        return True
    else:
        return False 

def help():
    return  '''
    请输入你的操作指令：[1|2|q|quit|exit]：
    1：注册
    2：登录
    q|quit|exit:退出系统
    other:帮助信息
    '''
def main():
    #print help()
    while True:
        cmd = raw_input('请输入你的指令,1:注册，2：登陆,q或者quit或者exit：退出本系统:')
        if cmd == '1':
            print register()
        elif cmd == '2':
            login()
        elif cmd in quit_cmd:
            sys.exit()
        else:
            print help()
main()
    
