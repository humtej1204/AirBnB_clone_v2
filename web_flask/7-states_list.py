#!/usr/bin/python3
'''
Script that starts a Flask web application
'''


from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list():
    '''
    Class hbnb, create a dinamic page which display the list of objects
    '''
    return render_template('7-states_list.html',
                           states_list=storage.all('State').values())


@app.teardown_appcontext
def close_db(self):
    '''
    Closes the database again at the end of the request
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
