from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

    
@app.route('/contato') 
def contato():
  return ('contato.html')

@app.route('/sobre')
def sobre():
  return ('sobre.html')