from flask import Flask
from flask import render_template 



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('login.html')
    #return render_template('index.html')

@app.route('/user/<username>')
def username(username):
    return render_template('index.html', name=username)

@app.route('/dashboard')
def dashboard():
    return render_template('index2.html')

@app.route('/dic')
def dic():
    result = {'name' : 'monkey', 'tel' : '132'}
    return render_template('index.html', data=result)

@app.route('/list')
def list():
    result = range(1, 10) 
    return render_template('index.html', listdata=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
