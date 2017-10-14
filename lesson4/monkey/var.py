


# 全局变量
name = 'monkey'
number = 99

def f1():
    # 局部变量
    name = "monkey func1"
    address = "bj"
    if name = "monkey":
        number = 100
    number += 100
    print "func1", name


def f2():
    number = 101
    print "func2", name, address, number

print name

f1()
f2()
