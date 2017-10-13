#!/usr/bin/evn python
#coding=utf-8
users = {}
wrong_time = 3
def regist():
    user_name = raw_input("请输入注册用户名:")
    passwd = raw_input("请输入注册密码:")
    users.update({user_name:passwd})

def login(wrong_time):
    user_name = raw_input("请输入登录用户名:")
    passwd = raw_input("请输入登录密码:")
    if  users.get(user_name)==passwd:
        print "登录成功"
        return("succ")
    else:
        print("登录失败 您还有%d次登录机会"%(wrong_time-1))
        wrong_time-=1
    return wrong_time 
while True:
    action=raw_input("请输入操作项 1 为注册 2为登录:")
    if action == "1":
        regist()
    if action == "2":
        if login(wrong_time) == 'succ':
            break
        else:
            wrong_time-=1
    if wrong_time < 1 :
        print "失败次数过多，禁止登录"
        break
