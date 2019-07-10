#!/usr/bin/env python3

from flask import Flask, render_template, url_for, redirect
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator 

app = Flask(__name__)
nav = Nav(app)



@nav.navigation("navbar")
def create_navbar():
  home_view = View("Home", 'index')
  pito_view = View("About Pito", 'about', name="pito")
  bart_view = View("About Bart", 'about', name="bart")
  return Navbar("MySite", home_view, pito_view, bart_view)


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
