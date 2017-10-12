#!/usr/bin/env python
#coding:utf-8

'''
需求: 处理NGINX ACCESS日志
实现：
1. 统计一个日志文件中不同状态码出现的次数；
2. 统计一个日志文件中不同IP出现的次数；
3. 统计同一个ip访问不同一个url的次数；
'''
codedict={}
ipdict={}
ipurldict={}

fd=open('./nginx_access.log')
#netinfo={}
line=fd.readline()
while line:
    if 'www.' in line:
        tmplist=line.split(' ')
        ip=tmplist[0]
        tmplist=line.split('"')
        list2=tmplist[1].split(' ')
        url=list2[1]
        list2=tmplist[2].split(' ')
        code=list2[1]
        #netinfo={'ip' : ip,'url' : url, 'code' : code}
        if codedict.has_key(code):
            codedict[code]+=1
        else:
            codedict[code]=1
        if ipdict.has_key(ip):
            ipdict[ip]+=1
        else:
            ipdict[ip]=1
        
        if ipurldict.has_key(ip):
            if ipurldict[ip].has_key(url):
                ipurldict[ip][url]+=1
            else:
                ipurldict[ip][url]=1
        else:
            ipurldict[ip]={url:1}
    line=fd.readline()

fd.close()
print '日志文件中不同状态码出现的次数：'
print codedict
print '日志文件中不同IP出现的次数'
print ipdict
print '同一个ip访问不同一个url的次数'
print ipurldict
