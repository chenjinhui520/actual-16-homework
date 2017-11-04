#!/usr/bin/env python
#coding:utf-8
import json,os
filename = "store.db"
def login():
    flag = True
    a = 0
    c = 1
    new_l = []
    while flag:
        name = raw_input('请输入用户名：').strip()
        passwd = raw_input('请输入密码：').strip()
        if os.path.exists(filename) and os.path.getsize(filename):
            data_l = readFile(filename)
            for i in data_l:
                new_l.append(i.encode())
            for i in new_l:
                if i.encode().split('|')[0] == name and i.encode().split('|')[1] == passwd:
                    print '登录成功！'
                    flag = False
                    break
            else:
                if c >= 3:
                    print '<你已被锁定，请投案自首>'
                    a = 1
                    break
                else:
                    print '用户名或密码错误,请重新...'
                c += 1
        else:
            print '文件不存在或为空...'
            print '请先注册：>>>'
            register()
    return a

def register():
    name = raw_input('请输入注册账号：').strip()
    passwd = raw_input('请输入注册密码：').strip()
    passwd2 = raw_input('请确认注册密码：').strip()
    if passwd == passwd2:
        email = raw_input('请输入注册邮箱：').strip()
        data = name + '|' + passwd + '|' + email 
        writeFile(filename,data)
        a = '注册成功！'
    else:
        a = '<两次输入密码不一致！>'
    return a

def listt():
    # 列出所有已注册的用户，并格式化输出，输出格式可以任意。
    global y,x
    y = ''
    x = '-' * 20
    if os.path.exists(filename) and os.path.getsize(filename):
        li = readFile(filename)
        #print li
        print '\033[7;31m[所有已注册用户]:\033[0m'
        for i in li:
            a,b,c = i.encode().split('|')
            y += '\t账号：%s\n\t密码：%s\n\t邮箱：%s\n%s\n' %(a,b,c,x)
            #print '-'*20
    else:
        y = '没有数据库文件或数据库中无用户'
    return y

def writeFile(filename,data):
    if os.path.exists(filename) == False:
        l = []
        l.append(data)
        fd = open(filename,'w')
        json.dump(l,fd)
        fd.close()
    else:
        l = []
        l2 = readFile(filename)
        for i in l2:
            l.append(i.encode())
        l.append(data)
        fd = open(filename,'w')
        json.dump(l,fd)
        #fd.write(data)
        fd.close()

def readFile(filename):
    fd = open(filename, 'r')
    data = json.load(fd)
    #data = fd.read()
    fd.close()
    return data

def check_user_exists(username):
    if user is exits:
        return False
    else:
        return True
def authentication(username, password):
    '''
        如果用户名和密码验证成功 return True 否则 return False
    '''    
    return True # return False

def helpp():
    print
    print 'You Could Input:\n'
    print '\tlogin      ->[登录]\n'
    print '\tregister   ->[注册]\n'
    print '\tlist       ->[列出所有用户]\n'
    print '\tquit|q     ->[退出程序]\n'
    print '\thelp       ->[帮助信息]\n'

def main():
    while True:
        action = raw_input("please input your action[login|register|quit|list|help]: ")
        if action == 'login':
            a = login()
            if a:
                break
        elif action == 'register':
            a = register()
            print a
        elif action == 'quit' or action == 'q':
            break
        elif action == 'list':
            ret = listt()
            print y
        elif action == 'help':
            helpp()
        else:
            pass
#main()

