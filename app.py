#!/usr/bin/env python3

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
  return "Hello, World!"



if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')
