#!/usr/bin/env python
#coding:utf-8
'''
题目：
实现history
1. 不停的提示输入，如果输入quit exit q 退出。
2. 如果输入命令，则打印命令执行成功。
3. 输入history，显示要求和history命令一模一样。
4. 输入help，显示帮助信息。
'''
def counter_command(nums,command):
	l1 = " %d %s" %(nums,command)
	command_list.append(l1)
command_list = []
counter = 1
while True:
	command = raw_input('please input you command:')
	if command in "quit exit q":
		break
	elif command == 'history':
		counter_command(counter,command)
		counter += 1
		for x in command_list:
			print x
	elif command == 'help':
		counter_command(counter,command)
		counter += 1
		print " 1、输入quit，exit，q退出程序; \n 2、输入help以显示帮助信; \n 3、输入history显示命令历史。"
	else:
		counter_command(counter,command)
		counter += 1
		print "命令执行成功！"


