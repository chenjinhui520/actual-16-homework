## 作业1
> 改造lesson3作业1的用户注册、登录系统, 使用函数的方式。  

- 注意
1. main函数为程序的入口函数，也称为主函数；
2. 用户退出程序前需要把数据持久化到文件中， 下次再运行该程序需要从磁盘文件中加载数据到内存中(也就是json.loads);

```
#!coding: utf-8

import json

filename = "store.db"

def login():
    pass


def register():
    pass


def writeFile(filename, data):
    pass


def readFile(filename):
    return

def printJson(data):
    print json.dumps(data, indent=4)


def check_user_exists(username):
    if user is 存在:
        return False
    else:
        return True


def authentication(username, password):
    
    return True # return False


def main():
    pass


main()

```


