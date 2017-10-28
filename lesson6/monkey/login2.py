
from flask import Flask, request
import json


'''
    https://github.com/login
    https://github.com/
'''

@app.route('/login', methods=['GET'])
def login():
   username = request.form['username'] 
   password = request.form['password'] 

   if not check_username_exists(username):
        return '/login'

   if not authentication(username, password)):
        return '/login'

   return '/'




















def check_username_exists(username):
   # 1. check_username_exists
   with open(filename, 'r') ad fd:
	data = fd.read()
	obj = json.loads(data)

   #obj -> [{'username' : 'monkey', 'password' : '123'}, {'username' : 'monkey1', 'password' : '123456'}]
   users = [ x['username'] for x in obj if x ]
   if username not in users:
	# return '/login'
        return False
   return True


def authentication(username, password):
   # 2. authentication(username, password)
   for x in obj:
       if x['username'] == username and x['password'] == password:
           return True 
   return False 









def check_username_exists(username):
   # 1. check_username_exists
   with open(filename, 'r') ad fd:
	data = fd.read()
	obj = json.loads(data)

   return "filename not found.", False

   #obj -> [{'username' : 'monkey', 'password' : '123'}, {'username' : 'monkey1', 'password' : '123456'}]
   users = [ x['username'] for x in obj if x ]
   if username not in users:
	# return '/login'
        return "user not exists.", False
   return True


def authentication(username, password):
   # 2. authentication(username, password)
   for x in obj:
       if x['username'] == username and x['password'] == password:
           return True 
   return False 
