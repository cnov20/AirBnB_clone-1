#!/usr/bin/python3

''' This module uses Flask to setup a Web Server Gateway Interface
    to a web application (HBNB) that enables the application to listen
    for requests to it / its web server, on a given port

    Defines routes and sends return message, indicating succesful connection

    Returns template for applicable route(s)
'''

from flask import Flask, url_for, render_template
app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C ' + text


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
