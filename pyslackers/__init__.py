from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from pyslackers import external
from pyslackers.bp_main import bp_main


def create_app(config):
    """
    Flask application factory: generate a configured flask
    application.
    :param config: Configuration object or dictionary
    """
    app = Flask('pyslackers')

    app.config.from_object(config)

    external.init_app(app)

    # Register all application blueprints
    # for bp in [bp_auth, bp_main]:  # auth disabled for now
    for bp in [bp_main]:
        app.register_blueprint(bp)

    # http://werkzeug.pocoo.org/docs/0.12/contrib/fixers/#werkzeug.contrib.fixers.ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app
