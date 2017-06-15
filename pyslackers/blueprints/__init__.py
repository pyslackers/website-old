import importlib
import os

from flask import Blueprint, Flask


def init_app(app: Flask) -> None:
    """Auto import and register all blueprints in this
    package."""
    for file_name in os.listdir(os.path.dirname(__file__)):
        if not file_name.startswith('_') and file_name.endswith('.py'):
            import_name = '.{}'.format(os.path.splitext(file_name)[0])
            bp_mod = importlib.import_module(import_name,
                                             package=__name__)
            for _, v in bp_mod.__dict__.items():
                if isinstance(v, Blueprint):
                    app.register_blueprint(v)
