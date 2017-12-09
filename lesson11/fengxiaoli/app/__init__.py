#!/usr/bin/env python
# coding: utf-8

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

from app.view import dashboard
from app.view import users
from app.view import login

app.register_blueprint(dashboard.mod)
app.register_blueprint(users.mod)
app.register_blueprint(login.mod)


