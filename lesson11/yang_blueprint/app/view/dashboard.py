#!/usr/bin/env python
#coding:utf-8
import logging
from flask import Blueprint
from flask import render_template

from app.common.auth import login_required

mod = Blueprint('dashboard',__name__,url_prefix='/')

@mod.route('/')
@login_required
def index():
    logging.debug('index')
    return render_template('index.html')


