#!/usr/bin/env python
#coding:utf-8
'''
作业1：
    需求：用户注册和用户登陆
    实现：
    1. 仿照Github登陆和注册用户。
    2. 注册用户填写注册信息，注册完成，提示用户注册成功。
    3. 登陆输入用户名和密码，验证成功，提示用户登陆成功信息；
        验证失败，提示错误的用户名和密码；
        连续输入错误3次，锁定用户，该用户不能在继续输入退出。
'''
import os
c = 1
ppp = True
while ppp:
    point = raw_input('老用户请登录[login]|新用户请注册[register]|退出[exit]：').strip()
    if point == 'exit':
        break
    if point == 'login':
        while ppp:
            name = raw_input('请输入用户名：').strip()
            passwd = raw_input('请输入密码：').strip()
            if os.path.exists('register') and os.path.getsize('register') != 0:
                with open('register') as fd:
                    for line in fd.readlines():
                    #n,p,e = fd.read().split('|')
                        if '|' in line and line.strip().split('|')[0] == name and line.strip().split('|')[1]  == passwd:
                            print '登录成功yep！'
                            break
                        else:
                            print '用户名或密码错误...'
                            if c != 3:
                                continue
                            else:
                                print '连续3次输入错误！[你已被锁定]！请到公安局自首..'
                                break
                    ppp = False
                    break
    if point == 'register':
        name = raw_input('请填写用户名：').strip()
        passwd = raw_input('请填写密码：').strip()
        email = raw_input('请填写注册邮箱(格式[wie984@....com])：').strip()
        f = open('register','a')
        f.write(name+'|'+passwd+'|'+email+'\n')
        f.close
    c += 1
'''
作业2：
    需求: 处理NGINX ACCESS日志
    实现：
    1. 统计一个日志文件中不同状态码出现的次数；
    2. 统计一个日志文件中不同IP出现的次数；
    3. 统计同一个ip访问不同一个url的次数；
    
    # 方式1:
      添加 m['80.82.78.38']['http://www.reboot.com'] = 1 如果不存在就修改
    {
        '80.82.78.38' : {
                  'http://www.baidu.com/cache/global/img/gs.gif' : 2,
                  'http://www.qq.com/404/search_children.js' : 5,
                   },
        '80.82.78.100' : {
                  'http://www.baidu.com/cache/global/img/gs.gif' : 20,
                   },
    }
    # 方式2:
    {
        '80.82.78.38 http://www.baidu.com/cache/global/img/gs.gif' : 2,
        '80.82.78.38 http://www.qq.com/404/search_children.js' : 5,
        '80.82.78.100 http://www.baidu.com/cache/global/img/gs.gif' : 20,
    } 
'''
'''
作业3：
    理解冒泡排序，不看上课代码，手写冒泡排序。  
'''


