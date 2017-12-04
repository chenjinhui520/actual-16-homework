#coding:utf-8


from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request 
from flask import jsonify


from app.common.auth import login_required
from app.common.users import get_users
from app.common.users import register


mod = Blueprint('users', __name__, url_prefix='/users')

'''用户
'''
@mod.route('/', methods=['GET', 'POST'])
@login_required
def users():

    if request.method == 'GET':
        users = get_users()
        return render_template('users.html', users=users)

    elif request.method == 'POST':

        data = request.form.to_dict()
        print data
        effect_record = register(data)
        print effect_record
        if effect_record == 1:
            ret = {'code' : 0, 'message' : 'register sucess.', 'data' : None}
        else:
            ret = {'code' : -1, 'message' : "register faield.", 'data' : None}
        #return json.dumps(ret)
        return jsonify(ret)


#'''用户编辑
#'''
#@mod.route('/edit', methods=['GET', 'POST'])
#def usersEdit():
#    if request.method == 'POST':
#        modifyInfo = request.form.to_dict()
#        # 修改数据库
#        # userEdit(modifyInfo)
#        # "UPDATE users SET password = '%s' wehre username = '%s'" % (modifyInfo['username'], modifyInfo['password'])
#        return redirect('/users')
#    else:
#        username = request.args['username']
#        print username
#        return render_template('users_edit.html', username=username)
#
#
#'''用户删除
#'''
#@mod.route('/<int:uid>', methods=['GET'])
#@login_required
#def usersDel(uid):
#    response = userDel(uid)
#    return redirect('/users')
#
