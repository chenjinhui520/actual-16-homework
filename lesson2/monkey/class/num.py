#!/usr/bin/env python
#coding:utf-8
#for d in range(1,11):
#    if d == 5 or d == 7 or d ==8:
#        pass
#    else:
#        print d
for num in range(10,0,-1):
	if num in [5,7,8]:
		continue
	print num
