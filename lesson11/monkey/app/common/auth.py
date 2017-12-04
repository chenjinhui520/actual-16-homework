# --*--- coding: utf-8 ---*---

from flask import session
from flask import redirect
from functools import wraps
from crypt import encryption

from users import get_passwd_from_username

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get('sign', None):
            return redirect('/login')
        return func(*args, **kwargs)

    return wrapper


def authentication(username, password):

    '''
    1. 对参数password md5哈希 md5passwd
    2. 从数据库根据username来查询密码 dbpasswd
    3. 如果密码md5passwd 和 dbpasswd一致 表明认证成功 否则认证失败
    '''
    md5passwd = encryption(password)

    # (u'534486cf34e31bce45b6952ce8db237f',)
    dbpasswd = get_passwd_from_username(username)

    if not dbpasswd:
        return 'Username:%s not found.' % username, False

    if md5passwd != dbpasswd[0]:
        return 'Username:%s bad password' % username, False

    return None, True

