#!/usr/bin/env python3

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/<name>')
def index(name='pito'):
  return render_template('home.html', name=name) 


@app.route('/About')
def hello():
  return render_template('about.html') 






if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')
