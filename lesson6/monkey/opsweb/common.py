#--*--coding: utf-8--*--

import json

filename = "/tmp/store.db"

# 登录认证
def authentication(username, password):
    if username == "admin" and password == '123465':
        return True
    return False


# 注册
def register(data):
    memdata, ok = load()
    if ok and memdata:
        memdata.append(data)
        dump(memdata)
    else:
        dump([data])
    return None, True


# 查看所有用户信息
def get_users():
    users, _ = load()
    return users


# 写入到磁盘
def dump(data):
    fd = open(filename, 'w')

    if isinstance(data, str):
        fd.write(data)
    elif isinstance(data, list):
        fd.write(json.dumps(data))

    fd.close()


# 从磁盘加载数据到内存
def load():
    try:
        fd = open(filename, 'r')
    except Exception as e:
        return [], False
    else:
        data = fd.read()
        jsondata = json.loads(data)
        return jsondata, True
    finally:
        if 'fd' in locals():
            fd.close()
