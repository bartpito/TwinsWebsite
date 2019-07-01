#!/usr/bin/env python3

from flask import Flask
app = Flask("TwinsPage")

@app.route('/')
def mainPage():
  return "hello, world"



if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1', port=5000)
