from flask import Flask, render_template, request
import os
import sys
import json


app = Flask('__main__')

@app.route('/', method=['GET', 'POST'])
def index():
    if (request.method == "POST"):
        if (request.form['discord_test'] == "discord_test"):            
            os.system('python3 discord_test.py')
        else:
            pass
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")