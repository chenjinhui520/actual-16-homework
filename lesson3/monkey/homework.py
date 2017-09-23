#coding: utf-8


counter = 0
filename = 'store.db'
personinfos = [] 

while True:
    action = raw_input('action :')

    if action == 'register':

        print 'Create your personal account'
        username = raw_input('Username :')
        email = raw_input('Email Address :')
        password = raw_input('Password:')

        person = {'username' : 'monkey' , 'email' : 'monkey@reboot.com', 'password' : '123456'}

        '''
        personinfos.appedd(person)
        '''

        print '---------------'

    elif action == 'login':

        username = raw_input('Username :')
        password = raw_input('Password:')

        '''
        循环列表
        for x in personinfos:
             if x['username'] == username and x['password'] == password:
                 'login sucess'
        '''
        if username == '' and password == '':
            print 'welcome to login sucess.'
        else:
            print 'bad username or password'

    elif action == 'quit':
        break
    else:
        print "action is required, please choice ['resiger', 'login', 'quit']."
