import flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_oauthlib.client import OAuth
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
oauth = OAuth()


slack_oauth = oauth.remote_app('slack',
                               base_url='https://api.slack.com',
                               request_token_url=None,
                               access_token_url='https://slack.com/api/oauth.access',  # noqa
                               authorize_url='https://slack.com/oauth/authorize',  # noqa
                               app_key='SLACK',
                               request_token_params=dict(
                                   scope='identity.basic'
                               ))


@slack_oauth.tokengetter
def _get_slack_token():
    return flask.session.get('slack_token'), ''


def init_app(app):
    """
    Initialize the external application dependencies

    :param app: Flask application instance
    """
    # db, oauth disabled for now TODO
    for extension in [db, login_manager, oauth]:
        extension.init_app(app)
    Migrate(app, db)

    from .models import User

    @login_manager.user_loader
    def _load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except Exception as e:
            return None
