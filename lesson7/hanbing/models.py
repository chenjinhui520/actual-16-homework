#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'hanbing'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.11.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True,index=True, autoincrement=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    reg_time = db.Column(db.DateTime,default=datetime.datetime.now())
    role_id = db.Column(db.Integer, nullable=False, default='0')


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
