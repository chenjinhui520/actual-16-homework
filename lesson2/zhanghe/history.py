#!/usr/bin/env python
#coding: utf-8

import os

commands = []
quitCommand = ['quit', 'q', 'exit']

def help():
	print '''
 1. 输入quit或q或exit退出程序
 2. 输入history查看命令历史
'''

def showCommands():
	commands.append('history')
	for line in range(len(commands)):
		print '{:>4}  {}'.format(line+1, commands[line])


while True:
	command = raw_input('Please input command: ')
	if command == 'help':
		help()
		continue

	if command in quitCommand:
		print 'Quit'
		break
	if command == 'history':
		if len(commands) == 0:
			print '历史命令为空'
		else:
			showCommands()
	else:
		commands.append(command)
		exitStatus = os.system(command)
		if exitStatus == 0:
			print '命令执行成功'
		else:
			print '命令执行失败'



