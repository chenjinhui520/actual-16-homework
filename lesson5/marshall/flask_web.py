# coding:utf-8
import json
from flask  import render_template,redirect,Flask,request


app = Flask(__name__)


def readfile():
    try:
        fh = open('users.db','r')
    except:
            users=[]
    else:
        users = json.loads(fh.read())
        fh.close()
    return users


def writefile(userinfo):
    users = readfile()
    users.append(userinfo)
    with open('users.db','w') as fh:
        fh.write(json.dumps(users))


def check_user_exist(userinfo):
    users = readfile()
    usersname = [ x['username'] for x in users ]
    if userinfo['username'] in usersname:
        return True
    else:
        return False

def check_email(userinfo):
    if '@' in userinfo['email']:
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        userinfo = request.form.to_dict()

        if check_user_exist(userinfo):
            return render_template('register.html',msg='user_exsit')

        if not check_email(userinfo):
            return render_template('register.html', msg='error_email')

        writefile(userinfo)
        return redirect('/userlist')
    else:
        return render_template('register.html')


@app.route('/userlist',methods=['GET'])
def userlist():
    users=readfile()
    return render_template('userlist.html',users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9002,debug=True)

