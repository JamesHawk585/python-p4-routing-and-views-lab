#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_hello_param(parameter):
    return f'<h1>Hello {parameter}</h1>'

@app.route('/print/hello')
def print_text_in_console():
    print('hello')
    return 'hello' 

@app.route('/count/<parameter>')
def count_param(parameter):
    return parameter

