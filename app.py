#!/usr/bin/env python3

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/About/<name>')
def hello(name=None):
  return render_template('about.html', name=name)






if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')
