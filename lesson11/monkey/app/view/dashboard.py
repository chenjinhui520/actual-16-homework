
from flask import Blueprint
from flask import render_template 


mod = Blueprint('dashboard', __name__, url_prefix='/')


@mod.route('/')
def dashboard():
    return render_template('index.html')

