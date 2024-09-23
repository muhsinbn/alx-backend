#!/usr/bin/env python3
""" Module that creates a flask app."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ method to display template."""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
