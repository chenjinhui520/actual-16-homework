#!/usr/bin/env python
# coding: utf-8

s = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

fmax = 0 # 第一大的数
smax = 0 # 第二大的数
for i in s:
	if i > fmax:
		fmax = i

for i in s:
	if i == fmax:
		continue

	if i > smax:
		smax = i
	

print "第一大的数: %s" % fmax
print "第二大的数: %s" % smax

