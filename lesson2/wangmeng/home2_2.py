#/usr/bin/env python
#coding:utf-8
import os
l = []
while True:
    con = raw_input('please input command:')
    if con == 'quit' or con == 'exit' or con == 'q':
        print 'quit'
        break
    elif con == 'history':
        l.append(con)
        for i in l:
            print "%s %s" %(l.index(i)+1,i)
    elif con == 'help':
        print os.system(con)
    else:
        print "命令执行成功:<%s>" % con
        l.append(con)
