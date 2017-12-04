from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request 
from flask import session

from app.common.auth import authentication
from app.common.users import get_role_from_username



mod = Blueprint('login', __name__)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        authinfo, ok = authentication(username, password)
        print authinfo, ok
        if ok:
            role = get_role_from_username(username)
            print role
            #session['sign'] = username
            session['sign'] =  { 'username' : username, 'role' : role[0]}
            return redirect("/")
        else:
            return render_template('login.html', errmsg=authinfo)
    else:
        return render_template('login.html')


@mod.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
