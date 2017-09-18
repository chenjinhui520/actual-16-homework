#!/usr/bin/env python
#coding:utf-8
'''
作业题目：
输入一系列的整数，输入0 表示输入结束
排序输出(升序)
'''
num_list=[] #空列表，用来存储输入的整数
while True:
	num = int(raw_input('please input a iteger num,Enter 0 to exit:'))
	if num == 0:
		break
	num_list.append(num)
#print 'Your input nums:',num_list
num_list.sort()
print 'Your input nums after sort',num_list
