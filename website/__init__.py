from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from website import external


def create_app(config):
    """
    Flask application factory: generate a configured flask
    application.
    :param config: Configuration object or dictionary
    """
    app = Flask('website')

    app.config.from_object(config)

    external.init_app(app)

    # http://werkzeug.pocoo.org/docs/0.12/contrib/fixers/#werkzeug.contrib.fixers.ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app
