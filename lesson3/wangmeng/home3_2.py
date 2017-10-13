#!/usr/bin/env python
#coding:utf-8
'''
作业2：
    需求: 处理NGINX ACCESS日志
    实现：
    1. 统计一个日志文件中不同状态码出现的次数；
    2. 统计一个日志文件中不同IP出现的次数；
    3. 统计同一个ip访问不同一个url的次数；
    # 方式1:
      添加 m['80.82.78.38']['http://www.reboot.com'] = 1 如果不存在就修改
    {
        '80.82.78.38' : {
                  'http://www.baidu.com/cache/global/img/gs.gif' : 2,
                  'http://www.qq.com/404/search_children.js' : 5,
                   },
        '80.82.78.100' : {
                  'http://www.baidu.com/cache/global/img/gs.gif' : 20,
                   },
    }
    # 方式2:
    {
        '80.82.78.38 http://www.baidu.com/cache/global/img/gs.gif' : 2,
        '80.82.78.38 http://www.qq.com/404/search_children.js' : 5,
        '80.82.78.100 http://www.baidu.com/cache/global/img/gs.gif' : 20,
    } 
'''
print
print '第一题'+'*'*50
print
#1
l = []
d = {}
f = open('nginx_access.log')
for i in f.readlines():
    l.append(i.split('"')[2].split()[0])
    for ii in l:
        d[ii] = l.count(ii)
f.close()
for iii in d:
    print "状态码['%s'] 出现 %s 次" %(iii,d[iii])
print
print '第二题'+'*'*50
print
#2
l = []
d = {}
f = open('nginx_access.log')
for i in f.readlines():
    l.append(i.split()[0])
f.close()
for ii in l:
    d[ii] = l.count(ii)
    print 'IP：%s \t出现 %s 次' %(ii,d[ii])
#####3
'''
l = []
d = {}
c = 1
f = open('nginx_access.log')
for i in f.readlines():
    if 'http' in i:
        l.append(i.split()[0])
        #d[i.split()[0]] = {i.split('GET ')[1].split()[0]:1}
        d = d.fromkeys(l,{})
        for j in d:
            if i.split()[0] == j:
                if d[j].get(i.split('GET ')[1].split()[0]) == None:
                    d[j][i.split('GET ')[1].split()[0]] = 1
            if d[j].get(i.split('GET ')[1].split()[0]):
                c += 1
                d[j][i.split('GET ')[1].split()[0]] = c
f.close()
print d
'''
print
print '第三题'+'*'*50
print
#3-2
l = []
d = {}
f = open('nginx_access.log')
for i in f.readlines():
    if 'http://' in i:
        l.append((i.split()[0],('http://'+i.split('http://')[1].split()[0].strip('"'))))
    if 'CONNECT' in i:
        l.append((i.split()[0],i.split('CONNECT')[1].strip().split()[0]))
f.close()
for j in l:
    #此时字典d中应为空
    if j[0] not in d:
        d[j[0]] = {j[1]:1}
    if j[0] in d and j[1] in d[j[0]]:
        d[j[0]][j[1]] += 1
for k,v in d.items():
    print k,v
