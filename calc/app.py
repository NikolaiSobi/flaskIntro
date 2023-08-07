# Put your app in here.
#!/usr/bin/env python3
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "WELCOME"

@app.route("/add")
def add_():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = add(a,b)
    return str(total)

@app.route("/sub")
def subtract_():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = sub(a,b)
    return str(total)

@app.route("/mult")
def multiply_():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = mult(a,b)
    return str(total)

@app.route("/div")
def divide_():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = div(a,b)
    return str(total)