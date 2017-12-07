#!/usr/bin/env python
#coding:utf-8

from app.models import execute_sql
from app.models import select_all_result 
from app.models import select_one_result

def assets_get():
    sql = '''SELECT id,hostname,status,i_ip,e_ip,ram,hd,cpu,cpu_model,address,update_date FROM assets'''
    return select_all_result(sql)

def assets_add(data):
    print data
    sql = '''INSERT INTO assets(hostname,i_ip,e_ip,ram,hd,cpu,cpu_model,address) values('%s', '%s', '%s', %d, %d, %d, '%s','%s')''' % (data['hostname'], data['private_ip'], data['public_ip'],int(data["mem_total"]),int(data["disk"]),int(data["cpu_num"]),data["cpu_model"],data["machine_room"])
    return execute_sql(sql)

def assets_del(uid):
    sql = '''DELETE FROM assets WHERE id = %s; ''' % int(uid)
    return execute_sql(sql)

def assets_info(uid):
    sql = '''SELECT * FROM assets WHERE id = %s; ''' % uid
    return select_one_result(sql)
def assets_edit(**kwargs):
    sql = ''' UPDATE assets SET hostname="%s",i_ip="%s",e_ip="%s",ram=%d,hd=%d,cpu=%d,cpu_model="%s",address="%s" where id=%d;''' % (kwargs['hostname'],kwargs['private_ip'],kwargs['public_ip'],int(kwargs['mem_total']),int(kwargs['disk']),int(kwargs['cpu_num']),kwargs['cpu_model'],kwargs['machine_room'],int(kwargs['id']))
    return execute_sql(sql)

