#!/usr/bin/env python
#coding:utf-8
import logging
from flask import Blueprint
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect

from app.common.auth import login_required

from app.common.assets import assets_get
from app.common.assets import assets_add
from app.common.assets import assets_edit
from app.common.assets import assets_del

mod = Blueprint('assets',__name__,url_prefix="/assets")
#获取资产
@mod.route('/',methods=['GET','POST'])
@login_required
def assets():
    logging.debug('assets')
    if request.method == "POST":
        data = request.form.to_dict()
        response = assets_add(data)
        ret = {"status":0}
        return jsonify(ret)
    else:
        assets = assets_get()
        return render_template('assets.html',assets = assets)

#修改资产
@mod.route('/edit',methods=['GET','POST'])
@login_required
def assets_e():
    logging.debug('assets_edit')
    if request.method == 'POST':
        data = request.form.to_dict()
        print data
        print type(data)
        response = assets_edit(**data)
        return jsonify({'status':0})
    else:
        return redirect('/assets')
#删除资产
@mod.route('/del/',methods=['GET'])
@login_required
def assets_d():
    logging.debug('assets_edit')
    data = request.args.to_dict()
    uid = data['id']
    print uid
    response = assets_del(uid)
    return redirect('/assets')
