# 文件对象操作

* open(name[, mode[, buffering]])
```
作用：使用指定的模式打开文件。
返回值：返回一个文件对象

模式：
r：只读模式。默认模式。需要文件事先存在
w：只写模式。文件不存在会创建，文件存在，则清空内容
a：只追加模式。文件不存在则创建，存在，则追加到末尾。

r+：读写模式。需要文件事先存在
w+：读写模式。文件不存在，则创建，存在则清空
a+：追加模式。文件不存在，则创建，存在，则追加到末尾。
```


* f.read([size])
```
作用：读取指定字节的数据，如果size没有指定，则读取所有内容
返回值：字符串
```

```
示例：
In [482]: data = fd.read()

In [483]: print data
127.0.0.1	localhost
127.0.1.1	hezhang

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters


In [484]: 

```

* f.name
```
作用：查看打开的文件名
返回值：字符串
```

```
示例：
In [489]: fd.name
Out[489]: '/tmp/hosts'

In [490]: 
```

* f.mode
```
作用：查看文件的打开模式
返回值：字符串
```

```
示例：
In [491]: fd.mode
Out[491]: 'r'

In [492]: 
```

* f.closed
```
作用：判断文件是否已经关闭
返回值：布尔值
```

```
示例：
In [494]: fd.closed
Out[494]: False

In [495]: 
```


* f.tell()
```
作用：返回当前指针所在的位置
返回值：整型
```

```
示例：
In [499]: fd.tell()
Out[499]: 222

In [500]: 

```

* f.seek(offset[, whence])
```
作用：将指针移动到指定的位置。默认的whence是0，表示offset从文件的开头，1表示相对于当前位置，2表示offset从文件的末尾。
返回值：None
```

```
示例：
In [524]: f.tell()
Out[524]: 222

In [525]: f.seek(0)

In [526]: f.tell()
Out[526]: 0

In [527]: 
```

* f.readline([size])
```
作用：一次读取文件的一行数据。
返回值：字符串
```

```
示例：
In [535]: print f.readline()
127.0.0.1	localhost


In [536]: print f.readline()
127.0.1.1	hezhang


In [537]:
```

* f.readlines([size])
```
作用：读取文件的所有行，以列表的形式返回
返回值：每一行组成的列表
```

```
示例：
In [548]: data = f.readlines()

In [549]: print type(data)
<type 'list'>

In [550]: print data
['127.0.0.1\tlocalhost\n', '127.0.1.1\thezhang\n', '\n', '# The following lines are desirable for IPv6 capable hosts\n', '::1     ip6-localhost ip6-loopback\n', 'fe00::0 ip6-localnet\n', 'ff00::0 ip6-mcastprefix\n', 'ff02::1 ip6-allnodes\n', 'ff02::2 ip6-allrouters\n']

In [551]: 

```


* f.flush()
```
作用：将缓存中的内容写入到文件中。
返回值：None
```

* f.write(str)
```
作用：将字符串str写入到文件。
返回值：None
```

```
示例：
In [564]: f = open('/tmp/a', 'w')

In [565]: f.write('hello 01\n')

In [566]: f.write('hello 02\n')

In [567]: f.write('hello 03\n')

In [568]: f.flush()

In [569]: f.close()

In [570]:   

In [570]: f = open('/tmp/a')

In [571]: for i in f.readlines():
     ...:     print i,
     ...:     
hello 01
hello 02
hello 03

In [572]: 

```


* f.writelines(sequence_of_strings)
```
作用：将列表中的内容写入到文件
返回值：None
```

```
示例：
In [576]: f1 = open('/tmp/hosts')

In [577]: data1 = f1.readlines()

In [578]: f1.close()

In [579]: f2 = open('/tmp/b', 'w')

In [580]: f2.writelines(data1)

In [581]: f2.close()

In [582]: f2 = open('/tmp/b')

In [583]: for line in f2:
     ...:     print line,
     ...:     
127.0.0.1	localhost
127.0.1.1	hezhang

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

In [584]: 

```
