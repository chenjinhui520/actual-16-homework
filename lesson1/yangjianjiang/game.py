#!/usr/bin/env python
#coding:utf-8

import random
life = 4 #四条命
num = 1 #初始关数
money = 0 #初始金币数0
while num <= 8:
	if life == 0:
		break
	print '你目前处于第%s关，你还有%s条命，你一共有%s金币' %(num,life,money)
	choice = int(random.random()*10)
	if choice < 5:
		money += 10
		print "你好，我的朋友，给你10个金币，继续下一关吧！"
	else:
		life -=1
		print "去死吧！！贪婪的人类"
	num += 1
if life > 0:
	print "恭喜你闯过所有关卡！"
else:
	print "你已经没命了，Game Over!!!!!"
