#coding: utf-8

from flask import Flask
from flask import request 
from flask import render_template 


app = Flask(__name__)



'''用户登录
'''
@app.route('/login')
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')

'''首页
'''
@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
