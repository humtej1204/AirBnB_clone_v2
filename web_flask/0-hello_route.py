#!/usr/bin/env python3
'''
Script that starts a Flask web application
'''


from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    '''
    Class hello, first test class
    '''
    return ('Hello HBNB!')

app.run(host="0.0.0.0", port=5000)
