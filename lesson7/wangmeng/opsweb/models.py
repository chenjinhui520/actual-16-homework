#!/usr/bin/env python
#coding:utf-8

import MySQLdb as mdb
conn = mdb.connect(host='127.0.0.1', user='root', passwd='123456', db='wm', charset='utf8')
cursor = conn.cursor()
conn.autocommit(1)

def execute_sql(sql):
    return cursor.execute(sql)

def select_all_result(sql):
    cursor.execute(sql)
    return cursor.fetchall()

def select_user_exist(sql):
    cursor.execute(sql)
    return cursor.fetchall()

