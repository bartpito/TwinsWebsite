#!/usr/bin/env python3

from flask import Flask, render_template, url_for


app = Flask("TwinsPage")

@app.route('/')
def index():
  return render_template("index.html")



@app.route('/Pito')
def hello_pito():
  return render_template('hello.html') 


if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1', port=5000)
