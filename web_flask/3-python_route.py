#!/usr/bin/python3
'''
Script that starts a Flask web application
'''


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
    Class hello, first test class
    '''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Class hbnb, second test class
    '''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''
    Class c_route, thrird test class
    '''
    return ("C " + str(text.replace("_", " ")))


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    ''''''
    return ("Python " + str(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
