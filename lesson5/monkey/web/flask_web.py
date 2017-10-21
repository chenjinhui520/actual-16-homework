#coding: utf-8

from flask import Flask
from flask import request

app = Flask(__name__)

# 路由
@app.route('/')
@app.route('/index')
def index():  # 视图
    return 'index3'

@app.route('/user/username')
def user_username():
    return 'func username'

@app.route('/user/<username>')
def username(username):  # 视图
    return 'username : %s' % username

@app.route('/username/<float:user_id>')
#@app.route('/username/<int:user_id>')
def username_for_id(user_id):  # 视图
    return 'username : %s' % user_id 

@app.route('/hello')
def hello():
    return 'Hello monkey!'

@app.route('/link')
def link():
    return '''\
	<a href="http://docs.jinkan.org/docs/flask/installation.html#installation"> 
	    <h1 style="color:red"> reboot actual 16 python form </h1>
	</a>'''

@app.route('/form')
def form():
    return '''<form action='/num_sum' method='GET'> 
		第一个数 : <input type='text' name='num1' value='109'><br/>
		第二个数 : <input type='text' name='num2'><br/>
		<input type=submit value='求和'>
              </form>'''
        

@app.route('/num_sum')
def num_sum():
    #print request.args
    num1 = request.args['num1']
    num2 = request.args['num2']
    print 'num1:%s, num2:%s' % (num1, num2)
    s = 2 + 3
    return str(s)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
