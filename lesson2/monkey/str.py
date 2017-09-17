
s = '''
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
woniu:x:1003:1003::/home/woniu:/bin/bash
raopeng:x:1004:1004::/home/raopeng:/bin/bash
'''
'''
#left
s1 = s.lstrip('\n')

# right
s2 = s1.rstrip('\n')
print s2
'''

s1 = s.strip('\n')
print s1
