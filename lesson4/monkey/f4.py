#coding: utf-8

def f1():
    print "hello world"
    return True

# 位置参数
def f2(x, y):
    return x, y


def f3(x=100):
    print x

#print f1()

#print f2(1, 2)
#print f2(2, 1)

#print "---------------"

# 关键字参数
#print f2(x=1, y=2)
#print f2(y=2, x=1)

f3(x=True)


