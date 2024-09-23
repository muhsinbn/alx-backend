#!/usr/bin/env python3
""" Module that creates a flask app."""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ Class that has a language class attr."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ method to display template."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
