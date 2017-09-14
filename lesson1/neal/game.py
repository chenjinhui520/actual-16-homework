#!/usr/bin/env python
#coding: utf-8
import random
life = 4
i = 1
money = 0
while i < 9: 
	choice = float (random.random())
	print 'GM:闯关者，请迎接你的第%s关，你还有%s条命，有%s个金币' % (i,life,money)
	if choice < 0.5:
		money += 10
		if i == 8:
			print '闯关成功!你还有%s条命，有%s个金币' % (life,money)
			break
		print '你好，我的朋友，给你10金币，继续下一关吧！'
	elif choice > 0.4:
		life -= 1	
		print '去死吧！！贪婪的人类！！生命-1'
		if life == 0:
			print 'GAME OVER'
			break  
		elif i == 8:
			print '闯关成功!你还有%s条命，有%s个金币' % (life,money)
			break
	i += 1
