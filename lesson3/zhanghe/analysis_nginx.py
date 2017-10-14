#!/usr/bin/env python
# coding: utf-8
# @author: felix.zhang
# @version: 1.0

statusCode = {}
ipAddress = {}
ipUrl = {}

nginxLog = r'/home/hezhang/Desktop/nginx_access.log'

fd = open(nginxLog, 'r')
logs = fd.readlines()
fd.close()


# Analysis Status Code
for line in logs:
    l = line.split()
    #print l
    ip = l[0]
    s1 = l[-5]
    s2 = l[8]
    
    # Analysis IP
    if ip in ipAddress:
        ipAddress[ip] += 1
    else:
        ipAddress[ip] = 1


    # Analysis Status Code
    if s1.isdigit():
        if s1 in statusCode:
            statusCode[s1] += 1
        else:
            statusCode[s1] = 1
    elif s2.isdigit():
        if s2 in statusCode:
            statusCode[s2] += 1
        else:
            statusCode[s2] = 1
    else:
        continue


    #ip url
    ipUrl[ip] = {}





for i in ipUrl:
    for line in logs:
        l = line.split()
        ip = l[0]
        method = l[5]
        url = l[6]

        if ip == i:
            if 'GET' in method:
                if url in ipUrl[ip]:
                    ipUrl[ip][url] += 1
                else:
                    ipUrl[ip] = {url: 1}


    
        
#print ipUrl       
#print statusCode
#print ipAddress

#'''
# 统计排序
# Sorted DESC
statusCodeResult = sorted(statusCode.iteritems(), key=lambda v: v[1], reverse=True)
ipAddressResult = sorted(ipAddress.iteritems(), key=lambda v: v[1], reverse=True)

print "HTTP状态码统计排序结果"
print '-' * 19
print '|{:^8}|{:^8}|'.format('Code', 'Count')
for code, count in statusCodeResult:
    print '-' * 19
    print '|{:^8}|{:^8}|'.format(code, count)
else:
    print '-' * 19

print
print "IP地址统计排序结果"
print '-' * 28
print '| {:^17}|{:^8}|'.format('IP Address', 'Count')
for ip, count in ipAddressResult:
    print '-' * 28
    print '| {:<17}|{:^8}|'.format(ip, count)
else:
    print '-' * 28
#'''

print ipUrl       
