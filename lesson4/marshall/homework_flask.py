from flask import Flask,render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('store.db') as f:
        users=json.loads(f.read())
        return render_template("index.html",users=users)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)


