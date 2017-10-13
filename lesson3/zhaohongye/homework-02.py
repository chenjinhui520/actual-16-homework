#!/usr/bin/env python
#coding:utf-8
#author=zhy
#date= 0926

'''
需求: 处理NGINX ACCESS日志
实现：
1. 统计一个日志文件中不同状态码出现的次数；
2. 统计一个日志文件中不同IP出现的次数；
3. 统计同一个ip访问不同一个url的次数；
'''
def status_count():
    File = open('./nginx_access.log')
    data = File.readlines()
    File.close()
    status_dict = {}
    for line in data:
        if status_dict.has_key(line.split(' ')[8]) == False :
            status_dict[line.split(' ')[8]] = 1
        else:
            status_dict[line.split(' ')[8]] += 1
    print '状态码的字典如下：'
    print status_dict

def ip1_count():
    File = open('./nginx_access.log')
    data = File.readlines()
    File.close()
    ip1_dict = {}
    for line in data:
        if ip1_dict.has_key(line.split(' ')[0]) == False :
            ip1_dict[line.split(' ')[0]] = 1
        else:
            ip1_dict[line.split(' ')[0]] += 1
    print 'IP的字典如下：'
    print ip1_dict



'''
# 方式1
{
    '80.82.78.38 http://www.baidu.com/cache/global/img/gs.gif' : 2,
    '80.82.78.38 http://www.qq.com/404/search_children.js' : 5,
    '80.82.78.100 http://www.baidu.com/cache/global/img/gs.gif' : 20,
}
'''

def ip_count():
    File = open('./nginx_access.log')
    data = File.readlines()
    File.close()
    ip_dict = {}
    for line in data:
        if ip_dict.has_key(line.split(' ')[0] + ' ' + line.split(' ')[6])  == False:
            ip_dict[line.split(' ')[0] + ' ' + line.split(' ')[6]] = 1
        else:
            ip_dict[line.split(' ')[0] + ' ' + line.split(' ')[6]] += 1
    print 'IP + 状态码 的字典如下：'
    print ip_dict

if __name__ == '__main__':
    status_count()
    ip1_count()
    ip_count()
