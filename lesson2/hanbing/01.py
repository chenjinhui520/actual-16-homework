#!/usr/bin/env python
#coding=utf-8 
'''
选用Input作为输入   
input会将输入都作为INT（如果输入非整型将会跳出程序）
而raw_input会将输入作为字符串
'''
l = []
while 1:
	temp_num = input("Give Me A Number: ")
	if type(temp_num) == int:
		l.append(temp_num)
	if 0 in l:
		l.pop(-1)
		l.sort()
		print l
		break
