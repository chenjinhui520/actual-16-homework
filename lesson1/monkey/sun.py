#!/usr/bin/env python
#coding: utf-8


'''
raw_input('please input your num1: ')
raw_input('please input your num2: ')
raw_input('please input your num3: ')
raw_input('please input your num4: ')
raw_input('please input your num5: ')
print 1 + 2 + 3 + 4 + 5

1 + 2 + 3 + 4 + 5 = 15
'''
# 求和
num1 = raw_input('please input your num1: ')
num2 = raw_input('please input your num2: ')
num3 = raw_input('please input your num3: ')
num4 = raw_input('please input your num4: ')
num5 = raw_input('please input your num5: ')
print type(num1)
print num1 + num2 + num3 + num4 + num5
print int(num1) + int(num2) + int(num3) + int(num4) + int(num5)

# 格式化输出
'''
%s
1 + 2 + 3 + 4 + 5 = 15

'%s + %s ...= %s' % ()
'''
