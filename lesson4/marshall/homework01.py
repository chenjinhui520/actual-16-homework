#!coding:utf-8

import json
import sys
filename = "store.db"

def login():
    wrong_d = {}
    user = raw_input("请输入用户名:")
    passwd = raw_input("请输入密码:")
    if authentication(user,passwd):
        print "用户名密码正确，登录成功"
    else:
        while True:
            print "用户名或者密码错误,请重新输入用户名密码:"
            user = raw_input("请输入用户名:")
            passwd = raw_input("请输入密码:")
            if authentication(user,passwd):
                print "用户名密码正确，登录成功"
                break
            else:
                try:
                    wrong_d[user] += 1
                except:
                    wrong_d[user] = 1
                if wrong_d[user] > 2:
                    print "登录失败"
                    break

def register():
    #注册用户，如发现用户已经存在则提示用户已经存在
    user = raw_input("请输入要注册的用户名:")
    check_user_exists(user)
    passwd = raw_input("请输入密码:")
    data = readFile(filename)
    data[user] = passwd
    writeFile(filename,data)

def writeFile(filename, data={}):
    fd = open(filename, 'w')
    data = json.dumps(data)
    fd.write(data)
    fd.close()

def readFile(filename):
    #读文件，如果发现文件不存在，则创建文件，文件记录空字典
    try:
        fd = open(filename, 'r')
        data = json.loads(fd.read())
        fd.close()
    except:
        data = {}
        writeFile(filename)

    return data

def printFormat(data, format="json"):
    if format == "json":
        print json.dumps(data, indent=4)

    elif format == "xml":
        print "<用户信息>"
        for key in data.keys():
            key = str(key)
            passwd = str(data[key])
            print "<用户名> %s </用户名>" %(key)
            print "<密码> %s </密码>" %(passwd)
        print "</用户信息>"

    elif format == "table":
        pass

def check_user_exists(user):
    data = readFile(filename)
    if data != {}:
        while user in data.keys():
            print "用户已经存在，请重新输入用户名:"
            user = raw_input("请输入要注册的用户名：")

def authentication(user,passwd):
    '''
        如果用户名和密码验证成功 return True 否则 return False
    '''
    data = readFile(filename)
    if user in data.keys() and passwd == data[user]:
        return True # return False
    else:
        return False
def help():
    print """请输入选择[1/2/3/4/5]:
    1:登录
    2:注册用户
    3:退出
    4:查询现有用户
    5:查看帮助
"""

def main():
    help()
    while True:
        action = raw_input("please input your action: ")
        if action == '1' or action == 'login':
            login()

        elif action == '2' or action == 'regist':
            register()

        elif action == '3' or action == "quit":
            sys.exit()

        elif action == '4' or action == "list":
            # 列出所有已注册的用户，并格式化输出，输出格式可以任意。
            data = readFile(filename)
            prompt = """请输入输出格式[json|xml|table]"""
            format_type=raw_input(prompt)
            printFormat(data,format_type)
        elif action == '5' or action == "help":
            help()
        else:
            pass

# 主函数
main()
