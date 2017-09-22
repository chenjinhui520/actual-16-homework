#!/usr/bin/env python
# coding: utf-8

arr=[]
while True:
    str = raw_input("[root@bogon 2]# ")
    if str == 'history':
        arr.append(str)
        for j in range(len(arr)):
            print ' %d %s' % ((j+1),arr[j])
    elif str == 'q':
        break
    elif str == 'quit':
        break
    elif str == 'exit':
        break
    elif str.startswith('help'):
        if str.endswith('L.append'):
            print "Docstring: L.append(object) -- append object to end"
            print "1. 追加对象到末尾"
            print "2. 无返回值"
            print "3. 示例"
            print "list.append('a')"
        elif str.endswith('S.strip'):
            print "Docstring: S.strip([chars]) -> string or unicode"
            print "1. 返回去掉头尾空格的字符串副本"
            print "2. 有返回值"
            print "3. 示例"
            print "str.strip()"
        elif str.endswith('S.lstrip'):
            print "Docstring: S.lstrip([chars]) -> string or unicode"
            print "1. 返回去掉左边空格的字符串副本"
            print "2. 有返回值"
            print "3. 示例"
            print "str.lstrip()"
        elif str.endswith('S.rstrip'):
            print "Docstring: S.rstrip([chars]) -> string or unicode"
            print "1. 返回去掉右边空格的字符串副本"
            print "2. 有返回值"
            print "3. 示例"
            print "str.rstrip()"
        elif str.endswith('S.find'):
            print "Docstring: S.find(sub [,start [,end]]) -> int"
            print "1.查找sub字符在字符串的位置"
            print "2. 返回sub所在索引，失败返回-1"
            print "3. 示例"
            print "str.find('a')"
            print "str.find('a',1,3)"
        elif str.endswith('S.join'):
            print "Docstring: S.join(iterable) -> string"
            print "1. 将序列中的元素以指定的字符串连接成新的字符串"
            print "2. 返回字符串"
            print "3. 示例"
            print "str.join('abc')"
        elif str.endswith('S.lower'):
            print "Docstring: S.lower() -> string"
            print "1. 返回转换成小写的字符串副本"
            print "2. 返回字符串"
            print "3. 示例"
            print "str.lower()"
        elif str.endswith('S.upper'):
            print "Docstring: S.upper() -> string"
            print "1. 返回转换成大写的字符串副本"
            print "2. 返回字符串"
            print "3. 示例"
            print "str.upper()"
        elif str.endswith('S.replace'):
            print "Docstring: S.replace(old, new[, count]) -> string"
            print "1. 用new字符串替换old字符串"
            print "2. 返回字符串"
            print "3. 示例"
            print "str.replace(str1,str2)"
            print "str.replace(str1,str2,count)"
        elif str.endswith('S.startswith'):
            print "Docstring: S.startswith(prefix[, start[, end]]) -> bool"
            print "1. 检查字符串是否以某个字符串开始"
            print "2. 匹配则返回true，否则flas"
            print "3. 示例"
            print "str.startswith(str)"
            print "str.startswith(str,start,end)"
        elif str.endswith('S.endswith'):
            print "Docstring: S.endswith(prefix[, start[, end]]) -> bool"
            print "1. 检查字符串是否以某个字符串结尾"
            print "2. 匹配则返回true，否则flas"
            print "3. 示例"
            print "str.endswith(str)"
            print "str.endswith(str,start,end)"
        elif str.endswith('S.count'):
            print "Docstring: S.count(sub[, start[, end]]) -> int"
            print "1. 返回字符串sub在S里出现的次数"
            print "2. 返回出现的次数"
            print "3. 示例"
            print "str.count(str1)"

    else:
        print "command %s execute successfully" % str
    arr.append(str)





