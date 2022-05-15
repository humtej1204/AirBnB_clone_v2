#!/usr/bin/python3
'''
Script that starts a Flask web application
'''


from flask import Flask, render_template


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
    '''
    Class python_route, fourth test class
    '''
    return ("Python " + str(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''
    Class number_route, fifth test class
    '''
    return (str(n) + " is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    '''
    Class n_template, sixth test class
    '''
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_odd_even(n):
    '''
    Class n_odd_even, seventh test class
    '''
    if (n % 2 == 0):
        txt = "even"
    else:
        txt = "odd"

    return render_template('6-number_odd_or_even.html', num=n, t=txt)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
