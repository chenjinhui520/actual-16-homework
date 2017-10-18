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
    fd = open(filename, 'w')
    fd.write(data)
    fd.close()


def readFile(filename):
    fd = open(filename, 'r')
    data = fd.read()
    fd.close()
    return data


def printFormat(data, format=json):
    if format == "json":
        print json.dumps(data, indent=4)

    elif format == "xml":
        pass

    elif format == "table":
        pass


def check_user_exists(username):
    if user is 存在:
        return False
    else:
        return True


def authentication(username, password):
    '''
        如果用户名和密码验证成功 return True 否则 return False
    '''    
    return True # return False

def help():
    pass


def main():
    while True:
        action = raw_input("please input your action: ")
        if action == 'login':
            pass

        elif action == 'register':
            pass

        elif action == 'quit':
            pass

        elif action == 'list':
            # 列出所有已注册的用户，并格式化输出，输出格式可以任意。
            pass

        elif action == 'help':
            pass

        else:
            pass

# 主函数
main()
```

- 注意 

```
lesson4的函数章节，非常、非常、非常重要！！！

***** 重要
位置参数、默认值参数、关键字参数
lambda 匿名函数

** 已经过时内置函数，只需要知道用法，不需要深入了解，因为生产项目中禁止使用
特殊函数: map/reduce/filter/zip

```

## 参考代码
> 如何手动实现内置的range函数，以及range函数的参数

```
#coding: utf-8
#filename: monkey.py


'''
如果手动实现简单版的range函数
'''


def rrange(*args):
    '''
    rrange(stop) -> list of integers
    rrange(start, stop[, step]) -> list of integers
    '''
    ret = []

    if len(args) == 1:
        start, stop, step = 0, args[0], 1
        ret = counter_range(start, stop, step)

    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
        ret = counter_range(start, stop, step)

    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
        ret = counter_range(start, stop, step)

    else:
        ret = "rrange expected at most 3 arguments, got %d" % len(args)

    return ret

def counter_range(start, stop, step):

    counter_ret = []
    while start < stop:
        counter_ret.append(start)
        start += step
    return counter_ret


if __name__ == '__main__':
    print rrange(10)
    print rrange(10, 21)
    print rrange(10, 21, 2)
```

> 调用和执行结果
```
(python27env) [root@l-monkey@gmail monkey]# ll monkey.py 
-rw-r--r-- 1 root root 929 10月 18 13:24 monkey.py
(python27env) [root@l-monkey@gmail monkey]# ipython
WARNING: IPython History requires SQLite, your history will not be saved
Python 2.7.10 (default, Aug 25 2017, 15:33:18) 
Type "copyright", "credits" or "license" for more information.

IPython 1.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import monkey

In [2]: monkey.rrange?
Type:       function
String Form:<function rrange at 0x7f37f4223320>
File:       /root/reboot16/actual-16-homework/lesson5/monkey/monkey.py
Definition: monkey.rrange(*args)
Docstring:
rrange(stop) -> list of integers
rrange(start, stop[, step]) -> list of integers

In [3]: monkey.rrange(10)
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [4]: monkey.rrange(1, 10)
Out[4]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

In [5]: monkey.rrange(1, 10, 2)
Out[5]: [1, 3, 5, 7, 9]
```

## lesson3的第二个作业的第二个方式
```
#coding: utf-8

import json


def counterLog(filename):
    ret = {}
    with open(filename, 'r') as fd:
        for line in fd:
            token = line.split()
            src_ip = token[0]
            target_url = token[6]
            if src_ip in ret:
                if target_url in ret[src_ip]:
                    ret[src_ip][target_url] += 1
                else:
                    ret[src_ip][target_url] = 1
            else:
                ret[src_ip] = { target_url : 1 }
    return ret

def printJson(data):
    print json.dumps(data, indent=4)


if __name__ == '__main__':
    data = counterLog('logs/access.log')
    printJson(data)
```
