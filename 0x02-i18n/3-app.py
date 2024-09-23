#!/usr/bin/env python3
""" Module that creates a flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


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
    """
    Renders the index page with localized titles and headers.

    This function uses the `gettext` function (aliased as `_`) to
    fetch the localized versions of `home_title` and `home_header`.

    Returns:
        A rendered HTML template for the index page with localized
        content.
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ A method that uses request.accept to determine best match
    for supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
