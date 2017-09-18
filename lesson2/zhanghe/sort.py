#!/usr/bin/env python
# coding: utf-8

l = []
while True:
	number = int(raw_input('please input a number: '))
	if number == 0:
		break
	else:
		l.append(number)


l.sort()

print 'Ascending:',
print ' -> '.join([str(i) for i in l])

l.reverse()
print 'Descending:',
print ' -> '.join([str(i) for i in l])

