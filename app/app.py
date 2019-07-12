#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request
import pandas as pd
import sys
sys.path.append('projects/SentimentAnalysis/')
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from cleaner import Cleaner
from network import Network
from newsparser import NewsParser
import os
import tensorflow as tf
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
tf.logging.set_verbosity(tf.logging.ERROR)


app = Flask(__name__)
nav = Nav(app)

maxlen = 100
max_words = 20000
emb_size = 50

network = Network(max_words, maxlen, emb_size, None, False, 'projects/SentimentAnalysis/data/my_model_3.h5')

global graph
graph = tf.get_default_graph()

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


@app.route('/Projects')
def projects():
    return render_template('projects.html')


@app.route('/ProjectsPage')
def projectsPage():
    return render_template('projectsPage.html')

@app.route('/Sentiment')
def home():
    return render_template('SentimentMainPage.html')


@app.route('/predict', methods=['POST'])



def predict():
    network.connect_to_db('./data/news.db')
    if request.method == 'POST':
        topic = request.form['topic']
        print(topic)
        with graph.as_default():
            prediction = network.predict_news(topic=topic, page_size=1, database=False)
            print(network.parser.titles[0])
            print(prediction)
   
    return render_template('SentimentResult.html', prediction=prediction, text=network.parser.titles[0])

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
