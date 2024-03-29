
from flask import (
  render_template,
  Blueprint,
  current_app)

base = Blueprint('base', __name__)

@base.route('/')
@base.route('/index')
def index():
  return render_template('index.html')


@base.route('/about/<name>')
def about(name):
  return render_template('index.html', name=name)