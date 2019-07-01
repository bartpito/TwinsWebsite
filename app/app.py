#!/usr/bin/env python3

from flask import Flask
app = Flask("TwinsPage")

@app.route('/')
def hello_world():
  return "hello, world"



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
