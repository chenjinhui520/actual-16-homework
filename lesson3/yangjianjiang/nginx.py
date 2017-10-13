#!/usr/bin/env python
#coding:utf-8
'''
需求: 处理NGINX ACCESS日志
实现：
1. 统计一个日志文件中不同状态码出现的次数；
2. 统计一个日志文件中不同IP出现的次数；
3. 统计同一个ip访问不同一个url的次数；

# 方式1
{
            '80.82.78.38 http://www.baidu.com/cache/global/img/gs.gif' : 2,
                '80.82.78.38 http://www.qq.com/404/search_children.js' : 5,
                    '80.82.78.100 http://www.baidu.com/cache/global/img/gs.gif' : 20,
                    }

# 方式2
> 添加 m['80.82.78.38']['http://www.reboot.com'] = 1 如果不存在就修改
{
            '80.82.78.38' : {
                              'http://www.baidu.com/cache/global/img/gs.gif' : 2,
                                            'http://www.qq.com/404/search_children.js' : 5,
                                                           },
                '80.82.78.100' : {
                                  'http://www.baidu.com/cache/global/img/gs.gif' : 20,
                                                 },
                }
'''
codes = {}
ips = {}
urls = {}
fd = open('/Users/joe/51reboot/doc/nginx_access.log')
data = fd.readlines()
#print data
#.split(' ')
for line in data:
    s = line.split(' ')
    ip_add = s[0]
    url = s[6]
    code = s[8]
    if code not in codes:
        codes[code] = 1
    else:
        codes[code] += 1
    if ip_add not in ips:
        ips[ip_add] = 1
    else:
        ips[ip_add] += 1

    if urls.has_key(ip_add + ' ' + url):
        urls[ip_add + ' ' + url] += 1
    else:
        urls[ip_add + ' ' + url] = 1
    

fd.close()
print "日志文件中不同状态码出现的次数如下："
print codes
print "日志文件中不同ip出现的次数如下："
print ips
print "日志文件中同一ip中不同url的次数如下"
print urls
