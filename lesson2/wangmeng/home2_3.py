#!/usr/bin/env python
#coding:utf-8
# 列表list的9个方法[解释]：
#1
'''
l.append?
    Docstring: L.append(object) -- append object to end
    Type:      builtin_function_or_method
    (1)追加对象到末尾(一个参数)
    (2)无返回值
    (3)示例：
     l = []
     l.append('hello')
     l.append(123)
     l.append(True)
     l.append([1,2,'rr'])
     print 'append:',l
'''
#2
'''
l.count?
    Docstring: L.count(value) -> integer -- return number of occurrences of value
    Type:      builtin_function_or_method
    (1)返回列表中的某个值出现的次数
    (2)有返回值
    (3)示例：
    l = [1,3,3,3,True,'w','w']
    l.count(3)
    l.count('w')
    l.count(1)
    注意:此处数值1会被默认为True返回，同样，True也被默认为1返回。
'''
#3
'''
l.extend?
    Docstring: L.extend(iterable) -- extend list by appending elements from the iterable
    Type:      builtin_function_or_method
    (1)通过添加可迭代对象中的元素来扩展本列表
    (2)无返回值
    (3)示例：
    l = [1,True,'qqq']
    t = (55,66)
    l2 = [[1,2,3]]
    l.extend(t)
    l.extend(l2)
'''
#4
'''
l.index?
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
    Type:      builtin_function_or_method
    (1)返回列表中所含有的元素第一次出现的索引值，参数为要查询的元素，若该元素不存在，会提示ValueError。可用索引指定范围，但不包含结束。
    (2)有返回值
    (3)示例：
    l = [2,3,3,True,'',True]
    l.index(3)
    l.index(5)
    l.index(True,4,5) #报错
    l.index(True,4,)  #正常
'''
#5
'''
l.insert?
    Docstring: L.insert(index, object) -- insert object before index
    Type:      builtin_function_or_method
    (1)在列表中某索引处前面插入对象，参数为索引值和对象
    (2)无返回值
    (3)示例：
    l = [2,3,3,True,'',True]
    l.insert(2,'haha')
    l.insert(-1,'haha')
'''
#6
'''
l.pop?
    Docstring: L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
    Type:      builtin_function_or_method
    (1)移除并返回列表中的某个元素，默认移除最后一个。参数为索引。如果列表为空或索引超出范围，则报IndexError。
    (2)有返回值
    (3)示例：
    l = [1,2,3,'tt',True]
    l.pop(1)
    l.pop()
    l.pop()
'''
#7
'''
l.remove?
    Docstring:
    L.remove(value) -- remove first occurrence of value.
    Raises ValueError if the value is not present.
    Type:      builtin_function_or_method
    (1)移除列表中你所指定的第一次出现的某个值，如果该值不存在，则报ValueError。
    (2)无返回值
    (3)示例：
    l = [1, 'yyy', 666, 'hello', 666]
    l.remove(666)
'''
#8
'''
l.reverse?
    Docstring: L.reverse() -- reverse *IN PLACE*
    Type:      builtin_function_or_method
    (1)列表元素原地反转
    (2)无返回值
    (3)示例：
    l = [1, 'yyy', 'hello']
    l.reverse()
    ['hello', 'yyy', 1]
'''
#9
'''
l.sort?
    Docstring:
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1
    Type:      builtin_function_or_method
    (1)对列表中元素[一般数值]进行升序排序
    (2)无返回值
    (3)示例：
    l = [3,4,7,5,88,-44,5,2,-1]
    l.sort()
    [-44, -1, 2, 3, 4, 5, 5, 7, 88]
'''






