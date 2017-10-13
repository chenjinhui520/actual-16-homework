#!/usr/bin/env python
#coding=utf-8
log_h = open("./nginx_access.log",'r')
dict_ip = {}
dict_status = {}
dict_ip_url = {}
while True:
    line = log_h.readline()
    if line:
        line_list = line.split()
        ip = line_list[0]
        url = line_list[6]
        status= line_list[8]
        if ip not in dict_ip:
            dict_ip[ip] = 1
        else:
            dict_ip[ip]+=1
        if status not in dict_status:
            dict_status[status] = 1
        else:
            dict_status[status]+=1
        if ip not in  dict_ip_url:
            dict_ip_url[ip] = {}
            if url not in dict_ip_url[ip]:
                print ip,url
                dict_ip_url[ip][url] = 1           
        else:
            if url not in dict_ip_url[ip]:
                dict_ip_url[ip][url] = 1 
            else:
                dict_ip_url[ip][url] += 1
    else:
        break

print dict_ip
print dict_status
print dict_ip_url
