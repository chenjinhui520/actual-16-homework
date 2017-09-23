

s = '''
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
'''

'\n'
#print s
# left
# right
#print s.strip()


'''
s1 = [' linux', 'windows', 'mac', 'andorid']

ret = []
for x in s1:
    s1 = x.strip(' ')
    ret.append(s1)
print ret 
'''

'''
strip | lstrip | rstrip
''.join()
split
format
replace
    s.replace('\n', '')
count
index
find -> index
isdigit
s.center -> 居中 第二个参数 字符串填充

'''

ret = []

s1 = s.split('\n')
for x in s1:
    if x:
        ret.append(x)
print ret
