from flask import Flask, render_template, request
import os
import sys


app = Flask('__main__')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")