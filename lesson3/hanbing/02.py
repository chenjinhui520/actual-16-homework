#!/usr/bin/env  python
#coding:utf-8

'''
吐槽一波这个日志格式不太规范
90%行第8个是状态码,少数第8行是'-'

'''




def tjztm():
    f = open('nginx_access.log')
    all_status = []
    status = []
    for s in f:
         tmp = s.split()
         all_status.append(tmp[8])
         if tmp[8] not in status:
             status.append(tmp[8])
    for i in range(len(status)):
        print '状态码 %s 的次数为 %s '%(status[i],all_status.count(status[i]))

    f.close()

def tjip():
    f = open('nginx_access.log')
    all_status = []
    status = []
    for s in f:
         tmp = s.split()
         all_status.append(tmp[0])
         if tmp[0] not in status:
             status.append(tmp[0])
    for i in range(len(status)):
        print 'IP %s 的次数为 %s '%(status[i],all_status.count(status[i]))

    f.close()


if __name__ == '__main__':
    tjztm()
    tjip()
