from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to caro"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')