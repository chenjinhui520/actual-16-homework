#coding: utf-8

def f1():
    print 'hello world.'

def f2(x):
    print x

def f3(x, y):
    print x, y
    print x + y

def f4(x, y):
    return x + y

def f5(x, y):
    print 'x + y = ', x + y
    return x + y

# 位置参数
def f6(x, y):
    return y, x

def revererString(x, y):
    return y + ' ' + x

def new_raw_input(prompt):
    return prompt

# 默认参数
def f7(prompt=""):
    return prompt

f6('123', '456')

#name = f7('oplease input your name: ')
#print 'name: ', name

#f2('please input your name: ')

#f3(2, 5)

#s = f4(2, 5)
#print s

#s = f5(2, 5)
#print 's: ', s

#x, y = f6('hello', 'world')
#print x, y

#s = revererString('hello', 'world')
#print s

#name = new_raw_input("please input your name: ")
#print name

#ss = f6(2, 5)
#print ss 
