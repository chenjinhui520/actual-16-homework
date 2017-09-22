#!/usr/bin/env python
#coding:utf-8

    (1)
    (2)
    (3)
#1
'''
s.count()
    Docstring:
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are interpreted
    as in slice notation.
    Type:      builtin_function_or_method
    (1)返回字符串中某些字符出现的次数值，参数为(某字符),可指定'起始-结束'范围,若该值不存在，返回0。
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.count('5')
    s.count('u')
'''
#2
'''
s.startswith()
    Docstring:
    S.startswith(prefix[, start[, end]]) -> bool

    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.
    Type:      builtin_function_or_method
    (1)查找字符串中是以哪些字符开头，并返回一个bool值。参数可同时指定'起始-结束'范围。
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.startswith(s)
    True
    s.startswith(' sQ')
    True
'''
#3
'''
s.endswith()
    Docstring:
    S.endswith(suffix[, start[, end]]) -> bool

    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.
    Type:      builtin_function_or_method
    同startswith(),查看字符串结尾！
'''
#4
'''
s.find()
    Docstring:
    S.find(sub [,start [,end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
    Type:      builtin_function_or_method
    (1)在字符串中查找某字符第一次出现时的索引值，并可指定'起始-结束'范围，若该值不存在，则返回-1。
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.find('5')
    -1
    s.find('s')
    s.find('128')
    8
'''
#5
'''
s.join()
    Docstring:
    S.join(iterable) -> string

    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.
    Type:      builtin_function_or_method
    (1)将S字符串拼接到可迭代对象的元素之间并返回
    (2)有返回值
    (3)示例：
    s2 = s.join('666')
    s2
    '6 sQWe wo128ruru  6 sQWe wo128ruru  6'
    s2 = '+'.join('666')
    s2
    '6+6+6'
'''
#6
'''
s.lower()
    Docstring:
    S.lower() -> string

    Return a copy of the string S converted to lowercase.
    Type:      builtin_function_or_method
    (1)返回一个将S子串中所有字符变成小写的新字符串
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.lower()
'''
#7
'''
s.upper()
    Docstring:
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
    Type:      builtin_function_or_method
    (1)返回一个将S子串中所有字符变成大写的新字符串
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.upper()
'''
#8
'''
s.strip()
    Docstring:
    S.strip([chars]) -> string or unicode

    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping
    Type:      builtin_function_or_method
    (1)返回一个将原S子串左右两边的空白去掉的新字符串，也可以去符号
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.strip()
    s2 = '-sdfsd-'
    s2.strip('-')
'''
#9
'''
s.lstrip()
    Docstring:
    S.lstrip([chars]) -> string or unicode

    Return a copy of the string S with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping
    Type:      builtin_function_or_method
    (1)同.strip()，去掉字符串左边空白，并返回新字符串
    (2)有返回值
    (3)示例：
    s2 = '-sdofjow-'
    s2.lstrip('-')
    'sdofjow-'
    s = ' sQWe wo128ruru  '
    s.lstrip()
    'sQWe wo128ruru  '
'''
#10
'''
s.rstrip()
    Docstring:
    S.rstrip([chars]) -> string or unicode

    Return a copy of the string S with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping
    Type:      builtin_function_or_method
    (1)同.strip()，去掉字符串右边空白，并返回新字符串
    (2)有返回值
    (3)示例：
    s2.rstrip('-')
    '-sdofjow'
'''
#11
'''
s.replace()
    Docstring:
    S.replace(old, new[, count]) -> string

    Return a copy of string S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.
    Type:      builtin_function_or_method
    (1)将原子符串中某些字符全部替换成新的字符并返回替换后的新字符串，参数为'旧字符,新字符'，参数内也可以指定替换几次
    (2)有返回值
    (3)示例：
    s = ' sQWe wo128ruru  '
    s.replace('ru','aa')
    ' sQWe wo128aaaa  '
    s.replace('r','y',1)
    ' sQWe wo128yuru  '
'''

