#!/usr/bin/evn python
# coding=utf-8
import json
filename = 'C:\\Users\\Administrator\\PycharmProjects\\20171014\\personinfos.josn'
def register():
    username=raw_input('请输入用户名:')
    email=raw_input('请输入邮箱:')
    password=raw_input('请输入密码:')
    result=checkUser(username) #检查用户名是否存在于文件中
    if result==1:
        print '用户名已存在!'
    if result==0:
        userdict={}
        userdict[username]={
            'email':email,
            'password':password,
            'errortime':0
        }
        writerFile(userdict)
        print '%s注册成功'%(username)
        return userdict
def login():
    while 1:
        username = raw_input('请输入用户名:')
        password = raw_input('请输入密码:')
        result = readFile()
        if username in result.keys():
            if password == result[username]['password']:
                print '%s登录成功' % (username)
                result=readFile()
                result[username]['errortime']=0
                writerFile(result)
                break
            else:
                print '密码错误!'
                result=readFile()
                result[username]['errortime']+=1
                writerFile(result)
        else:
            print '用户 %s 不存在' % username
            break
        result=readFile()
        print 'errortime: %s'% result[username]['errortime']
        if result[username]['errortime'] >= 3:
            print '%s failed 3 times! account locked' % username
            break
def writerFile(userdict):
    result=dict(readFile())
    result.update(userdict)
    file_w=open(filename,'w')
    data=json.dumps(result)
    file_w.write(data)
    file_w.close()
def readFile():
    file_r=open(filename,'r')
    data=file_r.read()
    file_r.close()
    result = json.loads(data)
    return result
def checkUser(username):
    result=readFile()
    if result==None:
        return 0
    else:
        i = result.keys()
        if username in i:
            return 1
        else:
            return 0
if __name__ == '__main__':
    while 1:
        print ' 请选择1或2或3\n 1 register \n 2 login\n 3 exit'
        action = raw_input('action: ')
        if action == '1':
            register()
        elif action == '2':
            login()
        elif action == '3':
            break
        else:
            print '输入错误!'











