#!/usr/bin/env python
#coding:utf-8
'''
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
    if ip_add not in ips:
        urls[ip_add]={url:1}
    elif urls[ip_add][url]:
        urls[ip_add][url] += 1


fd.close()
print "日志文件中同一ip中不同url的次数如下"
print urls
