#/usr/bin/env python
#coding:utf-8
l = []
while True:
    con = int(raw_input('please input a integer:'))
    if con == 0:
        print "It's OVER!"
        break
    else:
        l.append(con)
        l.sort()
print l

