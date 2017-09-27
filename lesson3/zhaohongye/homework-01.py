#!/usr/bin/env python
#coding:utf-8
#author=zhy
#date= 0926

'''
需求：用户注册和用户登陆
实现：
1. 仿照Github(https://github.com)登陆和注册用户。
2. 注册用户填写注册信息，注册完成，提示用户注册成功。
3. 登陆输入用户名和密码，验证成功，提示用户登陆成功信息；
   验证失败，提示错误的用户名和密码；
   连续输入错误3次，锁定用户，该用户不能在继续输入退出；

注意：
本次作业不需要将用户信息写入到文件.
'''
#注册列表
user = []
#登录错误次数
count = 0
#退出操作
quit = ['quit','exit','q']
#action
Action = ['register','login']
#帮助手册
Help = '''
help           -- 帮助手册
register       -- 注册账号
login          -- 登录账号
quit、exit、q  -- 退出
'''
while True:
    action = raw_input('please tell me what your wants: ')
    if action in quit:
        print '退出成功'
        break
    if  action not in Action:
        print Help
    if action == 'register':
        print '注册账号'
        Username = raw_input('Pick a uername: ')
        Email = raw_input('you@example.com: ')
        Password = raw_input('Create a password: ')
        Username_dict = {'Username':Username,'Email':Email,'Password':Password}
        user.append(Username_dict)
        print '用户信息如下 %s'  % Username_dict
        print '注册完成'
    if action == 'login':
        print '登录账号'
        Username_login = raw_input('Username or email address: ')
        Password_login = raw_input('Password: ')
        for i in user:
            if count >= 3:
                print '用户已锁定！'
                break
            elif i['Username'] == Username_login or i['Email'] == Username_login:
                if i['Password'] == Password_login:
                    print '验证成功'
                else:
                    print '验证失败，请重新登录！'
                    count += 1
                    print '登录错误次数：%s' % count
            else:
                print '用户不存在’' 
