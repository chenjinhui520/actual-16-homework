# 字典方法概述
* dict.clear()
```
作用：清除字典dict中的所有条目
返回值：无返回值
```

```
示例：
In [6]: d
Out[6]: {'name': 'felix'}

In [7]: d.clear()

In [8]: d
Out[8]: {}

In [9]: 
```


* dict.copy()
```
作用：返回字典dict的副本。
返回值：返回字典dict的一个副本，是一个新的副本
``` 

```
示例：
In [19]: d = {'name': 'felix'}

In [20]: d.copy()
Out[20]: {'name': 'felix'}

In [21]: e = d.copy()

In [22]: e
Out[22]: {'name': 'felix'}

In [23]: 
```

* dict.fromkeys(S[,v])
```
作用：使用可迭代对象S的值作为key，使用v作为key的默认值，创建一个新的字典。如果没有指定v，则默认v的值是None。
返回值：一个新的字典
```

```
示例：
In [28]: a = ['a', 'b']

In [29]: dict.fromkeys(a)
Out[29]: {'a': None, 'b': None}

In [30]: dict.fromkeys(a)
Out[30]: {'a': None, 'b': None}

In [31]: a = 'abc'

In [32]: dict.fromkeys(a)
Out[32]: {'a': None, 'b': None, 'c': None}

In [33]: dict.fromkeys(a)
Out[33]: {'a': None, 'b': None, 'c': None}

In [34]: a = 123

In [35]: dict.fromkeys(a)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-636122c8d1ac> in <module>()
----> 1 dict.fromkeys(a)

TypeError: 'int' object is not iterable

In [36]: 

```

* dict.get(k[,d])
```
作用：如果k在字典中，则返回dict[k]，如果k不在字典中，则返回d。默认的d是None
返回值：dict[k]或None
```

```
示例：
In [37]: d
Out[37]: {'name': 'felix'}

In [38]: d.get('name')
Out[38]: 'felix'

In [39]: d.get('age')

In [40]: d.get('age', -1)
Out[40]: -1

In [41]: 

```

* dict.has_key(k)
```
作用：判断键k是否在字典dict中。如果在，则返回True，否则返回False。
返回值：布尔值。
```

```
示例：
In [43]: d.has_key('name')
Out[43]: True

In [44]: d.has_key('age')
Out[44]: False

In [45]: 

```

* dict.update([E, ]**F)
```
作用：从字典或可迭代对象E和F更新字典dict的内容。
返回值：None
```

```
示例：
In [333]: d = {}

In [334]: d1 = {'name': 'felix', 'age': 28}

In [335]: d2 = {'address': 'beijing'}

In [336]: d.update(d1)

In [337]: d
Out[337]: {'age': 28, 'name': 'felix'}

In [338]: d.update(d2)

In [339]: d
Out[399]: {'address': 'beijing', 'age': 28, 'name': 'felix'}

In [340]: 
```

* dict.items()
```
作用：返回字典dict的(key,value)对组成的列表
返回值：列表
```

```
示例：
In [67]: d.items()
Out[67]: [('name', 'felix')]

In [68]: info
Out[68]: {'age': 28, 'name': 'felix.zhang', 'sex': 'male'}

In [69]: info.items()
Out[69]: [('age', 28), ('name', 'felix.zhang'), ('sex', 'male')]

In [70]: 
```

* dict.keys()
```
作用：返回字典dict的所有key组成的列表
返回值：key组成的列表
``` 

```
示例：
In [77]: info.keys()
Out[77]: ['age', 'name', 'sex']

In [78]: 
```

* dict.values()
```
作用：返回字典dict的所有value组成的列表
返回值：value组成的列表
```

```
示例：
In [79]: info
Out[79]: {'age': 28, 'name': 'felix.zhang', 'sex': 'male'}

In [80]: info.values()
Out[80]: [28, 'felix.zhang', 'male']

In [81]: 

```

* dict.iterkeys()
```
作用：返回一个迭代器，该迭代器是字典dict的所有key
返回值：一个迭代器
```

```
示例：
In [89]: info
Out[89]: {'age': 28, 'name': 'felix.zhang', 'sex': 'male'}

In [90]: keyIter = info.iterkeys()

In [91]: type(keyIter)
Out[91]: dictionary-keyiterator

In [92]: for k in keyIter:
    ...:     print k
    ...: 
age
name
sex

In [93]: 

```

* dict.itervalues()
```
作用：返回一个迭代器，该迭代器是字典dict的所有vlaues
返回值：一个迭代器
```

```
示例：
In [107]: info
Out[107]: {'age': 28, 'name': 'felix.zhang', 'sex': 'male'}

In [108]: valueIter = info.itervalues()

In [109]: type(valueIter)
Out[109]: dictionary-valueiterator

In [110]: for v in valueIter:
     ...:     print v
     ...:     
28
felix.zhang
male

In [111]: 

```

* dict.iteritems()
```
作用：返回一个迭代器，该迭代器是字典的key，value对。
返回值：一个迭代器
```

```
示例：
In [140]: info
Out[140]: {'age': 28, 'name': 'felix.zhang', 'sex': 'male'}

In [141]: itemsIter = info.iteritems()

In [142]: type(itemsIter)
Out[142]: dictionary-itemiterator

In [143]: for k, v in itemsIter:
     ...:     print k, v
     ...:     
age 28
name felix.zhang
sex male

In [144]: 

```

* dict.pop(k[,d]) 
```
作用：从字典dict中删除指定的key，如果key在dict中，则返回该key所对应的value，如果指定了d，则返回d，否则返回引发KeyError错误。
返回值：key在字典dict中所对应的value。如果指定了d，在key不存在时，返回d，否则引发KeyError的错误
```

```
示例：
In [174]: info
Out[174]: {'age': 28, 'name': 'felix.zhang', 'sex': 'male'}

In [175]: info.pop('age')
Out[175]: 28

In [176]: info.pop('age')
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-176-a54fc012db60> in <module>()
----> 1 info.pop('age')

KeyError: 'age'

In [177]: info.pop('age', 'NO')
Out[177]: 'NO'

In [178]: 

```


* dict.popitem()
```
作用：从字典dict中移除(key,value)对，如果字典dict是空的，则引发KeyError错误
返回值：删除的(key,value)对，元组
```

```
示例：
In [180]: info.popitem()
Out[180]: ('name', 'felix.zhang')

In [181]:
```

* dict.setdefault(k[,d])
```
作用：如果键k在字典dict中，则返回其值，如过key不在dict中，则添加。
返回值：键k在字典dict中所对应的值。或者是所设置的值。
```


```
示例：
In [183]: info
Out[183]: {'sex': 'male'}

In [184]: info.setdefault('sex')
Out[184]: 'male'

In [185]: info.setdefault('age', 28)
Out[185]: 28

In [186]: info
Out[186]: {'age': 28, 'sex': 'male'}

In [187]: 
```


