#!/usr/bin/env python3
import sys
sys.path.append('projects/SentimentAnalysis/')
sys.path.append('projects/SentimentAnalysis2/')
sys.path.append('projects/chatbot/')
import os
import pandas as pd
import tensorflow as tf
from newsparser import NewsParser
from network import Network
from cleaner import Cleaner
from TwitterSentiment.evaluate import predict_class
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from flask_nav import Nav
from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, send
from flask import request
import warnings
import h5py
warnings.filterwarnings('ignore')


f = h5py.File('/home/pszmelcz/Desktop/TwinsWebsite/app/projects/SentimentAnalysis2/bi_model_weights_1.h5', 'r')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.logging.set_verbosity(tf.logging.ERROR)


app = Flask(__name__)
app.config['SECRET_KEY']
socketio = SocketIO(app)
nav = Nav(app)


maxlen = 100
max_words = 20000
emb_size = 50

network = Network(
    max_words,
    maxlen,
    emb_size,
    None,
    False,
    'data/my_model_3.h5')
global graph
graph = tf.get_default_graph()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('landingPage.html')

@app.route('/About/<name>')
def about(name=None):
    if name == 'pito':
        return render_template('pito.html')
    elif name == 'bart':
        return render_template('bart1.html')


@app.route('/ProjectsPage')
def projectsPage():
    return render_template('projectsPage.html')


@app.route('/Sentiment')
def sentiment():
    return render_template('SentimentMainPage.html')


@app.route('/Predict', methods=['POST'])
def predict():
    network.connect_to_db('./data/news.db')
    if request.method == 'POST':
        topic = request.form['topic']
        print(topic)
        with graph.as_default():
            prediction = network.predict_news(
                topic=topic, page_size=1, database=False)
            print(network.parser.titles[0])
            print(prediction)

    return render_template(
        'SentimentResults.html',
        prediction=prediction,
        text=network.parser.titles[0])


@app.route('/Prediction')
def prediction():
    tweets, predicted_y, label = predict_class([], [-1], "datastories.twitter", 300)



@app.route('/Book')
def book():
    return render_template('bookPage.html')


@app.route('/NLP')
def NLP():
    return render_template('NLP.html')


@app.route('/Learning')
def learningPage():
    return render_template('learningPage.html')


@app.route('/chatbot')
def chatbot():
    #os.system('make action')
    return render_template('chatbot.html')


@app.route('/Emotion')
def emotion():
    return render_template('emotion.html')

@app.route('/fullMode')
def fullMode():
    return render_template('fullMode.html')

@app.route('/winMode')
def winMode():
    return render_template('winMode.html')

@socketio.on('message')
def handleMessage(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True, port=5003)
    #app.run(debug=True, host='localhost', port=5002)

