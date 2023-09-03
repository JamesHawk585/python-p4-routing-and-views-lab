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

@app.route('/count/<int:parameter>')
def count_param(parameter):
    # Generator expression 
    # it generates a sequence of numbers starting from 0 and ending at parameter - 1.
    return '\n'.join(str(i) for i in range(parameter)) + '\n'
    
@app.route('/math/<int:num1>/+/<int:num2>')
def math_route_add(num1, num2):
    # Flask view functions can only return a string, tuple, or a Flask Response Object. 
    return str(num1 + num2)

@app.route('/math/<int:num1>/-/<int:num2>')
def math_route_subtract(num1, num2):
    return str(num1 - num2)

@app.route('/math/<int:num1>/div/<int:num2>')
def math_route_divide(num1, num2):
    return str(num1 / num2)

@app.route('/math/<int:num1>/*/<int:num2>')
def math_route_multiply(num1, num2):
    return str(num1 * num2)

@app.route('/math/<int:num1>/%/<int:num2>')
def math_route_modulo(num1, num2):
    return str(num1 % num2)



# http://127.0.0.1:5555/math/5/+/5
