#coding: utf-8
'''
append
append(object) -- append object to end
1.追加对象至末尾
2.无返回值
3.示例
'''
arr1 = ['a', 1,]
arr1.append(['a', 'b', 'c',])
arr1.append(4)
print 'arr1.append:', arr1

'''
count
L.count(value) -> integer -- return number of occurrences of value
1.统计一个值出现的次数
2.有返回值
3.示例
'''
arr2 = ['a', 'b', 'c', 1, 4, 6, 'a', 'a', 'b']
print 'arr2.count:', arr2.count('a')

'''
extend
L.extend(iterable) -- extend list by appending elements from the iterable
1.通过可迭代的方式添加元素
2.无返回值
3.示例
'''
arr3 = ['a', 'b', 'c', 1, 4, 6, 'a']
count3 = [6, 6, 6, 2, 2, 2, 1]
arr3.extend(count3)
print 'arr3.extend', arr3

'''
index
L.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
1.返回一个值的第一个索引，如果值不存在，则返回一个错误
2.有返回值
3.示例
'''
arr4 = ['a', 'b', 'c', 1, 4, 6, 'a']
print 'arr4.index', arr4.index('a')

'''
insert
L.insert(index, object) -- insert object before index
1.在索引之前插入一个对象
2.无返回值
3.示例
'''
arr5 = ['a', 'b', 'c', 'ff', 4, 6, 'a']
count5 = ['neal', 'neal', 'love']
arr5.insert(3,count5)
print arr5

'''
pop
L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.
1.通过索引删除值，如果索引空，则删除最后值。
2.有返回值
3.示例
'''
arr6 = ['a', 'b', 'c', 'ff', 4, 6, 'a']
arr6.pop(3)
print arr6

'''
remove
L.remove(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.
1.删除第一次出现的值
2.无返回值
3.示例
'''
arr7 = ['a', 'b', 'c', 'ff', 4, 6, 'a']
print arr7.remove('a')

'''
reverse
L.reverse() -- reverse *IN PLACE*
1.反转排序
2.无返回值
3.示例
'''
arr8 = ['a', 'b', 'c', 'ff', 4, 6, 'a']
arr8.reverse() 
print arr8

'''
sort
L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1
1.列表排序，顺序
2.无返回值
3.示例
'''
arr9 = ['a', 'b', 'c', 'ff', 4, 6, 'a']
arr9.sort()
print arr9




