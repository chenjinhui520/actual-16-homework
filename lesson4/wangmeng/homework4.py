#!/usr/bin/env python
#coding:utf-8
'''
作业：
    需求：用户注册和用户登陆
    实现：
    1. 仿照Github登陆和注册用户。
    2. 注册用户填写注册信息，注册完成，提示用户注册成功。
    3. 登陆输入用户名和密码，验证成功，提示用户登陆成功信息；
        验证失败，提示错误的用户名和密码；
        连续输入错误3次，锁定用户，该用户不能在继续输入退出。
'''
#main函数为程序的入口函数，也称为主函数；
#用户退出程序前需要把数据持久化到文件中， 下次再运行该程序需要从磁盘文件中加载数据到内存中(也就是json.loads);
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
                #if i.split('|')[0] != name or i.split('|')[1] != passwd:
                if c >= 3:
                    print '<你已被锁定，请投案自首>'
                    a = 1
                    break
                else:
                    print '用户名或密码错误,请重新...'
                c += 1
    return a

def register():
    name = raw_input('请输入注册账号：').strip()
    passwd = raw_input('请输入注册密码：').strip()
    passwd2 = raw_input('请确认注册密码：').strip()
    if passwd == passwd2:
        email = raw_input('请输入注册邮箱：').strip()
        data = name + '|' + passwd + '|' + email 
        writeFile(filename,data)
        print '注册成功！'
    else:
        print '<两次输入密码不一致！>'

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

def printFormat(data, format=json):
    if format == "json":
        print json.dumps(data, indent=4)
    elif format == "xml":
        pass
    elif format == "table":
        '''
        username    |   email                   |   password
        monkey      |   monkey@51reboot.com     |   123456
        xiaoming    |   xiaoming@51reboot.com   |   123456
        '''
        pass
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
            register()
        elif action == 'quit' or action == 'q':
            break
        elif action == 'list':
            # 列出所有已注册的用户，并格式化输出，输出格式可以任意。
            if os.path.exists(filename) and os.path.getsize(filename):
                li = readFile(filename)
                print li
                print '\033[7;31m[所有已注册用户]:\033[0m'
                for i in li:
                    a,b,c = i.encode().split('|')
                    print '\t账号：%s\n\t密码：%s\n\t邮箱：%s' %(a,b,c)
                    print '-'*20
            else:
                print '没有数据库文件或数据库中无用户'
        elif action == 'help':
            helpp()

        else:
            pass
main()

