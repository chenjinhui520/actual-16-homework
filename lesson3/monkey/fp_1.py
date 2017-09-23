#coding: utf-8


# 1. 打开文件
fd = open('/etc/passwd')

# 2. 读取文件内容
data = fd.read()

print type(data)

# 3. 处理数据
counter = 0 
for line in data.split('\n'):
    if line.endswith('/bin/bash'):
        counter += 1
print '/bin/bash counter: ', counter


# 4. 关闭文件
fd.close()
