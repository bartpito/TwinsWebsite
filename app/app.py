#!/usr/bin/env python3

from flask import Flask, render_template, url_for


app = Flask("TwinsPage")

@app.route('/')
def hello_world():
  return "hello, world"



@app.route('/Pito')
def hello_pito():
  return render_template('hello.html') 


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
