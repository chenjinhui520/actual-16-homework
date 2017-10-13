#!/usr/bin/env python
#coding:utf-8
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
import sys
counter = 0 #记录输入错误次数
help_cmd = ["h","-h","help"]
register_cmd = ["r","-r","register"]
login_cmd = ["l","-l","login"]
quit_cmd = ["q","-q","quit"]
help_infos = '''
帮助信息如下：
h或者-h或者help    :	display help informantions
r或者-r或者register:	用户注册
l或者-l或者login   :	用户登陆
q或者-q或者quit    :    退出
'''
lock_list = []
username_list = []
register_info = {}


while True:
    cmd = raw_input("你想要做什么，请输入命令:")
    if cmd in register_cmd:
        print "欢迎光临本站，接下来是开始注册...."
        username = raw_input("please pick your name:")
        password = raw_input("please input your password:")
        email = raw_input("please input your email:")
        if username in username_list:
            print "你输入的用户名已存在，请重新输入。"
            username = raw_input("please pick your name:")
        if '@' not in email:
            print "你输入的邮箱格式不对，请重新输入"
            email = raw_input("please input your email:")
        register_info[username] = {"password":password,"email":email}
        username_list.append(username)
        print "用户%s 注册成功" %username
        print register_info
    elif cmd in login_cmd:
        username_login = raw_input("please input your login name:")	
        password_login = raw_input("please input your password:")
        #print username_login
        #print password_login
        if username_login not in username_list:
            print "用户名不存在，请重新登陆"
            username_login = raw_input("please input your login name:")	
            password_login = raw_input("please input your password:")
        elif username_login in lock_list:
    	    print "账户已锁定，请管理员解锁！"
    	    break
        else:
            while True:
                #print register_info
                if register_info[username_login]['password'] == password_login:
                    print "登陆成功"
                    break
                else:
                    counter += 1
                    if counter >= 3:
                        print "你已输入密码错误三次，已锁定"
                        lock_list.append(username_login)
                        break
                    else:
                        print "你输入的密码错误，请重新输入"
                        password_login = raw_input("please input your password:")
    elif cmd in quit_cmd:
        sys.exit()
    else:
        print "你输入的命令不对，请查看帮助信息"
        print help_infos

    		
	    
	  
