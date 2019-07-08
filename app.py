#!/usr/bin/env python3

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('mainpage.html')

@app.route('/About/<name>')
def about(name=None):
  if name == 'pito':
    return render_template('pito.html') 
  elif name == 'bart':
    return render_template('bart.html')



if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')
