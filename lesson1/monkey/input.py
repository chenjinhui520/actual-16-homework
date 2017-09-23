#!/usr/bin/env python
#coding: utf-8

#name = 'monkey'
name = raw_input('请输入你的名字: ')
print name

sex = raw_input('please input your sex: ')
print sex 

age = raw_input('please input your age: ')
print age

"""
print name + male + age
"""
print name + ' ' + sex + ' ' +  age

'''
1. monkey male 11
2. My name is monkey, sex is male, age is 11.
'''
print 'My name is ' + name + ', sex is ' + sex + ', age is ' + age + '.'

# 格式化输出
print 'My name is %s, sex is %s, age is %s.' % (name, sex, age)
