# 列表方法概述
* list.append(object)
```
作用：将object增加到列表末尾。
返回值：无返回值
```

```
示例：
In [1]: a = range(5)

In [2]: a
Out[2]: [0, 1, 2, 3, 4]

In [3]: a.append(6)

In [4]: a
Out[4]: [0, 1, 2, 3, 4, 6]

In [5]: 

```

* list.count(value)
```
作用：统计value在list中出现的次数
返回值：value在list中出现的次数，整型
```

```
示例：

In [8]: a
Out[8]: [0, 1, 2, 3, 4, 6]

In [9]: a.count(2)
Out[9]: 1

In [10]: a.count(5)
Out[10]: 0

In [11]: 
```

* list.extend(iterable)
```
作用：将可迭代对象iterable中的每一个元素增加到列表的末尾，从而扩充列表。
返回值：无返回值
```

```
In [13]: a
Out[13]: [0, 1, 2, 3, 4, 6]

In [14]: b= range(10,16)

In [15]: a.extend(b)

In [16]: a
Out[16]: [0, 1, 2, 3, 4, 6, 10, 11, 12, 13, 14, 15]

In [17]: 

查看返回值：
In [17]: print a.extend(b)
None

In [18]:

注意：在python中，如果没有返回值，则默认返回None
```


* list.index(value, [start, [stop]]) 
```
作用：返回value在list中第一次出现的索引。
    如果没有指定start和stop，则表示从开始到结束。
    如果只指定了start，没有stop，则表示从指定的start开始，到结尾结束。
返回值：如果value在list中，则返回整型，表示value在list中的索引位置，否则引发ValueError错误。
```

```
示例：

In [55]: a.index(2)
Out[55]: 2

In [56]: a.index(1)
Out[56]: 1

In [57]: a.index(5)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-57-1e3117811f1f> in <module>()
----> 1 a.index(5)

ValueError: 5 is not in list

In [58]: 

```


* list.insert(index, object)
```
作用：在index的前面插入对象object。
    如果index的绝对值大于当前列表的长度，为正值，则表示在列表的末尾添加元素。
    如果index的绝对值大于当前列表的长度，为负值，则表示在列表的开头添加元素。
```


```
示例：

In [59]: a
Out[59]: [0, 1, 2, 3, 4]

In [60]: a.insert(-9999, 10)

In [61]: a
Out[61]: [10, 0, 1, 2, 3, 4]

In [62]: a.insert(9999, 20)

In [63]: a
Out[63]: [10, 0, 1, 2, 3, 4, 20]

In [64]: a.insert(-1, 5)

In [65]: a
Out[65]: [10, 0, 1, 2, 3, 4, 5, 20]

In [66]: 
```

* list.pop([index])
```
作用：从列表中删除索引为index的元素。如果index省略，则删除最后一个元素。

返回值：被删除的元素。

注意：如果指定的index超过列表的长度，则引发IndexError的异常。
```

```
示例：

In [69]: a
Out[69]: [10, 0, 1, 2, 3, 4, 5, 20]

In [70]: a.pop()
Out[70]: 20

In [71]: a
Out[71]: [10, 0, 1, 2, 3, 4, 5]

In [72]: a.pop(0)
Out[72]: 10

In [73]: a
Out[73]: [0, 1, 2, 3, 4, 5]

In [74]: a.pop(10)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-74-ef2b54b3c9f6> in <module>()
----> 1 a.pop(10)

IndexError: pop index out of range

In [75]: 

```

* list.remove(value)
```
作用：从列表中删除第一个找到的value。如果list中没有value，则引发ValueError的错误。

返回值：无返回值
```

```
示例：
In [80]: a
Out[80]: [0, 1, 2, 3, 4]

In [81]: a.remove(0)

In [82]: a
Out[82]: [1, 2, 3, 4]

In [83]: a.remove(5)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-83-af76ca25878a> in <module>()
----> 1 a.remove(5)

ValueError: list.remove(x): x not in list

In [84]: 


```


* list.sort(cmp=None, key=None, reverse=False)
```
作用：在原列表的基础上，对列表进行排序。默认升序排列。reverse默认为False，如果为True，则表示反向排序
返回值：无返回值
```

```

In [103]: a
Out[103]: [0, 1, 2, 3, 4]

In [104]: a.sort()

In [105]: a
Out[105]: [0, 1, 2, 3, 4]

In [106]: a.sort(reverse=True)

In [107]: a
Out[107]: [4, 3, 2, 1, 0]

In [108]: 

```

* list.reverse()
```
作用：对列表进行反向排序。
返回值：无返回值
```

```
示例：

In [109]: a
Out[109]: [4, 3, 2, 1, 0]

In [110]: a.reverse()

In [111]: a
Out[111]: [0, 1, 2, 3, 4]

In [112]: a.reverse()

In [113]: a
Out[113]: [4, 3, 2, 1, 0]

In [114]: 
```

