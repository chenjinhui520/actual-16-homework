from flask import Flask
from flask import render_template 



app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('regsiter.html')

@app.route('/userlist')
def userlist():
    users = []
    return render_template('userlist.html', users=users)

@app.route('/search')
def userlist():
    user = username
    return render_template('search.html', user=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
