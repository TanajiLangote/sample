import os
from flask import Flask

app = Flask(name)

@app.route("/")
def hello():
    return "Hello, World!\ n these is a sample web by Tanaji"
