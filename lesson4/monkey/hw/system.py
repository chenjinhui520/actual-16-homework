#!coding: utf-8

import sys
import json

personinfos = []


def login(*args, **kwargs):
    username = raw_input('Username: ')
    password = raw_input('Password: ')
    # check failed count; failed_count >= 3
    if check_failed_count(username):
        print 'disable username:%s login reboot system, failed count more than 3.' % username
        return

    # check username and password is ok
    auth_result, ok = authentication(username, password)
    if ok:
        print "username:%s login sucess." % username
        print '''
            Welcome to reboot system.
        '''
    else:
        add_failed_counter(username)
        print "username:%s login failed, info:%s." % (username, auth_result)

def register(*args, **kwargs):
    print '\n\tCreate your personal account\n'
    username = raw_input('Username: ')
    email = raw_input('Email Address: ')
    password = raw_input('Password: ')

    if check_user_exists(username):
        print 'username : %s already exists.' % username, False

    registerInfo = {'username' : username, 'email' : email, 'password' : password, 'failed_count' : 0}
    personinfos.append(registerInfo)
    print 'account %s is created sucess' % username, True


def add_failed_counter(username):
    global personinfos
    ret = []
    for x in personinfos:
        if x['username'] == username:
            x['failed_count'] += 1
        ret.append(x)
    personinfos = ret

def check_failed_count(username):
    map_user_failed_dic = { x['username'] : x['failed_count'] for x in personinfos if x }
    if map_user_failed_dic[username] >= 3:
        return True
    return False


def save(*args, **kwargs):
    try:
        fd = open(args[0], 'w')
    except Exception as e:
        print "save data to file failed, info:%s." % e.args
    else:
        data = json.dumps(personinfos)
        fd.write(data)
        print "save data to file sucess."
    finally:
        fd.close()


def load(*args, **kwargs):
    global personinfos
    try:
        fd = open(args[0], 'r')
    except Exception as e:
        print "load data to mem failed, info:%s" % e.args
        return
    else:
        data = fd.read()
        personinfos = json.loads(data)
        print "load data to mem sucess."
        fd.close()


def printFormat(*args, **kwargs):
    if len(args) >= 1:
        format = args[0]
    else:
        format = None
    if format == "json":
        print json.dumps(personinfos, indent=4)

    elif format == "xml":
        pass

    elif format == "table":
        '''
        username    |   email                   |   password  | failed_count
        monkey      |   monkey@51reboot.com     |   123456    |     0
        xiaoming    |   xiaoming@51reboot.com   |   123456    |     0
        '''
        print "%-10s | %-24s | %-8s | %-8s" % ("username", 'email', 'password', 'failed_count')
        for x in personinfos:
            if not x:
                continue
            print "%-10s | %-24s | %-8s | %-8s" % (x['username'], x['email'], x['password'], x['failed_count'])
        print "\n"

    else:
        print personinfos


def check_user_exists(username):
    '''
    user exists     : return True
    user not exists : return False
    '''
    usernames = [ x['username'] for x in personinfos if x ]
    if username is usernames:
        return True
    else:
        return False


def authentication(*args, **kwargs):
    '''
    如果用户名和密码验证成功 return True 否则 return False
    '''
    map_user_pass_dic = { x['username'] : x['password'] for x in personinfos if x }
    if map_user_pass_dic.get(args[0], None) == args[1]:
        return 'login sucess.', True
    else:
        return 'bad password.', False


def help(*args, **kwargs):
    docstring = '''
            [[ reboot actual-16 ]]

    login            : login reboot system.
    register         : register account to reboot's system.
    exit             : exit reboot's system.
    help             : Print help info and exit successfully.
    list             : format account info.
    exit             : exit current program.
    save             : save data to file.
    load             : load data to mem.
    '''
    print docstring


def process_action(action):
    action_slice = action.strip().split()
    if len(action_slice) == 0:
        action, args = '', ()
    elif len(action_slice) >= 1:
        action, args = action_slice[0] , action_slice[1:]
    else:
        action, args = action_slice[0] , ()
    return action, args

def exit(*args, **kwargs):
    sys.exit(0)


def main():
    actionMap = {
        'login'    : login,
        'register' : register,
        'help'     : help,
        'exit'     : exit,
        'list'     : printFormat,
        'load'     : load,
        'save'     : save,
    }

    help()
    while True:

        action = raw_input("please input your action: ")
        action, args = process_action(action)
        try:
            actionMap[action](*args)
        except Exception as e:
            pass


if __name__ == '__main__':
    main()
