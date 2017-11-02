import json
def ReadFile():
    try:
        with open('store.db', 'r') as fd:
            users = json.loads(fd.read())
            return users
    except Exception as e:
        users = []
        return users

def WriteFile(registerInfo):
    try:
        with open('store.db', 'r') as fd:
            users = json.loads(fd.read())
            #print users
    except Exception as e:
        users = []

    users.append(registerInfo)
    with open('store.db', 'w') as fd:
        fd.write(json.dumps(users))

def check_user_exists(username):
    try:
        with open('store.db','r') as fd:
            users = json.loads(fd.read())
    except Exception as e:
        users = []
    usernames = [ x['username'] for x in users if x ]
    if username in usernames:
        return True
    else:
        return False

def check_email(email):
    if '@' in email:
        return True
    else:
        return False

def login(*args):
    data = ReadFile()
    map_user_pass_dic = { x['username'] : x['password'] for x in data if x }
    print map_user_pass_dic
    if map_user_pass_dic.get(args[0],None) == args[1]:
        return True
    else:
        return False
