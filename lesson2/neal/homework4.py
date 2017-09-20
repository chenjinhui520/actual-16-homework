#coding: utf-8
'''
s.strip
S.strip([chars]) -> string or unicode

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping
1.删除字符串前面和后面的空白符。删除两边在删除()内的指定的字符.
2.有返回值
3.示例
'''
s = '\n \n 123123abc1233211\n\n  \n'
print s.strip()

'''
s.lstrip
S.lstrip([chars]) -> string or unicode

Return a copy of the string S with leading whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping
1.删除字符串前面【左边】的空白字符串。删除前面【左边】()内的指定的字符.
2.有返回值
3.示例
'''
s1 = '\n \n 123123abc1233211\n  \n'
print s.lstrip()

'''
s.rstrip
S.rstrip([chars]) -> string or unicode

Return a copy of the string S with trailing whitespace removed.
If chars is given and not None, remove characters in chars instead.
If chars is unicode, S will be converted to unicode before stripping
1.删除字符串后面【右边】的空白字符串。删除后面【右边】()内指定的字符。
2.有返回值
3.示例
'''
s2 = '\n \n 123123abc1233211\n  \n'
print s.rstrip()

'''
s.find
S.find(sub [,start [,end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.
1.查找字符串中是否含有字符串，可以指定范围。默认从头开始查，查不到返回-1,查到后返回字符串第一位索引值
2.有返回值
3.示例
'''
s3 = '\n \n 123123abc1233211\n  \n'
print s3.find('abc')

'''
s.join
S.join(iterable) -> string

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
1.将序列中的元素以指定的字符连接。
2.有返回值
3.示例
'''
s4 = '!@#'
print s4.join('51reboot')

'''
s.lower
S.lower() -> string

Return a copy of the string S converted to lowercase.
1.转换字符串中所有大写字符为小写。
2.有返回值
3.示例
'''
s5 = 'DAFKLDSJLAF;lasjfiojew'
print s5.lower()

'''
s.upper
S.upper() -> string

Return a copy of the string S converted to uppercase.
1.转换字符串中所有的小写字符为大写。
2.有返回值
3.示例
'''
s6 = 'kjflksadjf;KFJDSAKLF'
print s6.upper()

'''
s.replace
S.replace(old, new[, count]) -> string

Return a copy of string S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
1.旧的字符串替换成新的字符串，第三参数是替换次数。
2.有返回值
3.示例
'''
s7 = 'abcacbaaaamslabcabcaaaacc'
print s7.replace('abc','neal',2)

'''
s.startswith
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.
1.检查字符串起始部分是否是以指定字符开头，是返回True，不是返回False。beg和end指定字符串的范围。
2.有返回值
3.示例
'''
s8 = 'neallove51reboot'
print s8.startswith('neal',0,8)

'''
s.endswith
S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.
1.检查字符串结尾部分是否是以指定字符结尾，是返回True，不是返回False。可指定字符串的范围。
2.有返回值
3.示例
'''
s8 = 'neallove51reboot'
print s8.endswith('51reboot',3,16)

'''
s.count
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are interpreted
as in slice notation.
1.统计字符串中字符出现的次数。可指定范围，返回结果次数为整型。
2.有返回值
3.示例
'''
s9 = 'neallove51reboot'
print s9.count('l', 0 ,5)






