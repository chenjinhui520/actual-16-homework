

from functools import wraps
from flask import redirect
from flask import session


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get('username'):
            return redirect('/login')

        rt = func(*args, **kwargs)
        return rt

    return wrapper
