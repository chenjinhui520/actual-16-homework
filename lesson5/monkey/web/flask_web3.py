#coding: utf-8

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():
    #print dir(request)
    print 'method:%s ' % request.method
    print "enter form request."
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        s = str( int(num1) + int(num2) )
        print 'return %s + %s = %s' % (num1, num2, s)
        return s
    else:
        return '''<form action='/form' method='POST'> 
          	第一个数 : <input type='text' name='num1' value='109'><br/>
          	第二个数 : <input type='text' name='num2'><br/>
            	<input type=submit value='求和'>
                  </form>'''
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
