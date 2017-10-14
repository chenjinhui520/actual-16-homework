#coding: utf-8

status_code_map = {}

# 打开文件
fd = open('logs/nginx.log', 'r')

data = fd.read()

for line in data.split('\n'):
    if not line:
        continue

    token = line.split()
    remoteIp = token[0]
    url = token[6]
    key = "%s %s" % (remoteIp, url)

    if key in status_code_map:
        status_code_map[key] += 1
    else:
        status_code_map[key] = 1

# 输出
print status_code_map


# 关闭问津啊
fd.close()
