#!/usr/bin/env python
# coding: utf-8

# 导入random模块
import random

life = 4 # 定义命数
shut = 8 # 游戏关数
select = ['left', 'right']
coins = 0

while life > 0:
	randomChoice = random.choice(select)
	while True:
		userChoice = raw_input('请输入您要进入的洞口 [left(左), right(右)](如left): ')
		if userChoice not in select:
			print '无效的选择，请重新选择...'
			continue
		else:
			break

	if userChoice == randomChoice:
		print '您好，我的朋友，送给你10个金币，继续下一关吧！'
		coins += 10
		shut -= 1
	else:
		print '去死吧！贪婪的人类！'
		life -= 1
	#	coins = 0

	if shut == 0:
		print '干的不错，您已通关'
		break
	else:
		print '您还有%s条命，共有金币%s个, 还剩下%s关' % (life, coins, shut)

	print 
else:
	print '我还会再回来的......'