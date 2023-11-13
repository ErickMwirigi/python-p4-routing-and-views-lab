#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
        a= int(parameter)
        num=0
        b=""
        while num < a:
            print(num)
            b=b+str(num)+"\n"
            num+=1
        return b  

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    a=int(num1)
    b=int(num2)
    c = ""
    if operation == "+":
        a+b
        c=c+str(a+b)
        return c
    elif operation == "-":
        a-b
        c=c+str(a-b)
        return c
    elif operation == "div":
        a/b
        c=c+str(a/b)
        return c
    elif operation == "*":
        a*b
        c=c+str(a*b)
        return c 
    elif operation =="%":
        c=c+str(a%b)
        return c 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
