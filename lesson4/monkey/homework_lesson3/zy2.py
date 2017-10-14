#coding: utf-8

status_code_map = {}

# 打开文件
fd = open('logs/nginx.log', 'r')

data = fd.read()

for line in data.split('\n'):
    if not line:
        continue
    token = line.split()
    status_code = token[0]
    if status_code in status_code_map:
        status_code_map[status_code] += 1
    else:
        status_code_map[status_code] = 1

# 输出
print status_code_map


# 关闭问津啊
fd.close()
