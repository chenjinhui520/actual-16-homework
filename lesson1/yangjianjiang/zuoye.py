#!/usr/bin/env python
#coding:utf-8
a=0
b=0
s=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for x in s:
	if x > a:
		a = x
for y in s:
	if y == a:
		continue
	if y >b:
		b = y
print "最大值是:",a
print "第二大值是:",b
