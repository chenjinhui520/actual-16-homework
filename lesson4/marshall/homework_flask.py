from flask import Flask,render_template,request,redirect
import json
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/userlist',methods=['GET','POST'])
def userlist():
    with open('store.db') as f:
        users=json.loads(f.read())
    return render_template("user_list.html",users=users)
@app.route('/adduser')
def adduser():
    return render_template("add_user.html")

@app.route('/login',methods=['POST'])

def login():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    with open('store.db') as f:
        users=json.loads(f.read())
        if user in users and passwd == users[user]:
            return "succ"
        else:
            return redirect('/')
@app.route('/confirmadd',methods=['POST'])
def confirmadd():
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    with open('store.db','r') as f:
        users = json.loads(f.read())
        users[user] = passwd
        users = json.dumps(users)
    with open('store.db', 'w') as f:
        f.write(users)
    return redirect('userlist')




if __name__=='__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)